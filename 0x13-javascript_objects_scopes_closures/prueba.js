#!/usr/bin/node
var john = {
	name: 'John',
	greet: (person) => { console.log("Hi " + person + ", my name is " + john.name);}
}
john.greet("Mark");
