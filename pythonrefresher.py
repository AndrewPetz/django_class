age = 23

name = "Andrew"

todayIsCold = True

if age > 18:
    print("You are older than 18")
    print("This is another line")
else:
    print("You are younger than 18")

def hello(name="Andrew", age=23):
    return "Hello {} you are {} years old.".format(name, age)

sentence = hello()

print(sentence)


dognames = ["Fido", "Sean", "Sally", "Mark"]
dognames[1] = "Jane"
print(dognames)