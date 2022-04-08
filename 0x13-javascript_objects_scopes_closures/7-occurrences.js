#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;
  let item;
  for (item of list) {
    if (item === searchElement) {
      occur += 1;
    }
  }
  return occur;
};
