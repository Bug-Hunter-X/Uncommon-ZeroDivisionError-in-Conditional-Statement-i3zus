def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') if b >0 else float('-inf') if b < 0 else float('nan')
    else:
        return a / b