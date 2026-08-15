    # BMI calculator
def main():
            # taking input from user
    weight = float(input("Enter your weight in kg :"))
    height = float(input("Enter your height in meters :"))

            # validating the input
    if weight and height <= 0:
        print("please enter valid weight and height")
    else:
        BMI = weight/height**2
        print(" Your BMI is :", BMI)
        
           # Calling the function
if __name__ == "__main__":
    main()
    