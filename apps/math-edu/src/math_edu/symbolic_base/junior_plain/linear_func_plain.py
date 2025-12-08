# --- SymPy 表达式与符号求解 ---
from sympy import symbols, solve, Eq

x, k_sym, b_sym = symbols('x k b')
y_expr = k_sym * x + b_sym  # 一次函数符号表达式
print(f'函数是: {y_expr}')
# 符号求解 x 截距（k≠0）
x0_sym = None
try:
    x0_sym = solve(Eq(y_expr, 0), x)[0]  # 得到 -b/k 的符号表达
except Exception:
    x0_sym = None


k= 10
b=-0.5
print(f'k={k}, b={b}')
# 代入数值得到 x0
x0_val = None
if abs(k) > 1e-8:
    x0_val = x0_sym.subs({k_sym: k, b_sym: b})
x0_text = f"{float(x0_val):.2f}" if x0_val is not None else "不存在（k=0）"

print(x0_text)