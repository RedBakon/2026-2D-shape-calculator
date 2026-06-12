def float_check(question, exit_code):
    """Checks users enter a  float between two values"""

    error = f"Oops - please enter an float higher than 0 or enter 'xxx' to exit"
    error1 = f"Please enter a number or enter 'xxx' to exit"


    rechange = float

    while True:

        # Change the response to a float and check that it's more than zero
        response = input(question)

        # checking for exit code
        if response == exit_code:
            return response

        try:

            response = rechange(response)

            # checks for numbers
            if response >= 0:
                return response
            if response <= 0:
                print(error)
            else:
                print(error1)

        except ValueError:
            print(error)

Test = float_check("enter xxx! ", "xxx")

print("Right!")