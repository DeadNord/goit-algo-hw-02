from collections import deque


def is_palindrome(input_string):
    cleaned_string = input_string.lower().replace(" ", "")

    char_queue = deque(cleaned_string)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            print(f"`{input_string}` is not a palindrome.")
            return False

    print(f"`{input_string}` is a palindrome.")
    return True


while True:
    user_input = input("Enter your string: ")
    # user_input = "A man a plan a canal Panama"
    result = is_palindrome(user_input)
    print(result)
