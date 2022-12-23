# Get the string inputs from the user
strings = []
for i in range(5):
    strings.append(input(f"Enter string {i+1}: "))

# Sort the strings by length in ascending order
strings.sort(key=len)

# Print the sorted strings
for s in strings:
    if len(s) <= 3:
        print(s.upper())
    else:
        print(s.capitalize())