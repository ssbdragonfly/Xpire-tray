import customtkinter as ctk
from pathlib import Path

def file_data() -> Path:
    fpath = Path(ctk.filedialog.askopenfilename())
    if not fpath.exists():
        raise RuntimeError("CTk Failed somewhere")
    return fpath

