def find_and_replace(filename, find_word, replace_word):
    try:
        # Read from file
        with open(filename, "r") as file:
            content = file.read()

        # Replace text
        new_content = content.replace(find_word, replace_word)

        # Write back to the same file
        with open(filename, "w") as file:
            file.write(new_content)

        print("✔ File updated successfully!")

    except FileNotFoundError:
        print("Error: File not found! Check the filename.")
    except PermissionError:
        print("Error: You don't have permission to modify this file.")
    except Exception as e:
        print(f"⚠ Unexpected error occurred: {e}")


# ------------ MAIN PROGRAM ------------

print(" Basic File Handling: Find & Replace Program")

filename = input("Enter the filename (example: data.txt): ")

find_word = input("Enter the word you want to find: ")
replace_word = input("Enter the new word: ")

if find_word.strip() == "":
    print("Find word cannot be empty!")
else:
    find_and_replace(filename, find_word, replace_word)
