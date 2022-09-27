input: float = float(input("Enter Hours:"))
hrs: float = input if input <= 40.0 else 40.0
overtime: float = 0.0 if input <= 40 else input - 40
del input
rate: float = float(input("Enter Rate:"))
print(hrs * rate + overtime * rate * 1.5)
