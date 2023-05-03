#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Usage: ./0-readme.js Filename');
  process.exit(1);
}

// Read the file and print its contents.
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
