"""
The walrus operation (:=) allows in place assignment inside conditionals
and allows in place assignment to the right of the equals sign
during a regular assignment operation.
Generally walrus assignment requires the operation be enclosed inside
parenthesis eg: (score := 10).
A walrus assignment operation enclosed in parenthesis will always return
its value so the interpreter will treat:
0.0 <= (score := 0.5) <= 1.0
identically to:
0.0 <= (0.5) <= 1.0
both of these examples will return the same result, the only difference is that
the walrus assignment example will have also simultaneously assigned the value
0.5 to the variable "score".
"""
if not (0.0 <= (score := float(input("Enter Score:"))) <= 1.0):
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