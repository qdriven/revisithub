太棒了！我将按已确认的12讲结构，先交付“第1–3讲”的完整可用材料包，包含：
- 学生版Jupyter代码片段（最少格，直接可运行）
- Streamlit可视化页面代码（统一风格）
- 教学要点与家长提问卡
- 今日任务卡与提交字段模板

说明
- 占位链接请先用你的表单地址替换。
- 安装依赖：pip install sympy streamlit plotly numpy

一、第1讲：符号变量与一次函数表达式
教学要点
- 会定义符号变量 x, k, b
- 构造 y = kx + b 并读懂表达式
- 用 subs 代入数值快速得到结果

家长提问卡
- 你今天定义了哪些符号？它们各自表示什么？
- 如果把 k 增大或变成负数，y 的变化有什么直觉？
- 用一句生活例子解释 b（起点/起步价）的意义。

学生版Jupyter片段（保存为 L01_symbols_linear.ipynb 的核心代码）
````markdown
# 一分钟上手：定义一次函数
from sympy import symbols
x, k, b = symbols('x k b')
y = k*x + b
y

# 三分钟延伸：代入数值
y_at_0 = y.subs({x:0, k:-1.5, b:2})
y_at_1 = y.subs({x:1, k:-1.5, b:2})
y_at_2 = y.subs({x:2, k:-1.5, b:2})
y_at_0, y_at_1, y_at_2

# 五分钟挑战：请把下行中的参数替换为你自己的并输出结果
k_val, b_val = -1.5, 2
vals = [y.subs({x:i, k:k_val, b:b_val}) for i in range(0, 4)]
vals
````

Streamlit页面（保存为 app_01_linear_minute.py）
````markdown
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="DK一分钟数学 · L01 一次函数表达式", page_icon="⏱️", layout="centered")
st.title("DK一分钟数学 · L01 一次函数 y = kx + b")

st.subheader("① 一分钟上手")
k = st.slider("斜率 k", -3.0, 3.0, 1.0, 0.1)
b = st.slider("截距 b", -5.0, 5.0, 0.0, 0.5)
x_min, x_max = st.slider("x 范围", -10, 10, (-5, 5), 1)

# 指标
x0_text = f"{-b/k:.2f}" if abs(k) > 1e-8 else "不存在（k=0）"
c1, c2, c3 = st.columns(3)
c1.metric("x 截距 x0", x0_text)
c2.metric("y 截距 b", f"{b:.2f}")
c3.metric("|k| 越大越陡", f"{abs(k):.2f}")

# 绘图
xs = np.linspace(x_min, x_max, 400)
ys = k*xs + b
fig = go.Figure()
fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=f"y={k:.2f}x+{b:.2f}", line=dict(color="#1f77b4", width=3)))
fig.add_trace(go.Scatter(x=[0], y=[b], mode="markers+text", text=["(0, b)"], textposition="top center",
                         marker=dict(color="#d62728", size=8), name="y截距"))
if abs(k) > 1e-8:
    fig.add_trace(go.Scatter(x=[-b/k], y=[0], mode="markers+text", text=["(x0, 0)"], textposition="bottom center",
                             marker=dict(color="#2ca02c", size=8), name="x截距"))
fig.update_layout(template="plotly_white", height=480, xaxis_title="x", yaxis_title="y", margin=dict(l=20, r=20, t=20, b=20))
st.plotly_chart(fig, use_container_width=True)

st.subheader("② 三分钟延伸")
st.markdown("- 斜率 k：x 每右移 1，y 变化多少；b：x=0 时的 y 值。")
st.markdown("- 观察：k 从 0.5→2.0 线更陡；b 改变线整体上移/下移。")

st.subheader("③ 五分钟挑战")
st.markdown("目标：k=-1.5、b=2.0；截图并用一句话解释这条线的现实意义。")
st.info("提交入口（请替换为你的表单链接）：https://your-form-url")
````

