import customtkinter as ctk
from backend import *

ctk.set_appearance_mode("dark")   
ctk.set_default_color_theme("blue")

width, height = 1000, 600
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Food Expire-E Program")   #change the name later
        self.geometry(f"{width}x{height}")    

        pack_kwargs = {
            "pady": 20,
            "padx": 20,
            "anchor": "w"
        }

        # Products Label
        self.product_label = ctk.CTkLabel(
            self,
            text="Products"
        )
        self.product_label.pack(**pack_kwargs)
 
        # Product Entry Field
        self.product_entry = ctk.CTkEntry(
            self,
            placeholder_text="Comma seperated list!"
        )
        self.product_entry.pack(**pack_kwargs)

        # Generate Button
        self.gen_results_button = ctk.CTkButton(
            self,
            text="Generate Results",
            command=self.create_text
        )
        self.gen_results_button.pack(**pack_kwargs)

    @staticmethod
    def filter_input(s: str) -> list[str]:
        s.replace(" ","")
        while s.count(",,"):
            s.replace(",,",",")
        return s.split(",")

    def create_text(self):
        expireitems = self.product_entry.get()
        expireitems = [x for x in self.filter_input(expireitems) if x]
        self.handle_input(expireitems)
    
    def handle_input(self, products: list[str]):
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
                    Popup("Please enter a number!", master=self)

            placement_window.destroy()
            tmp = get_foods_cached()[entry]
            storedfood = food_to_stored_food(tmp, storage_location=entrydict[entryagain])
            if storedfood.max_time == -1:
                attrs = entrydict.values()
                location = sorted(
                    attrs,
                    key=(lambda i: getattr(storedfood, i)),
                    reverse=True
                )[0]
                Popup(message=f"Please put it in the {location}")
                storedfood = food_to_stored_food(tmp, storage_location=entrydict[location])

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
