import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable(
    script = "alien_invasion.py", 
    icon = "alien_invasion.ico", 
    base = base)]

include_files = ([
    "assets/images/small_spaceship.bmp", 
    "assets/images/spaceship.bmp", "assets/images/alien.bmp", 
    "assets/images/play_button.bmp", 
    "assets/images/help_button.bmp", "assets/images/exit_button.bmp", 
    "assets/images/resume_button.bmp", "assets/images/quit_button.bmp", 
    "assets/images/back_button.bmp", "assets/images/ok_button.bmp", 
    "assets/fonts/silkscreen.ttf"])

includes = []
excludes = ["Tkinter"]
packages = ["pygame"]

setup(
    name = "Alien Invasion", 
    version = "1.0", 
    description = ("Shoot down as many aliens as you can, before the wave of "
        "aliens reaches the spaceship."), 
    options = ({"build_exe": ({
        "includes": includes, 
        "excludes": excludes, 
        "packages": packages, 
        "include_files": include_files})
    }), 
    executables = executables)