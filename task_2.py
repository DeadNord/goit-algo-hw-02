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
    user_input = input("Enter your string(or exit for stop the program): ")

    # example: "A man a plan a canal Panama"
    if user_input == "exit":
        print("Goodbye! You exited from program.")
        break
    result = is_palindrome(user_input)
    print(result)
