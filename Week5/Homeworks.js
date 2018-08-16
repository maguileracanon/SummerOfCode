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


/////////////////////////////////////////////