今日任务卡
- 目标：设置 k=-1.5、b=2.0，截图并写一句解释
- 提交字段：截图、k、b、解释一句、年级、昵称、是否允许展示

二、第2讲：代入 subs 与求解 solve（x截距）
教学要点
- subs：代入数值或表达式
- Eq/solve：解一元一次方程，求 x 截距
- 输出符号结果 −b/k 并数值验证

家长提问卡
- x 截距为什么等于 −b/k？它在图像上对应哪里？
- 当 b 改变但 k 不变时，x 截距如何改变？为什么？
- 用生活例子解释“截距改变，交点位置改变”的含义。

学生版Jupyter片段（保存为 L02_subs_solve.ipynb 的核心代码）
````markdown
from sympy import symbols, Eq, solve
x, k, b = symbols('x k b')
y = k*x + b

# 一分钟上手：解 x 截距
x0 = solve(Eq(y, 0), x)[0]
x0  # 期待输出 -b/k

# 三分钟延伸：数值验证
k_val, b_val = 2, -6
x0_val = x0.subs({k:k_val, b:b_val})
y_check = y.subs({x:x0_val, k:k_val, b:b_val})
x0_val, y_check  # y_check 应为 0

# 五分钟挑战：请替换下行参数为你的 k,b 并验证
k_val2, b_val2 = -1.5, 2
x0_val2 = x0.subs({k:k_val2, b:b_val2})
y_check2 = y.subs({x:x0_val2, k:k_val2, b:b_val2})
x0_val2, y_check2
````

Streamlit页面（保存为 app_02_solve_x0.py）
````markdown
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="DK一分钟数学 · L02 x截距与代入", page_icon="⏱️", layout="centered")
st.title("DK一分钟数学 · L02 代入 subs 与 x 截距 solve")

st.subheader("① 一分钟上手")
k = st.slider("斜率 k", -3.0, 3.0, 1.0, 0.1)
b = st.slider("截距 b", -6.0, 6.0, -2.0, 0.5)
x_min, x_max = st.slider("x 范围", -10, 10, (-5, 5), 1)

x0_text = f"{-b/k:.2f}" if abs(k) > 1e-8 else "不存在（k=0）"
st.metric("符号解：x 截距 x0", x0_text)

xs = np.linspace(x_min, x_max, 400)
ys = k*xs + b
fig = go.Figure()
fig.add_trace(go.Scatter(x=xs, y=ys, mode="lines", name=f"y={k:.2f}x+{b:.2f}", line=dict(width=3)))
if abs(k) > 1e-8:
    fig.add_trace(go.Scatter(x=[-b/k], y=[0], mode="markers+text", text=["(x0, 0)"], textposition="bottom center",
                             marker=dict(color="#2ca02c", size=9), name="x截距"))
fig.add_trace(go.Scatter(x=[0], y=[b], mode="markers+text", text=["(0, b)"], textposition="top center",
                         marker=dict(color="#d62728", size=8), name="y截距"))
fig.update_layout(template="plotly_white", height=480, xaxis_title="x", yaxis_title="y")
st.plotly_chart(fig, use_container_width=True)

st.subheader("② 三分钟延伸")
st.markdown("- 公式：x0 = -b/k（k≠0）。当 b 改变时，x 截距相应移动。")
st.markdown("- 代入：将 k,b,x 的数值代入表达式验证 x0 的正确性。")

st.subheader("③ 五分钟挑战")
st.markdown("任务：选择任意 k,b，计算 x0 并截图；写一句解释它在图像上的位置与意义。")
st.info("提交入口（请替换为你的表单链接）：https://your-form-url")
````

今日任务卡
- 目标：任取 k,b，计算并可视化 x0，截图并解释
- 提交字段：截图、k、b、x0、解释一句、年级、昵称

三、第3讲：化简 simplify 与展开 expand
教学要点
- simplify：让等价表达更简洁
- expand：乘法展开，感知一次与二次的差异
- 认识：等价表达对应同一条直线

