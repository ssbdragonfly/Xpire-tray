from backend.data import FoodData
from backend.utils import *
import customtkinter as ctk

class _Window(ctk.CTkToplevel):
    def __init__(self, *texts, **kwargs):
        super().__init__(**kwargs)
        assert len(texts) == 2
        self.geometry("800x300")
        self.label = ctk.CTkLabel(self, text=texts[0])
        self.label.pack(padx=20, pady=20)
        self.entry = ctk.CTkEntry(self, width=500, placeholder_text=texts[1])
        self.entry.pack(padx=20, pady=20)
        self.next = ctk.CTkButton(self, text="Next", command=self.quit)
        self.next.pack(pady=20)


class SearchWindow(_Window):
    def __init__(self, searches, **kwargs):
        super().__init__(
            "Enter which of the following it is: ",
            "Enter the intended product",
            **kwargs
        )
        self.label.configure(text=f"Enter which of the following it is: ")
        ctk.CTkLabel(self, text='\n'.join(x for x in searches)).pack(pady=20)
        self.mainloop()

class PlacementWindow(_Window):
    def __init__(self, product, **kwargs):
        super().__init__(
            "Enter the number associated with the location/state of the: Pantry(1) Fridge(2) Opened In the Fridge(3) Freezer(4)",
            "Enter the placement of the product exactly as stated",
            **kwargs
        )
        self.label.configure(text=f"Enter the number associated with the location/state of the {product}:\nPantry(1)\nFridge(2)\nOpened In the Fridge(3)\nFreezer(4)")
        self.mainloop()

def handle_input(products: list[str]):
    for x in products:
        searches = search_for(x, get_foods_cached())
        if not isinstance(searches, FoodData):
            top_level_window = SearchWindow(searches = searches)
            entry = top_level_window.entry.get() 
            top_level_window.destroy()
        else:
            entry = searches.name
        while True:
            placement_window = PlacementWindow(product = x)
            entrydict = {
                "1":"pantry",
                "2":"fridge",
                "3":"fridge_after_opening",
                "4":"freezer"
            }
            entryagain = placement_window.entry.get() 
            if entryagain.isnumeric():
                break
            else:
                print("Please enter a number!")

        placement_window.destroy()
        storedfood = food_to_stored_food(get_foods_cached()[entry],storage_location=entrydict[entryagain])
        #database stuff
