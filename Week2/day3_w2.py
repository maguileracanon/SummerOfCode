#DAy 3
'''
my_dict = {
	"a": 3500,
	"b": 700,
	"z":450
}
print(my_dict["a"])
print(my_dict)
#add
my_dict["favNum"] = 2605
print(my_dict["favNum"])
print(my_dict)
#modify
my_dict["a"] = 50
print(my_dict["a"])
print(my_dict)
#delete item
del(my_dict["a"])
#print(my_dict)
'''

#dictionary constructor
#mara = dict(name = "Catalina", last_name= "Aguilera", anotherlastname = "canon")

#CLASES

class Student():
	def __init__(self,name,discord_id,fav_food,dream): # so that I can set it up in the constructor
		self.name = name
		self.discord_id =  discord_id
		self.fav_food = fav_food
		self.dream = dream
	def my_print(self):
		print(self.name +" "+self.discord_id +" "+self.fav_food +" "+self.dream)

#instantiate using constructor
s1 = Student("mara","maraCatalina[DIY]","rissotto","finish PhD")
#s2 = Student("LunaPechita")

print(s1.discord_id)
#print(s2.discord_id)
s1.my_print()