from collections import Counter
import string
import sys

def analyze_file(file_path):
    try:
        # Open and read file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Count lines
        lines = text.splitlines()
        line_count = len(lines)

        # Remove punctuation and lowercase for word analysis
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator).lower()

        # Split into words
        words = clean_text.split()
        word_count = len(words)
        char_count = len(text)

        # Word frequency analysis
        word_freq = Counter(words)
        most_common_words = word_freq.most_common(10)

        # Display results
        print(f"--- Analysis of '{file_path}' ---")
        print(f"Total Lines: {line_count}")
        print(f"Total Words: {word_count}")
        print(f"Total Characters: {char_count}")
        print("\nTop 10 Most Common Words:")
        for word, freq in most_common_words:
            print(f"{word}: {freq}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print("An error occurred:", e)


# Call the function directly with your file path
analyze_file(r"C:\\Users\\RCET\\Desktop\\saiket\\samplefile.txt")
