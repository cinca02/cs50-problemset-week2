numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return (is_valid_length(s) and
            starts_with_two_letters(s) and
            is_valid_number_format(s) and
            no_punctuation_or_space(s))

# Check if between 2 and 6 characters
def is_valid_length(s):
    if  2 <= len(s) <= 6:
        return(True)
    return(False)

# Checks if starts with 2 letters
def starts_with_two_letters(s):
    if s[:2].isalpha():
        return(True)
    return(False)

# Checks if it's a valid number format
def is_valid_number_format(s):
    if s.isalpha(): # No numbers at all
        return(False)
    
    # If plate ends with a number check if it starts with a 0
    if s[-1].isdigit():
        # Check that number doesn't start with a 0
        # Find where the number starts
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit():
                if s[i] == "0" and i == len(s)-1:
                    return False
                break
    return True
        
# Checks no periods, spaces or punctuation
def no_punctuation_or_space(s):
    for char in s:
        if char.isalnum():
            return(True)
        return(False)

main()