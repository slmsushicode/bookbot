def num_words(book):
    words = book.split()
    num = len(words)
    return num
def word_count(book):
    lower = book.lower()
    chars = {}
    for char in lower:
        chars[char] = chars.get(char, 0) + 1
    return chars

def sort_on(items):
    return items["num"]

def structure(dictionary):
    lists = []

    for key, value in dictionary.items():
        dicts = {

            "char":key, "num":value
        
        }
        
        lists.append(dicts)
    lists.sort(reverse=True,key=sort_on)
    return lists
