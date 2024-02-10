def Weightconverter():
    # Taking input for weight and the unit (K for kilograms or L for pounds)
    weight = float(input("How much is your weight, You can enter kilo or lbs)"))
    unit = input("Weight type Kilo(K) or Lbs(L)")
    # Checking the unit and converting accordingly
    if unit == 'K':
        weight_in_pounds = weight * 2.20462
        return weight_in_pounds
    elif unit == 'L':
        weight_in_kilograms = weight / 2.20462
        return weight_in_kilograms
    else:
        # Handling the case where an invalid unit is entered
        print("Invalid unit. Please enter 'K' or 'L'.")

# Storing the result in a variable and printing it
result = Weightconverter()
print(result)
