#!/usr/bin/node
const OldSquare = require('./5-square.js');

class Square extends OldSquare {
  charPrint (c) {
    if (typeof(c) === 'undefined') {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
