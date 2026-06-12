# Initialise Questions
Questions = 1
Question_want = 0

while Question_want < Questions:
    Question = input("Question: ")

    Question_want += 1
    Questions += 1

    # if Question is exit code, break out of loop
    if Question == "xxx":
        Question_want += 1

    print(f"{Questions}")
    print(f"{Question_want}")

if Question_want == Questions:
    print(f"You have done {Questions} Questions")
