#!/usr/bin/node
/*
  a script that prints the number of movies
  where the character “Wedge Antilles” is present.
*/
const request = require('request');
const id = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;
/*
  Step 1: Create a GET request.
  Step 2: Throw the error if one occurred.
  Step 3: Get the results in json format,
  getting all the characters from each film.
  Step 4: Map every character link and get the name of the char.
  Step 5: Print the characters.
*/
request(URL, (error, response, body) => {
  if (error) throw error;
  const filmChars = JSON.parse(body).characters
    .map(character => request(character, (err, res, bdy) => {
      if (err) throw err;
      return JSON.parse(bdy).name;
    }));
  console.log(filmChars);
});
