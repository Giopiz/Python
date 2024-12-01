weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == 'K' :
    value = weight / 0.45
    print("Weight in Lbs: " + str(value))

else:
    value = weight * 0.45
    print("Weight in Kilos: " + str(value))


