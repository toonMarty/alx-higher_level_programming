#!/usr/bin/node

let idx;
let j;

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < process.argv[2]; idx++) {
    let row = '';
    for (j = 0; j < process.argv[2]; j++) {
      row += 'X';
    }
    console.log(row + ' ');
  }
}
