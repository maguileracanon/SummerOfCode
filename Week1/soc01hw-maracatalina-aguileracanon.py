from random import randint
#Day1 Homeworks
#Hours in a year. How many hours are in a year?
'''
print ("Hours in a year")
print(24*365)
print ("Minutes in a decade (including extra day every four years)")
print((60*24*365*10)+(60*24*2))
print("My Age in seconds")
print((25*365*60*60*24)+(60*60*24*(6+17)))

print("The age of Andreea Visanoiu​in years is")
print((48618000/(60*60*24))/365)
'''
#Day 3 Homeworks
'''
#Full name greeting.
first_name = input("What is your first name")
middle_name = input("What is your middle name")
last_name = input("What is your last name")
print("Welcome " + first_name + " " + middle_name + " " + last_name + " !!")
print("")
fav_num = input("Could you tell me your favourite numer?")
fav_num = int(fav_num)+1
fav_num = str(fav_num)
print("Congratulations! "+ fav_num+ " is your new bigger and better favorite number :P")

#Angry boss
chat = input("What do you need?: ")
print("WHAT DO YOU MEAN " +  chat.upper()+ "??? , YOU ARE FIRED!!")
'''

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
print("Let me give you the leap years between a period of time!! :D")
star_year = int(input("What is the starting year: "))
end_year = int(input(" OK, cool... now what would be the final year?: "))

list_of_leap_years = []

for i in range(star_year,end_year+1): # to enclude both limits
	if(i % 100 ==0):
		if(i % 400==0):
			list_of_leap_years.append(i)
			print(i)
	elif(i % 4 ==0):
		list_of_leap_years.append(i)
		print(i)

#print(list_of_leap_years)


'''


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
# Table of contents.
number_of_chapters = int(input("How many chapters are in your book? "))
print("ok... lets start adding the chapters information to the system")
book_info = []
for i in range (0,number_of_chapters):
	chap_name = input("Enter chapter name: ")
	chap_page = input("In wich page does this chapter starts")
	book_info.append([chap_name,chap_page])



# Old-school Roman numerals. 
'''
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
			number_in_romans +="L"*(l)
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
			new_Roman_number += "M"*(m)
			reminder = int_number % 1000	
		else:
			reminder = int_number
		# Evaluate 500
		if(reminder >= 500):
			if (reminder !=900):
				d = reminder // 500
				new_Roman_number +="D"*(d)
				reminder = reminder %500
			else:
				new_Roman_number+= "CM"
				reminder = reminder % 900

		else:
			c = reminder //100
			if(c==4):
				new_Roman_number+="CD"
				reminder = reminder %400

		c = reminder //100
		if(c!=0):
			new_Roman_number+="C"*(c)
			reminder = reminder %100

		# Evaluate 50
		if (reminder >=50):
			if(reminder !=90):
				l = reminder// 50
				new_Roman_number +="L"*(l)
				reminder = reminder %50
			else:
				new_Roman_number+= "XC"
				reminder = reminder %90
		else:
			x = reminder // 10
			if(x==4):
				new_Roman_number +="XL"
				reminder = reminder % 40

		#evaluate 10
		x = reminder // 10
		if(x !=0):
			number_in_romans +="X"*(x)
			reminder = reminder %10


		if (reminder >= 5):
			if(reminder !=9):
				v= reminder //5
				new_Roman_number +="V"*(v)
				reminder = reminder %5
			else:
				new_Roman_number +="IX"
				reminder = reminder % 9

		new_Roman_number += "I"*reminder
		print("your number in new romans style is :")
		print(new_Roman_number)

int_number = int(input("Writte number to convert: "))
convertNumber(int_number)
convertNewRoman(int_number)
'''