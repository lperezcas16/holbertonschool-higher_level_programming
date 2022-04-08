#!/usr/bin/node

const oldSquare = require('./5-square.js');
class Square extends oldSquare {
  charPrint (c) {
    if (!c) {
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
