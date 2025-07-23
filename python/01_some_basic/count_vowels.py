def count_vowels(text):
    """
    Count the occurrences of each vowel (a, e, i, o, u) in the input text.
    Returns a dictionary with vowels as keys and counts as values.
    """
    vowels = "aeiou"
    # Initialize dictionary with zero counts
    counts = {v: 0 for v in vowels}  
    
    # Convert the input text to lowercase and count each vowel
    for char in text.lower():
        if char in vowels:
            counts[char] += 1
    return counts

def print_vowel_summary(counts):
    """
    Print a summary of vowel counts.
    """
    total = sum(counts.values())
    print("Total number of vowels:", total)
    print("Vowel counts:")
    for vowel, count in counts.items():
        if count > 0:
            print(f"{vowel}: {count}")

# input text and call function
if __name__ == "__main__":
    user_input = input("Enter a string: ").strip()

    # Basic input validation: check for empty string
    if not user_input:
        print("You entered an empty string. Please enter some text.")
    else:
        counts = count_vowels(user_input)
        print_vowel_summary(counts)
      
