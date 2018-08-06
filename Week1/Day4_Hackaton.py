from random import randint
#Day4 Homeworks
'''
#Lyric of 99 bottles of BEer
first_verse= " bottles of beer on the wall  "
second_first = " bottles of beer."
second_verse = "Take one down and pass it around, "
next_count = " "
for b in range(99,0,-1):
	print(str(b) + first_verse + ", " + str(b) + second_first)
	if b > 1:
		next_count= str(b-1)
	elif b==1:
		next_count = "no more"
	print(second_verse + next_count + first_verse)
	print("")

print("No more bottles of beer on the wall, no more bottles of beer. ")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
'''
#Deaf Grandma
'''
num_of_bye=0
while num_of_bye < 3:
	message = input("Say something to grandma: ")
	if(message == "BYE"):
		num_of_bye +=1

	if message.isupper():
		randomyear = randint(1930, 1950) 
		print("NO, NOT SINCE " + str(randomyear))
	else:
		print("HUH?! SPEAK UP, GIRL!")

	

print("BYE SWEETHEARTH ♥")
'''
#Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them
# (and including them, if they are also leap years).



'''
#Write a function that prints out "moo" n times.
def myPrint(n):
	for i in range(0,n):
		print("moo")

x= input("Number of times desired: ")
myPrint(int(x))
'''
'''
#Building and sorting an array. Write the program that asks us to type as many words as we want 
#(one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. 
list_of_Strings=[]
newString = input("Type a new word, when you are ready press Enter to get your sorted the list:")
while (newString!=""):
	newString = input("Type a new word, when you are ready press Enter to get your sorted the list:")
	list_of_Strings.append(newString)

list_of_Strings.sort();
print(list_of_Strings)
'''

'''
# Old-school Roman numerals. 

def convertNumber(int_number):
	number_in_romans = ""
	if(int_number <3000):

		# Evaluate 1000
		m = int_number // 1000
		if(m!=0):
			number_in_romans += "M"*(m)
			reminder = int_number % 1000	
		else:
			reminder = int_number
		# Evaluate 500
		d = reminder // 500
		if(d!=0):
			number_in_romans +="D"*(d)
			reminder = reminder %500
		# Evaluate 100
		c = reminder //100
		if(c!=0):
			number_in_romans +="C"*(c)
			reminder = reminder %100
		# Evaluate 50
		l = reminder// 50
		if(l!=0):
			number_in_romans +="D"*(l)
			reminder = reminder %50
		#evaluate 10
		x = reminder // 10
		if(x !=0):
			number_in_romans +="X"*(x)
			reminder = reminder %10
		v= reminder //5
		if(v !=0):
			number_in_romans +="V"*(v)
			reminder = reminder %5

		number_in_romans += "I"*reminder
		print("your number in old romans is :")
		print(number_in_romans)

def convertNewRoman(int_number):
	new_Roman_number = ""
	if(int_number <3000):

		# Evaluate 1000
		m = int_number // 1000
		if(m!=0):
			number_in_romans += "M"*(m)
			reminder = int_number % 1000	
		else:
			reminder = int_number
		# Evaluate 500
		d = reminder // 500
		if(d!=0):
			number_in_romans +="D"*(d)
			reminder = reminder %500
		# Evaluate 100
		c = reminder //100
		if(c!=0):
			number_in_romans +="C"*(c)
			reminder = reminder %100
		# Evaluate 50
		l = reminder// 50
		if(l!=0):
			number_in_romans +="D"*(l)
			reminder = reminder %50
		#evaluate 10
		x = reminder // 10
		if(x !=0):
			number_in_romans +="X"*(x)
			reminder = reminder %10
		v= reminder //5
		if(v !=0):
			number_in_romans +="V"*(v)
			reminder = reminder %5

		number_in_romans += "I"*reminder
		print("your number in old romans is :")
		print(number_in_romans)
int_number = int(input("Writte number to convert: "))
convertNumber(int_number)
'''