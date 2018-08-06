def myPrint(n):
	for i in range(0,n):
		print("moo"*n) #side effect
	return ("moo"*n) #return value


# recursive function

def ask_recursively(question):
	print(question)
	reply = input("> ").lower()
	if reply=="yes":
		return True
	if reply=="no":
		return False
	else:
		print("please answer yes or no")
		ask_recursively(question)

ask_recursively("jajja?")
filename = "my_test_file.txt"
file = open(filename, "r") # I assume "r" stands for reading
#for line in file:
#	print(line)
raw = file.read()
print(raw[:3])
print("the lenght of this file is : " + str(len(raw)))