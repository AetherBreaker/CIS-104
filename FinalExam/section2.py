from typing import List, Tuple

# This list is used for testing the code
# testlist = [
#     "1.2",
#     "3.4",
#     "5",
#     "7.8",
#     "9.10",
#     "11",
#     "135794",
#     "15556.1623428",
#     "23452317.18",
#     "19.2062346",
#     "20.21",
#     "22.23",
#     "24.25",
#     "26.27",
# ]

"""I decided to expand the scope of this a little bit to try and remove floating point inaccuracy by trying something
that I recently learned about, apparently many embedded system processors can't actually perform floating point division
so they usually just handle decimals by converting them all to integers with a fixed number of digits after the decimal."""
if __name__ == "__main__":
    # This list will hold tuples with the integer part and decimal part of each number
    inputlist = []
    # Keep track of the maximum number of digits in the integer part of the numbers
    max_decimal_accuracy = 0

    # Keep asking for input until the user types "q", "quit", or "exit"
    while (consoleinput := input("Enter a number: ")) not in ("q", "quit", "exit"):
        try:
            float(consoleinput)
        except ValueError:
            print(
                f"ValueError: Could not convert '{consoleinput}' to a valid numbern"
                f"Please only input numbers, periods, or thousands separator underscores.\n"
                f'Or type: "q", "quit", or "exit" to finish accepting input.'
            )

        # Split the input into integer and decimal parts
        consoleinput = consoleinput.split(".")

        # Calculate the number of digits in the decimal parts
        decimal_accuracy = len(consoleinput[1]) if len(consoleinput) > 1 else 1

        # Update the maximum number of digits in the decimal parts
        if decimal_accuracy > max_decimal_accuracy:
            max_decimal_accuracy = decimal_accuracy

        # Add the integer and decimal parts to the inputlist
        inputlist.append(
            (*consoleinput,) if len(consoleinput) > 1 else (consoleinput[0], "0")
        )

    # Pad the decimal parts with zeros to make all positions line up
    result = []
    for int_part, decimal_part in inputlist:
        result.append(
            (
                int(int_part),
                int(f"{decimal_part:0<{max_decimal_accuracy}}"),
            )
        )

    # Calculate the sum of the integer and decimal parts individually, then combine
    sumof = float(
        f"{sum(intpart for intpart, decpart in result)}.{sum(decpart for intpart, decpart in result)}"
    )

    print(
        "\n".join(
            (
                f"Sum of inputs = {sumof}",
                f"Number of inputs = {len(inputlist)}",
                f"Average of inputs = {sumof / len(inputlist)}",
            )
        )
    )
