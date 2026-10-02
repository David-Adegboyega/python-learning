while True:
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))
        bmi = weight / (height ** 2)
        break
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Height cannot be zero.")

if bmi < 18.5:
    print(f'BMI: {bmi:.2f} category = Underweight')
elif bmi <= 24.9:
    print(f'BMI: {bmi:.2f} category = Healthy Weight')
elif bmi <= 29.9:
    print(f'BMI: {bmi:.2f} category = Over Weight')
else:
    print(f'BMI: {bmi:.2f} category = Obese')