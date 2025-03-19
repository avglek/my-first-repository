print ("test repository")
print ("test")

def say_something(number:int, word:str)->str:
    word = word.capitalize()
    return word * number

print("Echo "+say_something(5,"test"))

