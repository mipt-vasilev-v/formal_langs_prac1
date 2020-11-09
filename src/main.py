from regular_expr_reader import RegularExpressionReader

regular_expr = input()
mod = int(input())
remainder = int(input())
solver = RegularExpressionReader(regular_expr)
result = solver.FindMinLenEqualToRemainderByMod(mod, remainder)
if isinstance(result, int):
    print(result)
else:
    print("INF")
