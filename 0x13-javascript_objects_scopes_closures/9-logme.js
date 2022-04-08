#!/usr/bin/node
let occur = 0;
exports.logMe = function (item) {
  console.log(occur + ': ' + item);
  occur += 1;
};
