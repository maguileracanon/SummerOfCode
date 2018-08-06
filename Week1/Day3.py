#Day 3 

name = "Mara Catalina Aguilera Canon"
result=""
# name[-1] es la ultima letra : n 
#name[-2] es la penultima : o

for i in range(0,len(name)):
	#print(name[i])
	if i % 2 ==0:
		print(name[i])
		result = result + name[i]
		print('result just changed to: '  + result)

print('The final result for all even indexed letters in name is' + result + 'lalalal')

#>>> name = "Mara CAtalina"
#>>> name[-1]
#'a'
#>>> name[-2]
#'n'
#>>> str(2)
#'2'
#>>> var1=2
#>>> var2='5'
#>>> str(var1) + var2
#'25'
#>>> int(var2) +var1
#7
#>>>