import string

def count_words(text):
    """
    Count total number of words in the given text,
    ignoring punctuation.
    """

    # Remove punctuation (like .,!? etc.) to count only words
    translator = str.maketrans('', '', string.punctuation)

    # Use translate to remove punctuation
    clean_text = text.translate(translator)
    return len(clean_text.split())


# input text and call function
if __name__ == "__main__":
    user_input = input("Enter a string: ").strip()

    # Basic input validation: check for empty string
    if not user_input:
        print("You entered an empty string. Please enter some text.")
    else:
        print("Total number of words: ", count_words(user_input))
