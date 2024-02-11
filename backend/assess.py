import customtkinter as ctk
ctk.set_appearance_mode('dark')
def assessing(carbs_percent, sugar_percent, sodium_percent, protein_percent, fat_percent):
    window = ctk.CTk()
    window.title("Nutrition Assessment")
    window.geometry("700x350")    
    nutrition_text = ctk.CTkTextbox(window, height=200, width=500)
    nutrition_text.pack(pady=10)
    button_exit = ctk.CTkButton(window, text="Close", command=window.destroy)
    button_exit.pack(pady=10)
    healthy_ranges = {
        'carbs': {'range': (45, 65), 'weight': 0.2},
        'sugar': {'range': (0, 10), 'weight': 0.1},
        'sodium': {'range': (0, 2.3), 'weight': 0.3},  
        'protein': {'range': (10, 35), 'weight': 0.2},
        'fat': {'range': (20, 35), 'weight': 0.2}
    }
    health_index = 100
    nutrient_assessment = {}
    for nutrient, info in healthy_ranges.items():
        lower_bound, upper_bound = info['range']
        weight = info['weight']
        nutrient_percent = locals()[nutrient + '_percent']  
        if lower_bound <= nutrient_percent <= upper_bound:
            nutrient_assessment[nutrient] = 'is a sufficient amount of consumption for it.'
        elif nutrient_percent < lower_bound:
            nutrient_assessment[nutrient] = 'is too low, consider higher consumption of it.'
            health_index -= (lower_bound - nutrient_percent) * weight * 10
        else:
            nutrient_assessment[nutrient] = 'is too high, consider lower consumption of it.'
            health_index -= (nutrient_percent - upper_bound) * weight * 10
    
    nutrition_text.insert("end",'Health Index is:'+str(health_index)+'\n')
    nutrition_text.insert("end", 'Carbohydrate Consumption '+nutrient_assessment['carbs']+'\n')
    nutrition_text.insert("end", 'Sugar Consumption '+nutrient_assessment['sugar']+'\n')
    nutrition_text.insert("end", 'Sodium Consumption '+nutrient_assessment['sodium']+'\n')
    nutrition_text.insert("end", 'Protein Consumption '+nutrient_assessment['protein']+'\n')
    nutrition_text.insert("end", 'Fat Consumption '+nutrient_assessment['fat'])
    window.mainloop()
    return lambda:None
