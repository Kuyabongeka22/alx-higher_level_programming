#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        results = a/b
    except (TypeError, ZeroDivisionError, ValueError):
        return None
    else:
        return result
    finally:
        print("{}".format(results))

