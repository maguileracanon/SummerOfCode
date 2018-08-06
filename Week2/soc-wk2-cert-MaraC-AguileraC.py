# Day 1
from random import choice
#Calculate a table for each letter in the alphabet from a-z, 
#and count how many times each letter appears in alice_in_wonderland.txt 
#this is a library to concatenate lists in a matrix
'''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
counter = [0 for i in range(len(alphabet))]
filename = "aliceInWonderland.txt"
file = open(filename,"r")
raw = file.read()
for letter in range(0,len(alphabet)):
	for i in range(0,len(raw)):
		if(raw[i].lower() == alphabet[letter]):
			counter[letter] += 1
#result = np.c_[alphabet,counter]
for letter in range(0,len(alphabet)):
	print(alphabet[letter] + "   =   " + str(counter[letter]))
	'''

#-------------DAy 2 ---------------------------------
#_____________________________________________________
#_____________________________________________________


#There is something small that needs fixing. Can you spot it and fix it? (Hint, we only want A-Z and a-z)
'''
for i in range(65,65+26):
	print(i, "stands for ", chr(i))
for j in range(97,97+26):
	print(j, "stands for ", chr(j))
'''
#Make a function that prints A-Z and a-z
'''
def characterASCI():
	for i in range(65,65+26):
	print(i, "stands for ", chr(i))
	for j in range(97,97+26):
	print(j, "stands for ", chr(j))
'''

#Make a function that asks the user for a message, and turns it into a list of numbers. (It's a cypher ;))
'''
lookUpTable = []
listCharacters = []
for i in range(65,65+26):
	lookUpTable.append(i)
	listCharacters.append(chr(i))
for i in range(97,97+26):
	lookUpTable.append(i)
	listCharacters.append(chr(i))	



def EncriptMe(message):
	encodedMessage = " "
	for k in range(len(message)):
		for letter in range(len(lookUpTable)):
			if(message[k]==listCharacters[letter]):
				encodedMessage += str(lookUpTable[letter]) + " "
	print(encodedMessage)

secret =input("Give me a message to encript: ")
EncriptMe(secret)

'''
# "M" is visually more dense than "o".​
'''
M = "land"
o = "water"
world = [
 [o,o,o,o,o,M,o,o,o,o,o], # list of lists
 [o,o,o,o,M,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,M,M,o],
 [o,o,o,M,o,o,o,o,o,M,M],
 [o,o,o,M,o,M,M,o,o,o,o],
 [o,o,o,o,M,M,M,M,o,o,o],
 [o,o,o,M,M,M,M,M,M,M,M],
 [o,o,o,M,M,o,M,M,M,o,o],
 [o,o,o,o,o,o,M,M,o,o,o],
 [o,M,o,o,o,M,o,o,o,o,o],
 [o,o,o,o,o,o,o,o,o,o,o]
 ]

#Write a function that prints out all elements of the above board, starting from the first element of the first line, till the end. 
#Each line should be read from beginning to end.

def print_world(a_world):
	row_toprint = " "
	for i in range(len(a_world)):
		for j in range(len(a_world[1])):
			row_toprint += (a_world[i][j]) + " "
		print (row_toprint)
		row_toprint = " "
#Now write a function that prints out all elements in reverse.

def print_inverse(a_world):
	row_toprint = " "
	for i in range(len(a_world)-1,-1,-1):
		for j in range(len(a_world[1]) -1,-1,-1):
			row_toprint += (a_world[i][j]) + " "
		print (row_toprint)
		row_toprint = " "


#print_world(world)
print("")
#print_inverse(world)
'''

