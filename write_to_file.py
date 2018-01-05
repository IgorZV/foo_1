file = open("testfile.txt", "w")

file.writelines(["Hello Word", "This is new text file", "This is another line", "Why? Because we can"])

file.close()

def plus (a,b):
    result = a+b
    print(result)

def minus (a,b):
    result = a-b
    print(result)

plus(3,4)
minus(5,2)
