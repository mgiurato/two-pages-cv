# CV – LaTeX Build

## Prerequisites

Install a LaTeX distribution with `xelatex` and `biber` available in your PATH:

- **Windows**: [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)
- **macOS**: [MacTeX](https://www.tug.org/mactex/)
- **Linux**: `sudo apt install texlive-full` (or equivalent)

Verify the installation:

```bash
xelatex --version
biber --version
```

## Build

Generates `main.pdf` by running the full compilation sequence (`xelatex` → `biber` → `xelatex` → `xelatex`):

```bash
python build.py
```

Temporary files (`.aux`, `.bbl`, `.log`, etc.) are placed in the `build/` subdirectory.

## Clean

Removes the `build/` directory with all temporary files generated during compilation:

```bash
python build.py clean
```

## Compiler options

If `xelatex` is not available, change the following line in `build.py`:

```python
LATEX_CMD = "xelatex"   # or "lualatex" or "pdflatex"
```

> **Note**: `pdflatex` does not support OpenType fonts; some typographic features may not render correctly.
