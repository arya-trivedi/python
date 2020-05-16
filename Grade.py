# A simple marks grading app

# continuous while loop, till zero is entered

while True:
    try: # to handle the exception of wrong input
        # user input
        marks = int(input("How many marks you scored? "))

        if(marks < 0 or marks > 100):
            print("Please enter an integer between 1 and 100")
        elif (marks >= 90): # if marks more than 90
            print("Congratulations, you got A grade")
        elif(marks >79):  # if marks more than 79
            print("You got B grade")
        elif(marks >69):  # if marks more than 69
            print("You got C grade")
        elif(marks >59):  # if marks more than 50
            print("You got D grade")
        elif(marks == 0):
            print("Goodbye")
            break
        else:
            print("Oh ho, Better try in next exam")

    except ValueError: # show input error
        print("The input value has to be an integer, please try again!")