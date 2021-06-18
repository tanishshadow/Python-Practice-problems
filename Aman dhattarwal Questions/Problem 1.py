"""A simple python program to return the words from a file whose length is less than 4 (trailing whitespaces and delimiter case included)"""
def DISPLAYWORDS(file):
    "Returns the words from a file whose length is less than 4 (removes extra whitespaces)"
    f = open(file, 'r')
    con = f.read() 
    con2 = con.split() # making a list by splitting the string with spaces and removes trailing whitespaces
    res = ' '.join(con2) # joining the list elements converted in one string with a space between them

    l = res.split()

    for  item in l:
        if item.endswith('\\n'): #checking if any elments of the list is combined with a delimiter, which usually happens for eg:- 'mom\n'
            item.replace('\\n', '')
        if len(item) < 4:
            print(item)
    f.close() #closing a file is important


DISPLAYWORDS(r'aman dhattarwal\empty.txt')
