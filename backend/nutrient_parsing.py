from backend.imageapi import get_image_info

data = get_image_info()
def parse():
    ls = []
    carb_sum = 0
    sugar_sum = 0
    sodium_sum = 0
    protein_sum = 0
    fat_sum = 0
    cal_sum = 0
    for food_item in data['nutritional_info_per_item']:
        intake = food_item['nutritional_info']['dailyIntakeReference']
        if len(data.get('foodName')) == 1:
            ls.append((f"Food Item {food_item['food_item_position']}:"))
            
            ls.append(("Carbs percentage:", intake['CHOCDF']['percent']))

            ls.append(("Sugars percentage:", intake['SUGAR']['percent']))

            ls.append(("Sodium percentage:", intake['NA']['percent']))

            ls.append(("Protein percentage:", intake['PROCNT']['percent']))

            ls.append(("Fat percentage:", intake['FAT']['percent']))

            ls.append(("Calories:", food_item['nutritional_info']['calories']))

        elif len(data.get('foodName')) > 1:
            carb = (((intake['CHOCDF']['percent']) * (food_item['nutritional_info']['calories']) * (0.01))) #Sets variable carb to its percentage value multiplied by the calories
            carb_sum += carb

            sugar = (((intake['SUGAR']['percent']) * (food_item['nutritional_info']['calories']) * (0.01))) #Sets variable sugar to its percentage value multiplied by the calories
            sugar_sum += sugar

            sodium = (((intake['NA']['percent']) * (food_item['nutritional_info']['calories']) * (0.01))) #Sets variable sodium to its percentage value multiplied by the calories
            sodium_sum += sodium

            protein = (((intake['PROCNT']['percent']) * (food_item['nutritional_info']['calories']) * (0.01))) #Sets variable protein to its percentage value multiplied by the calories
            protein_sum += protein

            fat = (((intake['FAT']['percent']) * (food_item['nutritional_info']['calories']) * (0.01))) #Sets variable fat to its percentage value multiplied by the calories
            fat_sum += fat

            calories = (food_item['nutritional_info']['calories'])
            cal_sum += calories

    ls.append(("carb", carb_sum/cal_sum)) #Total number of carbs divided by total number of calories
    ls.append(("sugar", sugar_sum/cal_sum)) #Total number of sugar divided by total number of calories
    ls.append(("sodium", sodium_sum/cal_sum)) #Total number of sodium divided by total number of calories
    ls.append(("protein", protein_sum/cal_sum)) #Total number of protein divided by total number of calories
    ls.append(("fat", fat_sum/cal_sum)) #Total number of fat divided by total number of calories

    return ls



