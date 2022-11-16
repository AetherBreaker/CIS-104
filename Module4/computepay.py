def computepay(hours: float, rate: float) -> float:
    hrs: float = hours if hours <= 40.0 else 40.0
    overtime: float = 0.0 if hours <= 40 else hours - 40
    return hrs * rate + overtime * rate * 1.5


inp: float = float(input("Enter Hours:"))
rate: float = float(input("Enter Rate:"))
p = computepay(inp, rate)
print("Pay", p)
