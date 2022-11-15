#!/usr/bin/node
Error.stackTraceLimit = 0;

try {
  const fs = require('fs'); // Load the fs API
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf8');
} catch (e) {
  console.error(e);
}
