#!/usr/bin/node

const OldSquare = require('./5-square.js');
class Square extends OldSquare {
  charPrint (c) {
    if (c === undefined) {
      printSquare('X', this.width, this.height);
    } else {
      printSquare('C', this.width, this.height);
    }
  }
}

function printSquare (character, width, height) {
  for (let i = 0; i < height; i++) {
    console.log(character.repeat(width));
  }
}
module.exports = Square;
