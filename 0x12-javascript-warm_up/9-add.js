#!/usr/bin/node

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  console.log(a + b);
}
add(process.argv[2], process.argv[3]);
