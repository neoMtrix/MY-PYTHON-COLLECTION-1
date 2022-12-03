# Because we know that each key can be present only once, dictionaries are a great tool for counting elements and analyzing frequency. Let's check out a simple example of counting how many times each letter appears in a piece of text.
# DICTIONARIES | Iterating over the Contents of a Dictionary

def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

# In this code, we're first initializing an empty dictionary, then going through each letter in the given string. For each letter, we check if it's not already in the dictionary. And in that case, we initialize an entry in the dictionary with a value of zero. Finally, we increment the count for that letter in the dictionary. To sum up, we've created a dictionary where the keys are each of the letters present in the string and the values are how many times each letter is present. 