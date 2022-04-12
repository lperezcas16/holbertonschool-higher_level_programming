#!/usr/bin/node
const person = {
	  name: ['Bob', 'Smith'],
	  age: 32,
	  bio: function() {
		      console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
		    },
	  introduceSelf: function() {
		      console.log(`Hi! I'm ${this.name[0]}.`);
		    }
};
console.log(person.introduceSelf());
