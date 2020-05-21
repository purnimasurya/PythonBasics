file = input("Input the Filename: ")
index = file.split('.')
for i in index:
    if(i == "txt"):
        print("'The extension of the file is : 'text''" )
    elif(i == "csv"):
        print("'The extension of the file is : 'comma separated values''" )
    elif(i == "ppt"):
        print("'The extension of the file is : 'powerpoint presentation''" )
    elif(i == "py"):
        print("'The extension of the file is : 'python''" )
    elif(i == "java"):
        print("'The extension of the file is : 'java''" )
    elif(i == "c"):
        print("'The extension of the file is : 'c''" )
    elif(i == "cpp"):
        print("'The extension of the file is : 'c ++''" )