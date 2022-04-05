#!/usr/bin/node
const myVar = process.argv;

if (parseInt(myVar[2])) {
  const value = parseInt(myVar[2]);
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
