def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    print("Height = ", height)
    print("Weight = ", weight)

    bmi = weight / (height*height)
    print("BMI = ", round(bmi,2))

    if bmi < 18.5:
        print("Under weight")
    elif bmi > 25.0:
        print("Over weight")
    else:
        print("Normal weight")

calculate_bmi(1.73, 37)
