import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, Eq, solve

st.set_page_config(page_title="DK一分钟数学 · SymPy版 一次函数", page_icon="⏱️", layout="centered")

st.title("一分钟数学 · SymPy版｜一次函数 y = kx + b（原点居中坐标）")
st.caption("用 SymPy 构造表达式与求解，用 Plotly 在原点居中的坐标系上可视化。")

# --- SymPy 表达式与符号求解 ---
x, k_sym, b_sym = symbols('x k b')
y_expr = k_sym * x + b_sym  # 一次函数符号表达式

# --- 控件 ---
col1, col2 = st.columns(2)
with col1:
    k = st.slider("斜率 k", -5.0, 5.0, 1.0, 0.1)
    b = st.slider("截距 b", -20.0, 20.0, 0.0, 0.5)
with col2:
    axis_limit = st.slider("坐标轴范围（对称）", 5, 50, 10, 1)  # 坐标范围 [-L, L]
    show_points = st.checkbox("显示关键点（x截距与y截距）", True)

# 符号求解 x 截距（k≠0）
x0_sym = None
try:
    x0_sym = solve(Eq(y_expr, 0), x)[0]  # 得到 -b/k 的符号表达
except Exception:
    x0_sym = None

# 代入数值得到 x0
x0_val = None
if abs(k) > 1e-8:
    x0_val = x0_sym.subs({k_sym: k, b_sym: b})
x0_text = f"{float(x0_val):.2f}" if x0_val is not None else "不存在（k=0）"

# 指标面板（含 SymPy 结果）
c1, c2, c3 = st.columns(3)
c1.metric("x 截距（符号→数值）", x0_text)
c2.metric("y 截距 b", f"{b:.2f}")
c3.metric("|k|（陡缓程度）", f"{abs(k):.2f}")

# --- 数据与图像 ---
xs = np.linspace(-axis_limit, axis_limit, 800)
ys = k * xs + b

fig = go.Figure()

# 直线
fig.add_trace(go.Scatter(
    x=xs, y=ys, mode="lines",
    name=f"y={k:.2f}x+{b:.2f}",
    line=dict(color="#1F77B4", width=3)
))

# 关键点
if show_points:
    # y截距 (0, b)
    fig.add_trace(go.Scatter(
        x=[0], y=[b], mode="markers+text", text=["(0, b)"],
        textposition="top center", marker=dict(color="#D62728", size=10),
        name="y截距"
    ))
    # x截距 (x0, 0)
    if x0_val is not None and -axis_limit <= float(x0_val) <= axis_limit:
        fig.add_trace(go.Scatter(
            x=[float(x0_val)], y=[0], mode="markers+text", text=["(x0, 0)"],
            textposition="bottom center", marker=dict(color="#2CA02C", size=10),
            name="x截距"
        ))

# --- 原点居中的大坐标轴（带箭头与刻度） ---
# x 轴
fig.add_shape(type="line", x0=-axis_limit, y0=0, x1=axis_limit, y1=0,
              line=dict(color="#000000", width=2))
# y 轴
fig.add_shape(type="line", x0=0, y0=-axis_limit, x1=0, y1=axis_limit,
              line=dict(color="#000000", width=2))

# 轴箭头（用短线段模拟箭头）
arrow_len = axis_limit * 0.05
fig.add_shape(type="line", x0=axis_limit - arrow_len, y0=arrow_len, x1=axis_limit, y1=0,
              line=dict(color="#000000", width=2))
fig.add_shape(type="line", x0=axis_limit - arrow_len, y0=-arrow_len, x1=axis_limit, y1=0,
              line=dict(color="#000000", width=2))

fig.add_shape(type="line", x0=arrow_len, y0=axis_limit, x1=0, y1=axis_limit,
              line=dict(color="#000000", width=2))
fig.add_shape(type="line", x0=-arrow_len, y0=axis_limit, x1=0, y1=axis_limit,
              line=dict(color="#000000", width=2))

# 刻度（每单位刻度线）
tick_step = max(1, axis_limit // 10)  # 合理步长
ticks = np.arange(-axis_limit, axis_limit + 1e-9, tick_step)
for t in ticks:
    # x轴刻度
    fig.add_shape(type="line", x0=t, y0=-0.3, x1=t, y1=0.3,
                  line=dict(color="#888888", width=1))
    if t != 0:
        fig.add_trace(go.Scatter(x=[t], y=[-0.8], mode="text",
                                 text=[str(int(t))], textposition="bottom center",
                                 showlegend=False))
    # y轴刻度
    fig.add_shape(type="line", x0=-0.3, y0=t, x1=0.3, y1=t,
                  line=dict(color="#888888", width=1))
    if t != 0:
        fig.add_trace(go.Scatter(x=[-0.8], y=[t], mode="text",
                                 text=[str(int(t))], textposition="middle right",
                                 showlegend=False))

# 视觉与范围设置（原点居中、方形比例）
fig.update_layout(
    template="plotly_white",
    height=640,
    xaxis=dict(range=[-axis_limit, axis_limit], zeroline=False, showgrid=False, scaleanchor="y", scaleratio=1),
    yaxis=dict(range=[-axis_limit, axis_limit], zeroline=False, showgrid=False),
    margin=dict(l=20, r=20, t=40, b=20),
    legend=dict(orientation="h")
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("今日任务卡（SymPy验证）")
st.markdown("- 用 SymPy 符号解得到 x0 = -b/k；把当前 k,b 代入得到数值 x0，并在图上找到 (x0,0)。")
st.markdown("- 截图并用一句话解释：k 表示上升/下降的快慢，b 表示起点。")

st.info("提交入口（请替换为你的表单链接）：https://your-form-url")
