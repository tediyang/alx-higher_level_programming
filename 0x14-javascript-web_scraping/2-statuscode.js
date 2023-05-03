#!/usr/bin/node
// Get status code.
const request = require('request');
const URL = process.argv[2];
request (URL, (err, res, body) => {
  if (err) throw err;
  console.log(`Code: ${res.statuscode}`);
})
