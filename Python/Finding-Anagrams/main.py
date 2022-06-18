# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) != len(anagram):
        return False

    if sorted(word) != sorted(anagram):
        return False

    return True

print(find_anagram('hello', 'elloh'))
