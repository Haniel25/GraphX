import numpy as np

def plot_functions(ax, functions):
    x = np.linspace(-10, 10, 2000)

    # plan orthonormé
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    ax.grid(True, linestyle="--", alpha=0.6)

    for f in functions:
        try:
            expr = f.replace("^", "**")

            # ⚠️ IMPORTANT : conversion SIMPLE (sans np.)
            expr = expr.replace("ln(", "ln(")
            expr = expr.replace("log(", "log(")
            expr = expr.replace("exp(", "exp(")
            expr = expr.replace("sqrt(", "sqrt(")

            print("DEBUG expr =", expr)

            y = eval(expr, {
                "x": x,
                "sin": np.sin,
                "cos": np.cos,
                "exp": np.exp,
                "log": np.log10,
                "ln": np.log,
                "sqrt": np.sqrt
            })

            ax.plot(x, y, label=f)

        except Exception as e:
            print("ERROR:", f, e)

    ax.legend()