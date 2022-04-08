#!/usr/bin/node

const OldSquare = require('./5-square.js');
class Square extends OldSquare {
  charPrint (c) {
    let character = 'X';
    if (c !== undefined) {
      character = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}
module.exports = Square;
