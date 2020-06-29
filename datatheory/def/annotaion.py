
def f(ham: str, eggs: str ='eggs') -> str:
    print("Annotaiton:", f.__annotations__)
    print("arguments", ham, eggs)
    return ham + ' and ' + eggs

if __name__ =="__main__":
    f('spam')