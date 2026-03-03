# Input for 5 cities 
# x = input("Please select the weather for one of the following cities: London, Edinburgh, Cardiff, Belfast, Birmingham: ")

# if input not in ["London", "Edinburgh", "Cardiff", "Belfast", "Birmingham"]:
#     print("Invalid input. Please select a city from the list.")
# else: 
#     print(f"You have selected: {x}")
from weatherapi import CITIES

    


# Import current date and time - 
while True:
    print("Please select the weather for one of the following cities: London, Edinburgh, Cardiff, Belfast, Birmingham: ")
    city = input()
    try:
        city = str(city)
    except:
        print('Please use letters only')
        continue
    if city not in ["London", "Edinburgh", "Cardiff", "Belfast", "Birmingham"]:
        print('Please select a city from the list.')
        continue
    break

