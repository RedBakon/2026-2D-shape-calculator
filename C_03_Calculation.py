def string_check(question, valid_ans_list, num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# question checker
def float_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # users are able to use decimal points.
        try:
            response = float(to_check)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)

# Calculations start here
shape = ("square", "triangle", "rectangle", "circle")
A_or_P = ("area", "perimeter", "xxx")


# Ask for what shape
shape_wanted = string_check("What shape do you want to calculate? ", shape)

# Ask for area or perimeter
area_or_perimeter = string_check("Do you want to calculate area or perimeter? ", A_or_P)

# Asking for dimensions

# asking for the lengths if it's a square
if shape_wanted == "square":
    length = float_check("What is the length of one side of this square? ")

# asking for the base and height if it's area and the sides if it's a perimeter
if shape_wanted == "triangle":
    if area_or_perimeter == "area":
        base = float_check("What is the base of this triangle? ")
        height = float_check("What is the height of this triangle? ")
    if area_or_perimeter == "perimeter":
        triangle_side1 = float_check("What is the length of the first side? ")
        triangle_side2 = float_check("What is the length of the second side? ")
        triangle_side3 = float_check("What is the length of the third side? ")


# asks for the length and width if it's a rectangle
if shape_wanted == "rectangle":
        length = float_check("What is the length of this rectangle? ")
        width = float_check("What is the width of this rectangle? ")

# ask for the radius if it's a circle
if shape_wanted == "circle":
    radius = float_check("What is the radius of the circle? ")

# Calculations for shape

# calculations for a square
if shape_wanted == "square":
    if area_or_perimeter == "area":
        answer = length * length
    if area_or_perimeter == "perimeter":
        answer = 4 * length

# calculations for a triangle
if shape_wanted == "triangle":
    if area_or_perimeter == "area":
        answer = base * height * 0.5
    if area_or_perimeter == "perimeter":
        answer = triangle_side1 + triangle_side2 + triangle_side3

# calculations for a rectangle
if shape_wanted == "rectangle":
    if area_or_perimeter == "area":
        answer = length * width
    if area_or_perimeter == "perimeter":
        answer = 2 * (length + width)

# calculations for a circle
if shape_wanted == "circle":
    if area_or_perimeter == "area":
        answer = 3.14 * (radius * radius)
    if area_or_perimeter == "perimeter":
        answer = 2 * 3.14 * radius

print(f"The answer is {answer:.2f}")
