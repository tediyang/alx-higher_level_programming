#!/usr/bin/node
// Write to a file.
const fs = require('fs');
const filename = process.argv[2];
const words = process.argv[3];
fs.writeFile(filename, words, 'utf-8', err => {
  if (err) throw err;
});