'''
#There is one small bug in the continent counter above. Can you find it and fix it? (Hint: change the world so that the continent borders the edge)
def continent_counter(world, x , y):
	if (world[y][x] != 'land'):
		return 0
	size = 1
	world[y][x] = 'counted land'
	#row above
	if (x>=0 and x<len(world)):
		if(y>=0 and y<len(world)):
			size = size + continent_counter (world, x-1,y-1)
			size = size + continent_counter(world, x , y-1)
			size = size + continent_counter(world, x-1, y )
			size = size + continent_counter(world, x+1, y-1)
			size = size + continent_counter(world, x+1, y)
			size = size + continent_counter(world,x-1,y+1)
			size = size + continent_counter(world, x, y+1)
			size = size + continent_counter(world, x+1, y+1)
	return size

print(continent_counter(world,5,5))
'''
#Write a function that generates an n x n sized board with either land or water chosen randomly.
'''
choices = ['land','water']
world = []
def randomWorld(worldSize):
	for i in range (0,worldSize):
		world.append([" "] * worldSize)
		for j in range (0,worldSize):
			world[i][j] = choice(choices)
	

randomWorld(5)
print_world(world)
'''

######################################################
#################DAY 3 ###############################
######################################################

#Modify "a" for another name in my_dict
'''
my_dict = {
    "a": 35000,
    "b": 8000,
    "z": 450
}

def modifyKey(dictionary_name,Oldkey,newKey):
	dictionary_name[newKey] = dictionary_name[Oldkey]
	#print(dictionary_name)
	del(dictionary_name[Oldkey])

modifyKey(my_dict,"a","IamNot_a")
print(my_dict)
'''
#Redo the frequency distribution of alice_in_wonderland.txt and 
#save your result in a dictionary.
'''
alphabet2 = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}

filename2 = "aliceInWonderland.txt"
file2 = open(filename2,"r")
raw2 = file2.read()

for i in range(0,len(raw2)):
	if((raw2[i].lower()).isalpha()):
		alphabet2[raw2[i].lower()] +=1
print(alphabet2)

#Create a dictionary with your own personal details, 
mara = dict(name = "mara", age = 25 , petname = "luna" , favColour ="pink")
print(mara)
'''
#Review the chat reply of today's beautiful class interaction and instantiate a student variable for everyone who shared their dream.
'''
students = []
class Student():
	def __init__(self,name,discord_id,fav_food,dream): # so that I can set it up in the constructor
		self.name = name
		self.discord_id =  discord_id
		self.fav_food = fav_food
		self.dream = dream
	def my_print(self):
		print(self.name +" "+self.discord_id +" "+self.fav_food +" "+self.dream)

students.append(Student("Andreea Visanoiu","Andreea[GOLD]","wontonmee","teaching at university"))
students.append(Student("Virginia Balseiro","yesvirginia","pasta","moving to europe"))
students.append(Student("Cristina Tarantino","CristinaTarantino[Gold]","pasta","being an amazing developer"))
students.append(Student("Sacha Yung","sacha[GOLD]", "french fries", "to return to research"))
students.append(Student("Jessica","Jessi_RS[GOLD]","pasta","work as a developer by the end of the year"))
students.append(Student("Bituin Callanta", "bituin[gold]","sashimi","lessen the gender wage gap"))

for i in range(len(students)):
	students[i].my_print()


# taxonomy of Classes for 1MWTT

class Person():
	def __init__(self,name,last_name,discord_id,nationality,country_based_in,email,github_account):
		self.name = name + last_name
		self.discord_id = discord_id
		self.nationality = nationality
		self.country_based_in = country_based_in
		self.email = email
		self.github_account = github_account

class Student(Person):
	
	def __init__(self, name,last_name,discord_id,nationality,country_based_in,email,github_account,education_level,programming_skills_level):
		super().__init__(self, name,last_name,discord_id,nationality,country_based_in,email,github_account)
		self.education_level = education_level
		self.programming_skills_level = programming_skills_level
class Employer(Person):

	def __init__(self,name,last_name,discord_id,nationality,country_based_in,email,github_account,company_name,skills_required):
		super().__init__(self, name,last_name,discord_id,nationality,country_based_in,email,github_account)
		self.company_name = company_name
		self.skills_required = skills_required

class Mentor(Student):
	"""docstring for ClassName"""
	def __init__( self, name,last_name,discord_id,nationality,country_based_in,email,github_account,education_level,programming_skills_level, mentoring_in, available_hours_per_week):
		super().__init__(self, name,last_name,discord_id,nationality,country_based_in,email,github_account,education_level,programming_skills_level)
		self.mentoring_in = mentoring_in
		self.available_hours_per_week = available_hours_per_week

'''
		