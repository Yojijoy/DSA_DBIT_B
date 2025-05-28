def count_char_frequencies(text):
frequencies = {}
    for char in text:
    if char != ' ':
    freq[char] = freq.get(char, 0) + 1
    return freq
# Example usage
result = count_char_frequencies("data structures and algorithms")
print("Character frequencies:", result)