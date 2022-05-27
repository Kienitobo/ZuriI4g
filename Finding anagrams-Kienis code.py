# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word,anagram):
    # [assignment] Add your code here
    sorted_first_word=sorted(word)
    sorted_second_word=sorted(anagram)

    if len(word)==len(anagram):
        if sorted_first_word==sorted_second_word:
            return True
        else:
            return False


print(find_anagram("rest","bale"))
    