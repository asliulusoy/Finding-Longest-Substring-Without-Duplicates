'''
The purpose of the function named "longestSubstring" is to find the
longest sub-string in a string that does not contain any duplicate. 
'''
import math

#defining the function
def longest_substring(str):
           
    test_string="" #creating an empty string
    max_length = -1 #creating a integer to hold the values we gathered
     
    #finding the lenght of the input string, if it is 0 or 1, then the function will print an error message
    if (len(str) == 0):
        return 0
    elif(len(str) == 1):
        return 1
    for i in list(str):
        temp = "".join(i)
        if (temp in test_string):
            test_string = test_string[test_string.index(temp) + 1:]
        test_string = test_string + "".join(i)
        max_length = max(len(test_string), max_length)
    return test_string
 
def run_tests():
    test_cases = [
        ("bbbbb", "b"),
        #("", ""),
        ("abcdefg", "abcdefg"),
        ("aab", "ab"),
        ("dvdf", "vdf"),
    ]
    
    for idx, (input_str, expected_output) in enumerate(test_cases):
        result = longest_substring(input_str)
        if result == expected_output:
            print(f"Test case {idx+1}: PASSED")
        else:
            print(f"Test case {idx+1}: FAILED\nExpected: {expected_output}\nActual: {result}")


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    length = len(longest_substring(input_string))
    print("The length of the longest non-repeating character substring is",length, " and the substring is: ", longest_substring(input_string))
    run_tests()