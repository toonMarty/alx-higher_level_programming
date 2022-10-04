#!/usr/bin/node

let idx;

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (idx = 0; idx < process.argv[2]; idx++) {
    console.log('C is fun');
  }
}
