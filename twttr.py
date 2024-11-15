output = ""
vowels = "aeiouAEIOU"
# User Input
text = input("Input: ")

# Loop through each letter in string, add to output if not a vowel
for letter in text:
    if letter in vowels:
        continue # Skip vowels
    output += letter

# Print finished outcome
print(f"Output: {output}")