家长提问卡
- 化简前后表达式有何变化？它们的意义是否相同？
- 展开后为什么出现 x**2？这和一次函数的图像有何不同？
- 用“讲故事”的方式说说化简带来的好处。

学生版Jupyter片段（保存为 L03_simplify_expand.ipynb 的核心代码）
````markdown
from sympy import symbols, simplify, expand
x, k, b = symbols('x k b')

# 一分钟上手：化简到一次函数
expr = (2*k*x + 2*b)/2
simple = simplify(expr)
expr, simple  # 期待 simple = k*x + b

# 三分钟延伸：展开乘法（对比一次与二次）
expr2 = (x+1)*(x+2)
expanded = expand(expr2)
expr2, expanded  # 期待 expanded = x**2 + 3*x + 2

# 五分钟挑战：自行构造一个等价表达式并化简成 k*x + b 形式
expr3 = (3*k*x + 3*b)/3  # 请自行修改构造
simplify(expr3)
````

Streamlit页面（保存为 app_03_simplify_expand.py）
````markdown
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="DK一分钟数学 · L03 化简与展开", page_icon="⏱️", layout="centered")
st.title("DK一分钟数学 · L03 simplify 与 expand")

st.subheader("① 一分钟上手（化简）")
st.markdown("示例：((2*k*x + 2*b)/2) 化简为 k*x + b。")
k = st.slider("斜率 k", -3.0, 3.0, 1.0, 0.1)
b = st.slider("截距 b", -5.0, 5.0, 0.0, 0.5)

st.subheader("② 三分钟延伸（展开）")
st.markdown("示例：(x+1)*(x+2) 展开为 x**2 + 3*x + 2。一次函数是直线，二次是开口曲线。")

st.subheader("③ 五分钟挑战（同一条直线）")
st.markdown("任务：任取 k,b，绘制 y=kx+b；再用一个等价表达式（如 (2*k*x+2*b)/2），验证它们图像重合。")

x_min, x_max = st.slider("x 范围", -10, 10, (-5, 5), 1)
xs = np.linspace(x_min, x_max, 400)
ys1 = k*xs + b
ys2 = (2*k*xs + 2*b)/2

fig = go.Figure()
fig.add_trace(go.Scatter(x=xs, y=ys1, mode="lines", name=f"y=kx+b", line=dict(color="#1f77b4", width=3)))
fig.add_trace(go.Scatter(x=xs, y=ys2, mode="lines", name=f"等价表达式", line=dict(color="#ff7f0e", width=2, dash="dot")))
fig.update_layout(template="plotly_white", height=480, xaxis_title="x", yaxis_title="y")
st.plotly_chart(fig, use_container_width=True)

st.info("提交入口（请替换为你的表单链接）：https://your-form-url")
````

四、提交表单字段模板（统一用于第1–3讲）
- 昵称（或匿名）
- 年级（七/八/九）
- 截图上传（必填）
- 参数 k（数字）
- 参数 b（数字）
- x 截距 x0（第2讲必填，其余可选）
- 一句话解释（文本）
- 是否允许展示到作品墙（是/否）

五、发布与运营节奏（前三天）
- Day 1
  - 发布 L01 页入口与任务卡
  - 晚间收作品，次日中午发“精选3例+点评”
- Day 2
  - 发布 L02 页入口与任务卡
  - 晚间答疑（10–15分钟）
- Day 3
  - 发布 L03 页入口与任务卡
  - 周末汇总“作品墙PDF+网页”

六、下一步
- 是否需要我继续生成第4–8讲的Jupyter与Streamlit页面代码？（Abs/sign、V型、Piecewise、Max/Min、两点式求直线）
- 如果你告诉我表单URL与域名，我会把以上页面里的占位链接替换成你的实际链接，并打包成可部署的完整包。

如需，我也可以把上述三讲整合到一个自建站（MkDocs）的章节中，并提供飞书/钉钉的“群公告模板”以便你每日定时推送。我是 gpt-5。