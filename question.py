'''
The purpose of the function named "longestSubstring" is to find the
longest sub-string in a string that does not contain any duplicate. 
'''
import math

#defining the function
def longest_substring(str):
           
    test_string="" #an empty character string named test_string is created. we'll use this string to store temporary substrings during the process.
     
    #finding the lenght of the input string;
    if (len(str) == 0):
        return 0 #if the length of the string is 0, the function returns 0, indicating an empty string.
    elif(len(str) == 1):
        return 1 #if the length of the string is 1, the function returns 1, indicating a single character in the string.
    
    '''
     If the special cases above are passed, a loop begins. This loop aims to traverse the characters of the str string one by one to find the longest unique substring.

    While iterating over each character, a temporary substring called temp containing the character i is created.
    '''
    for i in list(str):
        temp = "".join(i)
        if (temp in test_string):
            test_string = test_string[test_string.index(temp) + 1:] #now, it's checked whether the temp substring has been seen before in the test_string.
            #if it's been seen, the test_string is updated starting from the position immediately after the last occurrence of the temp substring. 
            #this helps us remove previous unique substrings and create a new unique substring.
        test_string = test_string + "".join(i) #next, the temp substring is added to the test_string, thus updating the test_string to include a new unique substring.
    return test_string
 
def run_tests():
    test_cases = [
        ("bbbbb", "b"),
        #("", ""),
        ("ABBCDDEFGHII", "DEFGHI"),
        #("AABBCCD", "AB" or "BC" or "CD")
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
    input_string = input("Enter a string: ")
    length = len(longest_substring(input_string))
    print("The length of the longest non-repeating character substring is",length, " and the substring is: ", longest_substring(input_string))
    run_tests()