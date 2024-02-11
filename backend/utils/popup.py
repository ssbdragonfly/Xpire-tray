from CTkMessagebox import CTkMessagebox

class Popup(CTkMessagebox):
    def __init__(self, message: str, **kwargs) -> None:
        super().__init__(message=message, **kwargs)