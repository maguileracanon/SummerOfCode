/*
function myFunction(p1,p2){
	return p1*p2
}

console.log( myFunction( 3,8))

function toCelsius(fahrenheit){
	return (fahrenheit -32) *(5/9)
}

document.getElementById("anavirginia").innerHTML = toCelsius(63)

*/

function showName(firstName,lastName){
	var nameIntro="Your name is "
	function makeFullName(){
		return nameIntro + firstName + " " + lastName
	}
	return makeFullName()
}

document.getElementById("anavirginia").innerHTML = showName("Mara","Aguilera")
showName("Mara","Aguilera")
/*
$(function(){
	var selections = []
	$(".myButton").click(function(){
		selections.push(this.prompt("name"))
	})
})
*/
function celebrityID(){
	var celebrityID = 999
	return {
		getID: function(){
			return celebrityID
		},
		setID: function (theNewID) {
			celebrityID = theNewID
		}
	}
}

var mjID = celebrityID()
console.log(mjID)
console.log(mjID.getID())
mjID.setID(3141)
console.log(mjID.getID())
//hoisting 
var x
var y=7
x=5


elem = document.getElementById("kasia")
elem.innerHTML =x+" " + y

 //declaration after using variable, its fine javascript allows this
// oeri var x=17 es initialization y no la declara

//let and const are not hoisted


function celebrityIDCreator(theCelebrities){
	var i 
	var uniqueID = 100
	for (i=0; i< theCelebrities.length; i++){
		theCelebrities[i]["id"] = function(){
		return uniqueID+i
	}
	}

	return theCelebrities
}


var romComCelebs = [{name: "Reese Witherspoon", id:0},{name:"Julia Roberts",id:0},{name:"Meg Ryan",id:0}]
var createIdForRomComCelebs = celebrityIDCreator (romComCelebs)
var reeseID = createIdForRomComCelebs[0]
console.log(reeseID.id())
