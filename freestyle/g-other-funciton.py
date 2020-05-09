# Python program to illustrate fucntion with main

def getInteger():
    result = int(input("Enter integer: "))
    return result

def Main():
    print("Started")

    # calling the getInteger funciton and storing its returned
    # value in teh output variable
    output = getInteger()
    print(output)

# now we are required to tell Python
# for "Main" function existence
if __name__=="__main__":
    Main()
