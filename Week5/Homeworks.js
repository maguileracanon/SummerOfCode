// ----------------Day 1 ///////////////////////
///////////////////////////////////////////////
//Hours in a year. How many hours are in a year?
console.log("There are", 365*24,"hours in a year")
//Minutes in a decade
console.log("There are", (60*24*365*10)+(60*24*2), "minutes in a dacade\n including leap years")
//My age in seconds
console.log("I am",(24*365*60*60*25)+(60*60*24*(6+46)) ,"seconds old")
//Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds
console.log("Cristina is",Date.now() -(new Date((2018-32),8,13,12,0,0,0)),"milliseconds old")

//Calculate your age accurately based on your birthday 
myBirthday = new Date(1993,6,30,12,0,0,0);
deltaTime = Date.now() - myBirthday;
// Since dates in Javascript are stored as milliseconds
console.log("I am", deltaTime, "milliseconds old")


//////-----------DAY 2 ////////////////////////////

//Music A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz 
//Calculate and console.log the frequency each of the 12 notes between A and A' 
//Hint: the notes are NOT in a linear scale, but in a geometric scale
//Reference : http://www.sengpielaudio.com/calculator-notenames.htm
console.log()
A = 49
A_p = 61
notes=["A4","A#4","B4","C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5"]
j=0
console.log("According to the reference, from a to a' we go from key", 49 ,"to key",61)
for(i=A; i <=A_p; i++){
	frequency = 440*(Math.pow(2,((i-49)/12))) 
	console.log("The frequency of",notes[j],"is",frequency)
	j++
}


///Planets Calculate and console log how many 'minutes' the Moon travels in a day. 
//Hint: first calculate how many degrees the Moons travels in the sky 
//when the Earth returns to the same position during its daily rotation.
//Reference = https://www.space.com/24871-does-the-moon-rotate.html
rot_around_earth = 1/29.5 
console.log("The moon moves", 360*rot_around_earth , "degrees per day around the earth")


/////////////////////// DAY 3  //////////////////////
//Full name greeting. Write a program that asks for a person’s first name, then middle, and then last.
// Finally, it should greet the person using their full name.
first_name = prompt("Please type your first name: ")
middle_name = prompt("Please type your middle name (press enter if you dont have one):")
last_name = prompt("Please type your last name")
alert("Wellcome "+ first_name +" " + middle_name+ " " + last_name)

//Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number,
//and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
fav_number = prompt("Type your favourite number:")
alert("Would you consider " + String(parseFloat(fav_number) + 1 )+  " as your bigger and better favorite number?")

//Angry boss. Write an angry boss program that rudely asks what you want. 
//Whatever you answer, the angry boss should yell it back to you and then fire you.

wish = prompt("What do you want now? :")
alert("WHADDAYA MEAN "+ wish.toUpperCase()+ "?!? YOU'RE FIRED!!")

/*
Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
Table of Contents

Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

Optional: in JS we may prefer to 'print' these to the HTML file itself rather than the console.
*/


/////////////////////// DAY 4  //////////////////////



