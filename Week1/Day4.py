#Day4 excluyendo loops porq eso solo es repetir lo q ella hizo
#Comprehsive list
food = ["icecream", "pizza", "popcorn","paella"]

favorite = [print(f) for f in food]

print(favorite) # Prints NONE,NONE,NONE because it doesnt create
#it just prints, doesnt store anything

favorite = [f+" is tasty" for f in food]
print(favorite)
favorite.append("salad")
favorite.sort()
print(favorite)
favorite.pop() # removes the last element of the list