def is_palindrom(text):
    """
    Check if a string is a palindrome (reads the same forwards and backwards).
    """
    text_clean = text.replace(" ", "").lower()
    return text_clean == text_clean[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrom(user_input):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")
