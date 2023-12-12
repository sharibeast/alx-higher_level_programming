#!/usr/bin/node
const text = 'C is fun';
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let index = 0; index < x; index++) {
    console.log(text);
  }
}
