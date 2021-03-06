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

chapters_info=[["Getting Started",1],["Numbers",9],["Letters",13]]
for(i=0;i<chapters_info.length;i++){
	console.log("Chapter "+String(i+1)+":   "+chapters_info[i][0]+"           page  "+String(chapters_info[i][1]));
}


/////////////////////// DAY 4  //////////////////////
//“99 Bottles of Beer on the Wall.” Write a program that prints out the lyrics to that beloved classic,
// “99 Bottles of Beer on the Wall.”
first_verse= " bottles of beer on the wall  ";
second_first = " bottles of beer.";
second_verse = "Take one down and pass it around, ";
next_count = " ";
b=99;
while (b>0) {
	console.log(String(b) + first_verse + ", " + String(b) + second_first);
	if (b > 1){
		next_count= String(b-1);
	}
	else if (b==1){
		next_count = "no more";
		}
	console.log(second_verse + next_count + first_verse);
	console.log("");
	

	b=b-1;
	
}
console.log("No more bottles of beer on the wall, no more bottles of beer. ")
console.log("Go to the store and buy some more, 99 bottles of beer on the wall.")

/*
Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!
unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:
NO, NOT SINCE 1938!

Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.

*/

num_of_bye=0;
while (num_of_bye < 3){
	message = prompt("Say something to grandma: ");
	if(message == "BYE"){
		num_of_bye +=1;
	}

		if (message== message.toUpperCase() && num_of_bye < 3){
			randomyear = Math.floor(Math.random() * (1950-1930 + 1))  + 1930 ;
			alert("NO, NOT SINCE " + String(randomyear));
		}
		else{
			alert("HUH?! SPEAK UP, GIRL!");
		}
	
}
	
alert("BYE SWEETHEARTH <3");

/*
Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years). 
Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!
*/

alert("Let me give you the leap years between a period of time!! :D")
star_year = parseInt(prompt("What is the starting year: "))
end_year = parseInt(prompt(" OK, cool... now what would be the final year?: "))

list_of_leap_years = [];
index_list = 0;
for (i=star_year; i< end_year; i++) {//# to include both limits
	if(i % 100 ==0){
		if(i % 400==0){
			list_of_leap_years[index_list] =i;
			index_list++;
			console.log(i);
		}
	}
	else if(i % 4 ==0){
		list_of_leap_years[index_list] =i;
		index_list++;
		console.log(i);
	}
} 
console.log(list_of_leap_years)

/*
Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; 
for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?
*/ 

list_of_Strings=[];
index_array=0;
newString = prompt("Type a new word, when you are ready press Enter to get your sorted the list:")
while (newString!=""){
	list_of_Strings[index_array]=newString.toLowerCase();
	index_array++;
	newString = prompt("Type a new word, when you are ready press Enter to get your sorted the list:")
}

list_of_Strings.sort();
console.log(list_of_Strings)

/*
Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). 
Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center
*/
