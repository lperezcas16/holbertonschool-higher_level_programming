#!/usr/bin/node
const myVar = process.argv;

if (parseInt(myVar[2] && parseInt(myVar[3]))){
    myVar.sort(function(a, b){return b-a})
    let highest = myVar[2];
    console.log(highest);
} else {
    console.log('0');
}