import pandas

# lists to hold ticket details
all_shapes = ["square", "square", "triangle", "rectangle"]
all_area_questions = ["25 x 25", "36.5 x 36.5", "50 x 150", "5.4 x 2.4"]
all_area_answers  = [625.00, 1332.25, 3750.00, 12.96]

area_questions_dict = {
    'Shapes': all_shapes,
    'Area Questions': all_area_questions,
    'Area answers': all_area_answers
}

# create dataframe / table from dictionary
area_questions_frame = pandas.DataFrame(area_questions_dict)

print(area_questions_frame)