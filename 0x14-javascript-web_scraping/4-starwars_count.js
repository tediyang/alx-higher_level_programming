#!/usr/bin/node
/*
  a script that prints the number of movies
  where the character “Wedge Antilles” is present.
  The first argument is the API URL of the
  Star wars API: https://swapi-api.alx-tools.com/api/films/
  Wedge Antilles is character ID 18 - 
  your script must use this ID for filtering the result of the API
  You must use the module request
*/
const request = require('request');
const URL = process.argv[2];
request(URL, (err, res, body) => {
  if (err) throw err;
  const films = JSON.parse(body).results
   .map(film => film.characters)
   .map(character => character.filter(char_mov => char_mov.includes('18')))
   .filter(list => list.length != 0);
  console.log(films.length);
  }
);
