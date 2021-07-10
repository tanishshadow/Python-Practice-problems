# Python – Least Frequent Character in String
#finding the least frequent character from a string


def least(string)->str:
    "Returns the least frequent character from a string"
    min_freq = []  # list containing the counts of all characters along with the indexes
    for ind, ite in enumerate(string.strip().lower()):
        count = string.count(ite)
        min_freq.append([ite, count])

    freq = min(min_freq, key=lambda x: x[1]) #since the count is in 2 nd index
    return freq[0] # we only want the character not the index !!!!


print(least("Bubblesorttsorl"))
