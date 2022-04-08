#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    let l = 'X';
    if (c !== undefined) {
      l = c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(l.repeat(this.width));
    }
  }
}
module.exports = Square;
