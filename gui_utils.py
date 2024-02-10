import customtkinter as ctk
from pathlib import Path

def select_file() -> Path:
    fpath = Path(ctk.filedialog.askopenfilename())
    if not fpath.exists():
        raise RuntimeError("CTk Failed somewhere")
    return fpath.absolute()

