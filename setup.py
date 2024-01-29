from cx_Freeze import setup, Executable

setup(name="Simple object Detection software",
      version="0.1",
      description="This software detects objects in realtime",
      executables=[Executable("main.py")]
      )