#PRINT FUNCTION is used to display something, it can be a string, an interger, a float, a boolean.

# Can print a string
print("Example of a string:")
print("Hello World")

# Can print nothing and skip a line... There should be an easier way of doing this.
print()

# Can print an interger
print("Example of interger:")
print(20)
print()

# Can print a float
print("Example of float:")
print(20.5)
print()

# By putting a number in between "" it will understand it as a text, it will look the same but future fuctions might be affected
print("Example of number as text:")
print("20")
print()

# Can print the result of an equation
print("Example of and equation result:")
print(2023-1990)
print()

# We can use one / to get the result as a float
print("Example of equations that ends in decimals:")
print(5/2)
print("Float")
print()
print(-5/2)
print("Float")
print()

# Or we can use two // to get the result as an interger - It will round down. Closert o 0 if positive, further from 0 if negative.
print("Example of equations that ends in decimals:")
print(5//2)
print("Interger")
print()

print("Example of equations that ends in decimals:")
print(-5//2)
print("Interger")
print()

# We can ask Python what is the type of the element, in case we are in doubt
print((type("Hello World")),("shows us it is a string"))
print((type("20")),("shows us it is a number written as a string, be careful with making this mistake"))
print((type(20)),("shows us it is an interger"))
print((type(20.5)),("shows us it is a float"))
print((type(False)),("shows us it is a boleean, a True or False statement based on logical premises"))
print()

# We can define elements, as this example of a static element
name = "Bessem"

# When concatenating elements we can use , or +
# + will not add space in between
print("Hello "+name+"!")
# , will add space in between
print("Hello",name,"!")
# So we might need to use both sometimes.
print("Hello",name+"!")
