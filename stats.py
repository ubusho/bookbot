
def get_num_words(text):
    return len(text.split())

def count_characters(text):
    dictionary = {}
    for character in text.lower():
        if character.isalpha():
            if not character in dictionary:
                dictionary[character] = 1
            else:
                dictionary[character] += 1
    return dictionary

def sort_on(dict):
    return dict["num"]
    
def unsorted_list(dictionary):
    character_counts = []
    for item in dictionary:
        character_counts.append({"character":item, "num":dictionary[item]})
    return character_counts