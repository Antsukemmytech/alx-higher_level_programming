#!/usr/bin/node
const number = parseInt(process.argv[2]);
if (number.isNan(number)) {
  console.log('Not a number');
} else {
  console.log('my number: ' + number);
}
