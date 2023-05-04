#!/usr/bin/node
/*
  a script that prints the number of movies
  where the character “Wedge Antilles” is present.
*/
const request = require('request');
const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) throw err;
  const films = JSON.parse(body).results
    .map(film => film.characters)
    .map(character => character.filter(charMov => charMov.includes('18')))
    .filter(list => list.length !== 0);
  console.log(films.length);
});
