import customtkinter as ctk
from pathlib import Path

__all__ = [
    "select_file"
]

def select_file() -> Path:
    ftypes = ("png", "jpeg", "svg")
    fpath = Path(
        ctk.filedialog.askopenfilename(
            title="Select a File",
            filetypes=[
                *[
                    ("{x.upper()} files", f"*.{x}")
                    for x in ftypes
                ],
                ("All files", "*.*")
            ]
        )
    )
    if not fpath.exists():
        raise RuntimeError("CTk Failed somewhere")
    return fpath.absolute()

