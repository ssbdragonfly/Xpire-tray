import customtkinter as ctk
from pathlib import Path

__all__ = [
    "select_file"
]

def select_file() -> Path:
    ftypes = ("png", "jpeg", "svg", "jfif", "jpg")
    fpath = Path(
        ctk.filedialog.askopenfilename(
            title="Select a File",
            filetypes=[
                ("All files", "*.*"),
                *[
                    (f"{x.upper()} files", f"*.{x}")
                    for x in ftypes
                ],
            ]
        )
    )
    if not fpath.exists():
        raise RuntimeError("CTk Failed somewhere")
    return fpath.absolute()

