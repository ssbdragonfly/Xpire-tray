from backend.utils import *
import customtkinter as ctk

class SearchWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        searches = kwargs.pop("searches")
        super().__init__(*args, **kwargs)
        self.geometry("800x300")
        self.warning_label = ctk.CTkLabel(self, text="Enter which of the following it is: ")
        self.warning_label.pack(padx=20, pady=20)
        self.warning_entry = ctk.CTkEntry(self, width=500, placeholder_text="Enter the intended product")
        self.warning_entry.pack(padx=20, pady=20)
        self.warning_label.config(text="Enter which of the following it is: " + searches)

class PlacementWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        product = kwargs.pop("product")
        super().__init__(*args, **kwargs)
        self.geometry("800x300")
        self.placement_label = ctk.CTkLabel(self, text="Enter the number associated with the location/state of the: Pantry(1) Fridge(2) Opened In the Fridge(3) Freezer(4)")#add new lines if possible
        self.placement_label.pack(padx=20, pady=20)
        self.placement_entry = ctk.CTkEntry(self, width=500, placeholder_text="Enter the placement of the product exactly as stated")
        self.placement_entry.pack(padx=20, pady=20)
        self.placement_label.config(text="Enter the number associated with the location/state of the"+product+": Pantry(1) Fridge(2) Opened In the Fridge(3) Freezer(4)")
def handle_input(products):
    for x in products:
        searches = search_for(x)
        if not isinstance(searches, str):
            top_level_window = SearchWindow(searches = searches)
            entry = top_level_window.warning_entry.get() 
            top_level_window.destroy()
        placement_window = PlacementWindow(product = x)
        entrydict = {
            "1":"pantry",
            "2":"fridge",
            "3":"fridge_after_opening",
            "4":"freezer"
        }
        entryagain = placement_window.placement_entry.get() 
        placement_window.destroy()
        storedfood = food_to_stored_food(get_foods_cached()[entry],storage_location=entrydict[entryagain])
        #database stuff