import numpy as np
from collections import Counter

def avr_word(words):
    avg_len = average_word_length(words)
    character_avg = []
    character_temp = []
    for i in range(avg_len):
        for word in words:
            if len(word)-1 >= i:
                character_temp.append(word[i])
        character_avg.append(most_common(character_temp))
        character_temp = []
    return ''.join(character_avg)        
        
def clean_up(word, punctuation="!\"',;:.-?)([]<>*#\n\\"):
    return word.lower().strip(punctuation)

def average_word_length(text):
    cleaned_words = [clean_up(w) for w in (w for l in text for w in l.split())]
    return round(sum(map(len, cleaned_words))/len(cleaned_words))

def most_common(lst):
    return max(set(lst), key=lst.count)

print(avr_word(["Joh", "Bol", "Biht"]))