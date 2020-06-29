def revert(string):
    if string: 
        string = string[-1] + revert(string[:-1])
    return string

def revert2(string):
    return string[::-1] 

def revert3(string):
    return string[len(string)+1::-1]
    
if __name__ == "__main__":
    print(revert("hello world"))
    print(revert2("hello world"))
    print(revert3("hello world"))
    