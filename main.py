import customtkinter as ctk
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageDraw
from backend import *

ctk.set_appearance_mode("dark")   
ctk.set_default_color_theme("blue")

width, height = 1000, 600
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(TITLE)   #change the name later
        self.geometry(f"{width}x{height}")
        self.homepage()

    def homepage(self) -> None:
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
            command=self.add_by_name
        )
        self.gen_results_button.pack(**pack_kwargs)
        
        self.upload_from_file = ctk.CTkButton(
            self,
            text="Choose file",
            command=self.add_from_file
        )
        self.upload_from_file.pack(**pack_kwargs)
        
        assess = lambda: None # to remove later
        
        self.ml_regression_button = ctk.CTkButton(
            self,
            text="Nutrition Assesment",
            command=assess
        )
        self.ml_regression_button.pack(**(pack_kwargs | {"pady": 70}))

    @staticmethod
    def filter_input(s: str) -> list[str]:
        s.replace(" ","")
        while s.count(",,"):
            s.replace(",,",",")
        return s.split(",")

    def create_text(self) -> list[str]:
        expireitems = self.product_entry.get()
        expireitems = [x for x in self.filter_input(expireitems) if x]
        return expireitems
    
    def add_by_name(self) -> None:
        new_database_members = self.create_text()
        self.handle_input(new_database_members)
        
    def add_from_file(self) -> None:
        img_info = get_image_info()
        if img_info == ExitCode.FAILURE:
            return
        elif not img_info:
            raise Exception("API Error: Something went wrong")
        food_name = img_info["foodName"]
        self.handle_input([food_name.capitalize()] if isinstance(food_name, str) else [food_name[0].capitalize()])
    
    def handle_input(self, products: list[str]):
        new_database_members = []
        for prod in products:
            searches = search_for(prod, get_foods_cached())
            if not isinstance(searches, FoodData):
                top_level_window = SearchWindow(searches = searches)
                entry = top_level_window.entry.get()
                if entry.isnumeric() and int(entry) < len(searches):
                    entry = searches[int(entry)-1]
                else:
                    entry = searches[-1]
                top_level_window.destroy()
            else:
                entry = searches.name
            storedfood = self.get_stored_location(entry, prod)
            new_database_members.append(storedfood)
            print(f"Added {storedfood} to database")
        append_to_database(*new_database_members)
            
    def get_stored_location(self, entry: str, prod: list[str]) -> None:
        while True:
            # why are we checking product = prod here?
            placement_window = PlacementWindow(product = prod)
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
                pcall(Popup("Please enter a number!", master=self))

        placement_window.destroy()
        tmp = get_foods_cached()[entry]
        stored_location = entrydict[entryagain]
        storedfood = food_to_stored_food(tmp, storage_location=stored_location)
        if storedfood.max_time == -1:
            attrs = entrydict.values()
            location = sorted(
                attrs,
                key=(lambda i: getattr(tmp, i)),
                reverse=True
            )[0]
            if not (
                stored_location == "fridge_after_opening"
                and location == "fridge"
            ):
                Popup(message=f"Please put it in the {location}", master = self)
                storedfood = food_to_stored_food(tmp, storage_location=location)
        return storedfood
    
    def on_closing(self) -> None:
        schedule_reminders(get_foods_cached(), 90)
        self.withdraw()

def main():
    app = App()
    app.protocol('WM_DELETE_WINDOW', app.withdraw)
    app.mainloop()

if __name__ == "__main__":
    main()
