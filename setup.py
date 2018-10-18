import os.path, cx_Freeze

### setting environment variables dynamically to void key error on local machines
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ["TCL_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tcl8.6")
os.environ["TK_LIBRARY"] = os.path.join(PYTHON_INSTALL_DIR, "tcl", "tk8.6")

executables = [cx_Freeze.Executable("Race_the_car.py")]
cx_Freeze.setup(
    name="RacetheCar",
    options={
        "build_exe": {
            "packages": [
                "pygame",
                "sys",
                "pygame.surfarray",
                "numpy",
                "pygame._numpysurfarray",
            ],
            "include_files": [
                "red2.jpg",
                "blue2.jpg",
                "car_11.png",
                "car_22.png",
                "hm2.jpg",
            ],
        }
    },
    executables=executables,
)
