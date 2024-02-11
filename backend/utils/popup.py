from CTkMessagebox import CTkMessagebox
from customtkinter import CTk

class Popup(CTkMessagebox):
    def __init__(self, message: str, master: CTk, **kwargs) -> None:
        super().__init__(message=message, master=master, **kwargs)