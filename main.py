# get Name function
def getName():
	userName = input("Please tell me your name: ")
	# userName variable is specific to this function
	return userName


def greetUser(name): #parameter variables are specific to the function
	print("Hi " + name)

#name1 = getName()
#print("Hi " + name1)
# Instead of doing the 2 lines of code above just do this
greetUser(getName())

#name2 = getName()
#print("Hi " + name2)
greetUser(getName())

#name3 = getName()
#print("Hi " + name3)
greetUser(getName())

 #Ask the user for 2 numbers - num1, num2
 #Write a function that takes num1 and num2 as parameters and prints the sum
num1 = int(input("Choose a number: "))
num2 = int(input("Choose another number: "))

def sum(num1, num2):
	print("The sum is " + str(num1+num2))

sum(num1, num2)

# prints the sum
def sum(numList):
	total = 0
	for index in numList:
		total += index
	print("The sum is " + str(total))

sum([1,2,3,4,5,6,7,8,9,10]) #55
