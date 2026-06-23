#!/usr/bin/env python3
"""Build script for the CV LaTeX project."""

import subprocess
import sys
import os

MAIN = "main"
# Change to "pdflatex" or "lualatex" if you don't have XeLaTeX installed
LATEX_CMD = "xelatex"
# Temporary files are placed in this subdirectory
BUILD_DIR = "build"


def run(cmd: list[str]) -> None:
    print(f"\n>>> {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"\nERROR: command failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def build() -> None:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(BUILD_DIR, exist_ok=True)
    # -aux-directory puts all temp files in BUILD_DIR (MiKTeX); PDF stays in cwd
    latex_flags = [
        "-interaction=nonstopmode",
        f"-aux-directory={BUILD_DIR}",
    ]
    run([LATEX_CMD] + latex_flags + [f"{MAIN}.tex"])
    # Biber reads/writes from BUILD_DIR
    run(["biber", "--input-directory", BUILD_DIR, "--output-directory", BUILD_DIR, MAIN])
    run([LATEX_CMD] + latex_flags + [f"{MAIN}.tex"])
    run([LATEX_CMD] + latex_flags + [f"{MAIN}.tex"])
    print(f"\nDone! Output: {MAIN}.pdf")


def clean() -> None:
    import shutil
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
        print(f"Removed directory: {BUILD_DIR}/")
    else:
        print("Nothing to clean.")
    print("Clean done.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "clean":
            clean()
        else:
            print(f"ERROR: unknown command '{sys.argv[1]}'. Usage: python build.py [clean]")
            sys.exit(1)
    else:
        build()
