#Given a list of integers with duplicate elements in it.
#The task to generate another list, which contains only the duplicate elements. In simple words, the new list should contain the elements which appear more than one.


intial = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

def dupe_gen(lst):
    return list(set([str(i) for i in intial if lst.count(i)>1])) # converting the list to a set to remove all duplicates
 
print(dupe_gen(intial))
