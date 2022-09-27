try:
    hrsinput: float = float(input("Enter Hours:"))
    rate: float = float(hrsinput("Enter Rate:"))
except ValueError:
    print("Error: Input can only accept numbers and decimal points.")
hrs: float = hrsinput if hrsinput <= 40.0 else 40.0
overtime: float = 0.0 if hrsinput <= 40 else hrsinput - 40
del hrsinput
print(hrs * rate + overtime * rate * 1.5)
