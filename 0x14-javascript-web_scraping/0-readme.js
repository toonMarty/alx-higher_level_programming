#!/usr/bin/node
Error.stackTraceLimit = 0;

try {
  const fs = require('fs'); // Load the fs API
  const text = fs.readFileSync(process.argv[2], 'utf8');
  console.log(text);
} catch (e) {
  console.log(e);
}
