#!/usr/bin/node
// Read the file and print its contents.
const fs = require('fs');
const filename = process.argv[2];
const words = process.argv[3];
fs.writeFile(filename, words, "utf-8", err => {
    if (err) throw err;
});
