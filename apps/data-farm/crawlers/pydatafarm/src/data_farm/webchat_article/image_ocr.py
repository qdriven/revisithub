import os
import re
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

INPUT_FILE = "urls"  # 你的 URL 文件
SAVE_DIR = Path("downloads")  # 保存目录
WORKERS = 8  # 并发线程数
TIMEOUT = 20  # 每次请求超时秒数
MAX_RETRIES = 3  # 每个 URL 最大重试次数

SAVE_DIR.mkdir(parents=True, exist_ok=True)


def infer_filename(url: str, idx: int) -> str:
    """
    从 URL 推断文件名：
    - 优先使用 wx_fmt 参数作为扩展名
    - 其次使用响应头中的 Content-Type
    - 再次 fallback 为 .bin
    - 基名使用路径倒数两段，避免重复
    """
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    ext = qs.get("wx_fmt", [None])[0]

    parts = [p for p in parsed.path.split("/") if p]
    base = f"{parts[-2]}_{parts[-1]}" if len(parts) >= 2 else f"file_{idx}"
    base = re.sub(r"[^\w\-.]", "_", base)
    if ext:
        return f"{base}.{ext}"
    return f"{base}.bin"


def download_one(url: str, idx: int, timeout=TIMEOUT, max_retries=MAX_RETRIES) -> tuple:
    """
    下载单个 URL 到本地文件，返回 (url, local_path, success, error_msg)
    """
    filename = infer_filename(url, idx)
    dest = SAVE_DIR / filename
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        # 可按需添加来源防盗链： "Referer": "https://your-source-page"
    }
    last_err = None

    # 避免重复下载
    if dest.exists() and dest.stat().st_size > 0:
        return (url, str(dest), True, "exists")

    for attempt in range(1, max_retries + 1):
        try:
            with requests.get(url, headers=headers, stream=True, timeout=timeout) as r:
                r.raise_for_status()
                # 根据响应类型修正扩展名
                content_type = r.headers.get("Content-Type", "")
                if "image/" in content_type:
                    ext_from_ct = content_type.split("/")[-1].split(";")[0].strip()
                    if not dest.suffix.lower().endswith(ext_from_ct):
                        dest = dest.with_suffix(f".{ext_from_ct}")

                with open(dest, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024 * 64):
                        if chunk:
                            f.write(chunk)
                return (url, str(dest), True, "")
        except Exception as e:
            last_err = str(e)
            time.sleep(0.8 * attempt)

    return (url, str(dest), False, last_err or "unknown error")


def read_urls_from_file(path: str):
    urls = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            u = line.strip()
            if not u:
                continue
            # 简单校验是 URL
            if u.startswith("http://") or u.startswith("https://"):
                urls.append(u)
    return urls


def main():
    urls = read_urls_from_file(INPUT_FILE)
    if not urls:
        print("URL 文件为空或未找到有效链接。")
        return

    results = []
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = {executor.submit(download_one, url, idx): (url, idx)
                   for idx, url in enumerate(urls)}
        for fut in as_completed(futures):
            url, idx = futures[fut]
            try:
                res = fut.result()
            except Exception as e:
                res = (url, "", False, f"executor error: {e}")
            results.append(res)

    ok = [r for r in results if r[2]]
    fail = [r for r in results if not r[2]]

    print(f"下载完成：总计 {len(results)}，成功 {len(ok)}，失败 {len(fail)}")
    if ok:
        for i, r in enumerate(results):
            with open(f"image_{i}.png", "wb") as f:
                f.write(r.content)
            print(f"保存完成: image_{i}.png ({len(r.content)} bytes)")

    if fail:
        print("失败列表：")
        for url, path, _, err in fail:
            print(f"- {url} -> {path} ({err})")


if __name__ == "__main__":
    main()
