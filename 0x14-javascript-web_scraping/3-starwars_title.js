#!/usr/bin/node
/* a script that prints the title of a Star
Wars movie where the episode number matches a given integer */
const request = require('request');
const URL = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(URL, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).title);
});
