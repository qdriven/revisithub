import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, Eq, solve, S

st.set_page_config(page_title="DK一分钟数学 · L01 SymPy版", page_icon="⏱️", layout="centered")

st.title("DK一分钟数学 · 一次函数 y = kx + b（SymPy 简洁版）")
st.caption("符号推导 + 图像直观：可复现学习。固定坐标，更显眼的关键指标。")

# 仅两个滑块
k_val = st.slider("斜率 k", -3.0, 3.0, 1.0, 0.1)
b_val = st.slider("截距 b", -5.0, 5.0, 0.0, 0.5)

# 符号构造（SymPy）
x, k, b = symbols('x k b')
y_expr = k*x + b  # 符号表达式
# 符号求解 x 截距
x0_expr = None
if k != 0:
    try:
        x0_expr = solve(Eq(y_expr, 0), x)[0]  # 期望为 -b/k
    except Exception:
        x0_expr = None

# 用数值替换（subs）得到具体表达式与数值
y_num = y_expr.subs({k: S(k_val), b: S(b_val)})
x0_num = None
y_check = None
if abs(k_val) > 1e-12 and x0_expr is not None:
    x0_num = x0_expr.subs({k: S(k_val), b: S(b_val)})
    y_check = y_expr.subs({x: x0_num, k: S(k_val), b: S(b_val)})

# 展示：大字表达式与指标
expr_text = f"y = {k_val:.2f}x + {b_val:.2f}"
x0_text = f"{float(x0_num):.2f}" if x0_num is not None else "不存在（k=0）"
ycheck_text = "0（验证通过）" if y_check is not None and float(y_check) == 0.0 else ("—" if y_check is None else f"{float(y_check):.2e}")

st.markdown(f"### 当前函数：{expr_text}")
c1, c2, c3 = st.columns(3)
c1.metric("x 截距（符号解）", x0_text)
c2.metric("y 截距 b", f"{b_val:.2f}")
c3.metric("代回验证 y(x0)", ycheck_text)

# 固定坐标
x_min, x_max = -5, 5
y_min, y_max = -5, 5

# 采样绘图（NumPy 仅用于取点）
xs = np.linspace(x_min, x_max, 400)
ys = k_val * xs + b_val

fig = go.Figure()
# 直线
fig.add_trace(go.Scatter(
    x=xs, y=ys, mode="lines",
    name=expr_text, line=dict(color="#1F77B4", width=5)
))
# y 截距
fig.add_trace(go.Scatter(
    x=[0], y=[b_val], mode="markers+text",
    text=[f"(0, {b_val:.2f})"], textposition="top center",
    marker=dict(color="#D62728", size=12, symbol="circle"),
    name="y 截距"
))
# x 截距
if x0_num is not None:
    x0f = float(x0_num)
    fig.add_trace(go.Scatter(
        x=[x0f], y=[0], mode="markers+text",
        text=[f"({x0f:.2f}, 0)"], textposition="bottom center",
        marker=dict(color="#2CA02C", size=12, symbol="diamond"),
        name="x 截距"
    ))

# 固定轴范围和样式
fig.update_layout(
    template="plotly_white",
    height=520,
    xaxis=dict(title="x", range=[x_min, x_max], zeroline=True, zerolinewidth=2, zerolinecolor="#AAAAAA",
               showgrid=True, gridcolor="#EEEEEE"),
    yaxis=dict(title="y", range=[y_min, y_max], zeroline=True, zerolinewidth=2, zerolinecolor="#AAAAAA",
               showgrid=True, gridcolor="#EEEEEE"),
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(orientation="h")
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("今日任务卡（固定坐标）")
st.markdown("- 用 SymPy 的符号解理解 x 截距：当 k ≠ 0，x0 = -b/k；把 x0 代回 y 应为 0。")
st.markdown("- 目标：设置 k=-1.5、b=2.0；截图并用一句话解释这条线的现实意义。")
st.info("提交入口（请替换为你的表单链接）：https://your-form-url")
