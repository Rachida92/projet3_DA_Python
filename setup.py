from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["front_end", "back_end"]
}

setup(
    version="1",
    name="MacGyver",
    description="Votre programme",
    executables=[Executable("main.py")],
    options={"build_exe": build_exe_options},
)
