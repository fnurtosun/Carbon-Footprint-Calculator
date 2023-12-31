import matplotlib.pyplot as plt

name = input("Enter your name: ")
total_footprint = 0
heating_score = 0
food_score = 0
stuff_score = 0
transportation_score = 0

print("Hello, " + name.upper() + "!")
input("Now, we will calculate your annual carbon emissions and determine what you can do to offset them. Press Enter to continue.")

while True:
    while True:
        question0 = input("Do you have an idea about your carbon footprint (yes/no)? ").lower()
        if question0 == "yes":
            print("Alright, let's calculate your carbon footprint.")
            break
        elif question0 == "no":
            print("The carbon footprint is a measure of the environmental impact of human activities.")
            break
        else:
            print("Please type yes or no")

    input("Press Enter to continue")

    score = 0

    while True:
        answer = input("What type of fuel do you use to heat your home? a) wood b) coal c) natural gas d) electricity? ")
        answer = answer.lower()
        if answer in ["wood", "a"]:
            try:
                wood_kg = int(input("How many kg of wood do you consume annually? "))
                heating_score += wood_kg * 1.8
                print(f"Your carbon footprint for heating with wood: {wood_kg * 1.8} kg.")
                break
            except ValueError:
                print("Please enter a valid number for wood consumption.")
        elif answer in ["coal", "b"]:
            try:
                coal_kg = int(input("How many kg of coal do you consume annually? "))
                heating_score += coal_kg * 2.5
                print(f"Your carbon footprint for heating with coal: {coal_kg * 2.5} kg.")
                break
            except ValueError:
                print("Please enter a valid number for coal consumption.")
        elif answer in ["natural gas", "c"]:
            try:
                natural_gas_kg = int(input("How many kg of natural gas do you consume annually? "))
                heating_score += natural_gas_kg * 3.1
                print(f"Your carbon footprint for heating with natural gas: {natural_gas_kg * 3.1} kg.")
                break
            except ValueError:
                print("Please enter a valid number for natural gas consumption.")
        elif answer in ["electricity", "d"]:
            try:
                electricity_kg = int(input("How much kw of electricity do you consume annually? "))
                heating_score += electricity_kg * 0.8
                print(f"Your carbon footprint for heating with electricity: {electricity_kg * 0.8} kg.")
                break
            except ValueError:
                print("Please enter a valid number for electricity consumption.")
        else:
            print("Please choose an option.")
            continue

    while True:
        answer = input("How would you describe your diet? A) Vegan B) Vegetarian C) Heavy Meat Eater ")
        answer = answer.lower()
        if answer in ["vegan", "a"]:
            try:
                vegan_kg = int(input("How much money do you spend on food annually?($) "))
                food_score += vegan_kg * 1.1
                print(f"Your carbon footprint for meat consumption: {vegan_kg * 1.1} kg.")
                break
            except ValueError:
                print("Please enter a valid number for food expenditure.")
        elif answer in ["vegetarian", "b"]:
            try:
                vegetarian_kg = int(input("How much money do you spend on food annually? "))
                food_score += vegetarian_kg * 1.3
                print(f"Your carbon footprint for meat consumption: {vegetarian_kg * 1.3} kg.")
                break
            except ValueError:
                print("Please enter a valid number for food expenditure.")
        elif answer in ["heavy meat eater", "c"]:
            try:
                heavy_meat_eater_kg = int(input("How much money do you spend on food annually? "))
                food_score += heavy_meat_eater_kg * 1.8
                print(f"Your carbon footprint for meat consumption: {heavy_meat_eater_kg * 1.8} kg.")
                break
            except ValueError:
                print("Please enter a valid number for food expenditure.")
        else:
            print("Please choose an option.")
            continue

    answer = int(input("How much do you spend on furniture?($) "))
    try:
        stuff_score += answer * 0.61
        print("Your carbon footprint for furniture: ", answer * 0.61)
    except ValueError:
        print("Please enter a valid number for furniture expenditure.")

    answer = int(input("How much do you spend on clothing?($) "))
    try:
        stuff_score += answer * 0.42
        print("Your carbon footprint for clothing: ", answer * 0.42)
    except ValueError:
        print("Please enter a valid number for clothing expenditure.")

    answer = int(input("How much do you spend on technological devices?($) "))
    try:
        stuff_score += answer * 0.67
        print("Your carbon footprint for technological devices: ", answer * 0.67)
    except ValueError:
        print("Please enter a valid number for technological device expenditure.")

    answer1 = input("What is the fuel type of your vehicle? a) LPG b) gasoline c) diesel ").lower()
    if answer1 in ["a", "lpg"]:
        try:
            lpg_lt = int(input("How many liters do you use annually? "))
            transportation_score += lpg_lt * 2.3
            print(f"Your carbon footprint for transportation with LPG: {lpg_lt * 2.3}")
        except ValueError:
            print("Please enter a valid number for LPG consumption.")
            continue
    elif answer1 in ["b", "gasoline"]:
        try:
            gasoline_lt = int(input("How many liters do you use annually? "))
            transportation_score += gasoline_lt * 2.7
            print(f"Your carbon footprint for transportation with gasoline: {gasoline_lt * 2.7}")
        except ValueError:
            print("Please enter a valid number for gasoline consumption.")
            continue
    elif answer1 in ["c", "diesel"]:
        try:
            diesel_lt = int(input("How many liters do you use annually? "))
            transportation_score += diesel_lt * 3.3
            print(f"Your carbon footprint for transportation with diesel: {diesel_lt * 3.3}")
        except ValueError:
            print("Please enter a valid number for diesel consumption.")
            continue
    else:
        print("Please choose an option!")
        continue

    print("Total carbon footprint:", heating_score + food_score + stuff_score + transportation_score, "kg")
    total_footprint += heating_score + food_score + stuff_score + transportation_score

    continue_calculation = input("Would you like to calculate the carbon footprint of another person? (yes/no): ").lower()
    if continue_calculation != "yes":
        break

print("Total carbon footprint of all individuals:", total_footprint, "kg")

offset = int(total_footprint * 1.3 / 1000)
print("You can pay your debt to nature by planting", offset, "trees.")
input("Press enter to see the link of donation")
print("https://www.tema.org.tr/bagislar")

labels = ["Heating", "Food", "Transportation", "Stuff"]
values = [heating_score, food_score, transportation_score, stuff_score]

plt.pie(values, labels=labels, autopct='%3.1f%%', startangle=140)
plt.title('Carbon Footprint by Category')
plt.show()

cevap = input("Would you like to see those who contributed? (Yes No): ")

proje_yapanlar = [
    {"isim": "Faruk Emir Selvi", "numara": "1317200031"},
    {"isim": "Ecem Alnıak", "numara": "1317220009"},
    {"isim": "Aysun Selin Uçar", "numara": "1317210014"},
    {"isim": "Fatma Nur Tosun", "numara": "1317220036"},
]

if cevap.lower() == "yes":
    for kisi in proje_yapanlar:
        print(f"{kisi['isim']} - {kisi['numara']}")
else:
    print("Then goodbye.")
