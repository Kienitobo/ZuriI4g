# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from distutils import text_file
from fileinput import filename
from pydoc import text
import string


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as file:
     data=file.read()
    return data
print(read_file_content(r'C:\Users\Kieni\Documents\Zuri tasks\Reading-Text-Files\Reading-Text-Files\story.txt'))

def count_words():
    text = read_file_content(r'C:\Users\Kieni\Documents\Zuri tasks\Reading-Text-Files\Reading-Text-Files\story.txt')
    # [assignment] Add your code here

    for char in '-.,?:\n':
     text=text.replace(char,'')
    text=text.lower()
    text=text.split()
    sentence_dictionary={}
    for item in text:
        if item in sentence_dictionary:
           sentence_dictionary[item] =sentence_dictionary[item]+1
        else:
          sentence_dictionary[item]=1

    return sentence_dictionary

print((count_words()))
