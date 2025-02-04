#input
integer_in = int(input("Enter an integer: "))
float_in = float(input("Enter a float: "))
string_in = str(input("Enter a string: "))

print(type(integer_in))
print(type(float_in))
print(type(string_in))

text = ("123")
number = int(text)  #convert
float_num = float(number)

print(type(number))
print(type(float_num))
print(type(text))

person = {    #dict
    "name": "Bob",
    "age" : "30"
}

print(person["name"])

#operations on set
my_set = {1,2,3}
my_set.add(4)
my_set.remove(2)
print(3 in my_set)