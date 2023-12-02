from day_1_input import calibration_document

# example = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

total = 0

for value in calibration_document:
    digits = ""
    current_sum = 0

    for char in value:
        if char.isdigit():
            digits += char

    if len(digits) >= 2:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        calibration_value = first_digit * 10 + last_digit
        current_sum += calibration_value
    else:
        digit = int(digits)
        calibration_value = digit * 10 + digit
        current_sum += calibration_value

    total += current_sum

print(total)
