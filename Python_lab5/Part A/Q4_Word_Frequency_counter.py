paragraph = input("Enter a paragraph: ")

# Convert text to lowercase and remove punctuation
cleaned = ""

for ch in paragraph.lower():

    if ch.isalnum() or ch.isspace():
        cleaned += ch
    else:
        cleaned += " "

words = cleaned.split()

if not words:

    print("Please enter a non-empty paragraph.")

else:

    # Count the frequency of each word
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Counts")

    for word, count in frequency.items():
        print(word, ":", count)

    # Display top N words
    try:
        n = int(input("\nEnter N for top N words: "))

        if n < 0:
            print("Enter a positive number.")
            n = 0

    except ValueError:
        print("Invalid number.")
        n = 0

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\nTop", n, "Words")

    for word, count in sorted_words[:n]:
        print(word, ":", count)

    # Find words appearing exactly once
    once = sorted([
        word
        for word, count in frequency.items()
        if count == 1
    ])

    print("\nWords Appearing Exactly Once")
    print(once)

    # Invert the frequency dictionary
    inverted = {}

    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)

    for count in inverted:
        inverted[count].sort()

    print("\nInverted Dictionary")
    print(inverted)

    # Group words according to their length
    length_groups = {}

    for word in frequency:

        length = len(word)

        length_groups.setdefault(length, []).append(word)

    for length in length_groups:
        length_groups[length].sort()

    print("\nWords Grouped by Length")
    print(length_groups)

    # Search for a particular word
    search_word = input("\nEnter a word to search: ").lower()

    cleaned_search = ""

    for ch in search_word:

        if ch.isalnum():
            cleaned_search += ch

    if cleaned_search in frequency:

        print(cleaned_search, "appears",
              frequency[cleaned_search], "time(s).")

    else:
        print("Word not found.")