# from day_1_input import calibration_document

nums = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

example = ["twolnine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

total = 0

for value in example:
    digits = ""
    current_sum = 0

    for char in value:
        if char.isdigit():
            digits += char

        elif char.isalpha():
            digits += nums.get(char.lower(), "")

    print(digits)

    if len(digits) >= 2:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        calibration_value = first_digit * 10 + last_digit
        current_sum += calibration_value
    elif len(digits) == 1:
        digit = int(digits)
        calibration_value = digit * 10 + digit
        current_sum += calibration_value

    total += current_sum

print(total)
