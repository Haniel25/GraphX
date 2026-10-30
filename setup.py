from cx_Freeze import setup, Executable

setup(
    name="GraphX",
    version="1.0",
    description="GraphX Application",
    executables=[
        Executable(
            script="main.py",
            base="gui",   # ✅ IMPORTANT (Python 3.12+ / 3.14)
            icon="GraphX.ico"
        )
    ]
)