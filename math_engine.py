def clean_expression(expr):
    expr = expr.replace(" ", "")
    expr = expr.replace("^", "**")

    return fix_implicit_multiplication(expr)


def fix_implicit_multiplication(expr):
    new_expr = ""

    for i in range(len(expr)):
        new_expr += expr[i]

        if i < len(expr) - 1:

            # 3x -> 3*x
            if (expr[i].isdigit() or expr[i] == ")") and expr[i+1] == "x":
                new_expr += "*"

            # x3 -> x*3
            if expr[i] == "x" and expr[i+1].isdigit():
                new_expr += "*"

            # )x -> )*x
            if expr[i] == ")" and expr[i+1] == "x":
                new_expr += "*"

    return new_expr


def suggest_help(expr):
    if expr == "":
        return ["Ex: x^2, 3x+2, sin(x), cos(x), exp(x), ln(x)"]
    return []