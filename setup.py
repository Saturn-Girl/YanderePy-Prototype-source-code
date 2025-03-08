from cx_Freeze import setup, Executable
import os

# Include additional files and folders
files = [
    "Yandere-Chan(Player - YanderePy.exe).mtl",
    "Yandere-Chan(Player - YanderePy.exe).obj",
    "ListData.py",
    "bitter chcoc dacoration_syudou_ChiE .wav",
    ("YanderePy.exe prototype_data", "YanderePy.exe prototype_data"),  # Include folder
]

# Executable file
exe = Executable(
    script="YanderePy32.exe.py",
    target_name="YanderePy32.exe",
)

setup(
    name="YanderePy",
    version="1.0",
    description="YanderePy Game",
    options={"build_exe": {"include_files": files}},
    executables=[exe],
)
