def get_num_words(filepath):
    with open(filepath) as f:
        filecontents = f.read()
    return count_words(filecontents)
    

def count_words(filecontents):
    return len(filecontents.split())

def get_letter_count(filepath):
    newdict={}
    with open(filepath) as f:
        filecontents = f.read()

    for word in filecontents.lower():
        for letter in word:
            if letter.isalpha():
                if letter in newdict:
                    newdict[letter] += 1
                else:
                    newdict[letter] = 1
    newdict = sortedList(newdict)
    return newdict

def sort_on(items):
    return items["num"]

def sortedList(newDict):
    finalList = []
    for key in newDict:
        finalList.append({"char": key, "num": newDict[key]})
    finalList.sort(reverse=True, key=sort_on)
    return finalList
