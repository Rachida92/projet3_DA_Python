import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe':{
        'includes': ["front_end", "back_end"]
                 }

}
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables=[
        Executable("main.py", base=base)
]

setup(
    version="1",
    name="MacGyver",
    description="Votre programme",
    options=options,
    executables=executables
)
