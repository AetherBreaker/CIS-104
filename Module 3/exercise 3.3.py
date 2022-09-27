score = float(input("Enter Score:"))
if not (0.0 <= score <= 1.0):
    raise (ValueError("Value must not be less than 0 or greater than 1"))
rubric = {
    "A": lambda input: input >= 0.9,
    "B": lambda input: input >= 0.8,
    "C": lambda input: input >= 0.7,
    "D": lambda input: input >= 0.6,
    "F": lambda input: input < 0.6,
}
for grade, scorecheck in rubric.items():
    if scorecheck(score):
        print(grade)
        break
if False:
    pass
elif True:
    pass
