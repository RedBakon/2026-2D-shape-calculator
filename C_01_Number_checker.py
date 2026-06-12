def float_check(question):
    """Checks users enter an float between two values"""

    error = f"Oops - please enter an float higher than 0"
    while True:

        try:
            # Change the response to an float and check that it's more than zero
            response = float(input(question))

            if response >= 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)
