def palindrome(word, start_index, end_index = -1):
    if start_index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[start_index] != word[end_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, start_index + 1, end_index - 1)


print(palindrome("abba", 0))