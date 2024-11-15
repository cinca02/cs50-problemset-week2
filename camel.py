import sys

snake = ""

# Checking if command line input
if len(sys.argv) > 1:
    camel = sys.argv[1]
# If not, prompts user for input
else:
    camel = input("camelCase: ")

# Loop through letters, changing uppercase to _ + lowercase
for letter in camel:
    
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter
    
# Output snake case result
print(f"snake_case: {snake}")