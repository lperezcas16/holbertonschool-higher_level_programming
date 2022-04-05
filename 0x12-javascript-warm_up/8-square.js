#!/usr/bin/node
const myVar = process.argv;

if (!parseInt(myVar[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myVar[2]); i++) {
    console.log('x'.repeat(parseInt(myVar[2])));
  }
}
