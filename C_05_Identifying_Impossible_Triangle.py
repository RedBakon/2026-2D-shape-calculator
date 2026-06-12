# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"

# Functions go here
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

def instructions():
    print(make_statement("Instructions", "ℹ️"))

    print('''
This is a basic area and perimeter calculator that any user can use.
It's used to calculate area and perimeter of shapes by the measurements that you submit into the calculator

To calculate the perimeter of a square is by using by adding up all the four sides that it has.
And to calculate its area is by multiplying the width and length of the square.

The list of shapes that are available shapes are: Square, Triangle, Circle, Rectangle
    ''')

# Functions go here
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

            # change the response to a float
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

# Main Routine goes here

# Area shapes

# string checks
A_or_P = ("perimeter", "xxx")
shapes = ("triangle", "xxx")
yes_or_no = ("yes", "no")

# Initialise Questions
Questions = 1
Question_want = 0

# Calculation here

# Print Heading
print("✖️➕📐 Area and Perimeter Calculator 📐➕✖️")
print()

shape_picked = "triangle"
area_or_perimeter = "perimeter"

# Loop starts here.
while Question_want < Questions:

    # asking for the base and height if it's area and the sides if it's a perimeter
    if shape_picked == "triangle":
        if area_or_perimeter == "perimeter":
            triangle_side1 = float_check("What is the length of the triangle first side? ", "xxx")
            triangle_side2 = float_check("What is the length of the triangle second side? ", "xxx")
            triangle_side3 = float_check("What is the length of the triangle third side? ", "xxx")


    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    # if the user put in a impossible triangle
    elif (triangle_side1 + triangle_side2) <= triangle_side3 or (triangle_side2 + triangle_side3) <= triangle_side1 or (triangle_side1 + triangle_side3) <= triangle_side2:
        print("This is a impossible triangle, please try again")
        print()
        continue
    else:
        # calculations for a triangle
        if shape_picked == "triangle":
            if area_or_perimeter == "perimeter":
                answer = triangle_side1 + triangle_side2 + triangle_side3


    # if the user picked exit code skip.
    if Question_want == Questions:
        pass
    else:
        print(f"The answer is {answer:.2f}")
        print()
        # remove (s)
        if Questions == 1:
            print(f"That's {Questions} Question!")
        else:
            print(f"That's {Questions} Questions!")

    if Question_want == Questions:
        pass
    else:
        Question_want += 1
        Questions += 1

    if Question_want == Questions:
        print(f"You did {Questions - 1} Questions")

# End of loop





