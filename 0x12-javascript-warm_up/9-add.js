#!/usr/bin/node
const myVar = process.argv;

if (parseInt(myVar[2]) && parseInt(myVar[3])) {
  console.log(parseInt(myVar[3]) + parseInt(myVar[2]));
} else {
  console.log('NaN');
}
