import customtkinter as ctk

__all__ = [
    "SearchWindow",
    "PlacementWindow"
]

class _Window(ctk.CTkToplevel):
    def __init__(self, *texts, **kwargs):
        super().__init__(**kwargs)
        assert len(texts) == 2
        self.geometry("800x300")
        self.label = ctk.CTkLabel(self, text=texts[0])
        self.entry = ctk.CTkEntry(self, width=500, placeholder_text=texts[1])
        self.next = ctk.CTkButton(self, text="Next", command=self.quit)
        
        self._pack_kwargs = {
            "padx": 20,
            "pady": 20
        }
        to_pack = (
            "entry",
            "label",
            "next"
        )
        for attr in to_pack:
            getattr(self, attr).pack(**self._pack_kwargs)
            
        self.focus_force()
    
    def _init(self) -> None:
        self.mainloop()


class SearchWindow(_Window):
    def __init__(self, searches: list[str], **kwargs):
        super().__init__(
            "Enter which of the following matches what you entered: ",
            "Enter the intended product",
            **kwargs
        )
        ctk.CTkLabel(self, text='\n'.join(x for x in searches)).pack(**self._pack_kwargs)
        self._init()

class PlacementWindow(_Window):
    def __init__(self, product: str, **kwargs):
        super().__init__(
            f"Enter the number associated with the location/state of the {product}:",
            "Enter the placement of the product exactly as stated",
            **kwargs
        )
        locations = ("(1) Pantry", "(2) Fridge", "(3) Opened In the Fridge", "(4) Freezer")
        ctk.CTkLabel(self, text="\n".join(locations)).pack(**self._pack_kwargs)
        self._init()