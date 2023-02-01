#reference variable 
# memory utilization by allocation the same object reference to a new variable if the object already exists with the same value.
x = 10
y = x

if id(x) == id(y):
	print("x and y refer to the same object")

#if x and y do not refer to the same object
#memory utilization by allocation the same object reference to a new variable
x = 10
y = x
x += 1

if id(x) != id(y):
	print("x and y do not refer to the same object")
