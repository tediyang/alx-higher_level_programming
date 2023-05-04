#!/usr/bin/node
/*
    A script that gets the contents of a webpage and stores it in a file.
*/
const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const filename = process.argv[3];
request(URL, (err, res, body) => {
  if (err) throw err;
  fs.writeFile(filename, body.text, 'utf-8', err => {
    if (err) throw err;
  });
});
