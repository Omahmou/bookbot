def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, 'r') as f:
        file_contents = f.read()

    # Count words and print the result
    word_count = count_words(file_contents)
    print(f"The number of words in Frankenstein is: {word_count}")

    # Filter text to keep only alphabet characters and lowercase it
    filtered_text = filter_alphabetical(file_contents.lower())

    # Count characters and print the result
    char_count = count_characters(filtered_text)
    print("Character count (filtered):", char_count)
    
    # Convert dictionary to list for sorting
    char_count_list = [{"char": char, "count": count} for char, count in char_count.items()]
    
    # Sort the list by the count
    char_count_list.sort(reverse=True, key=sort_on)
    
    # Printing sorted character count
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for item in char_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def filter_alphabetical(text):
    filtered_text = []
    for char in text:
        if char.isalpha() or char == ' ':  # Include spaces to count words correctly
            filtered_text.append(char)
    return ''.join(filtered_text)


def count_characters(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Check if the character is alphabetical
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(item):
    return item["count"]


if __name__ == "__main__":
    main()
