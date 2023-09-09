# The purpose of the function named "longest_substring" is to find the
# longest sub-string in a string that does not contain any duplicates.

# Importing math is not needed for this code.

# Defining the function
def longest_substring(s):
    longest = ""  # Initialize an empty string to store the longest unique substring.
    current = ""  # Initialize an empty string to store the current unique substring.

    # Iterate over each character in the input string.
    for char in s:
        if char not in current:
            current += char  # Add the character to the current unique substring.
        else:
            if len(current) > len(longest):
                longest = current  # Update the longest substring if needed.
            # Find the index of the repeated character in the current unique substring
            index = current.index(char)
            # Remove all characters before and including the repeated character.
            current = current[index + 1:] + char

    # Check one more time after the loop ends to ensure we capture the longest substring.
    if len(current) > len(longest):
        longest = current

    return longest

# Function to run test cases
def run_tests():
    test_cases = [
        ("bbbbb", "b"),
        ("", ""),
        ("ABBCDDEFGHII", "DEFGHI"),
        ("ABCD", "ABCD"),
        ("dvdf", "vdf"),
    ]
    
    for idx, (input_str, expected_output) in enumerate(test_cases):
        result = longest_substring(input_str)
        if result == expected_output:
            print(f"Test case {idx+1}: PASSED")
        else:
            print(f"Test case {idx+1}: FAILED\nExpected: {expected_output}\nActual: {result}")

if __name__ == "__main__":
    input_string = input("Enter a string:: ")
    length = len(longest_substring(input_string))
    print("The length of the longest non-repeating character substring is", length, " and the substring is: ", longest_substring(input_string))
    run_tests()
