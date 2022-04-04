#!/usr/bin/node
const myVar = process.argv;

console.log(parseInt(myVar[2]) ? 'My number: ' + parseInt(myVar[2]) : 'Not a number')
