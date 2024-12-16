def function_with_uncommon_error(x):
    if x == 0:
        return float('inf') # Or raise a more descriptive exception, like ValueError
    else:
        return x + 5