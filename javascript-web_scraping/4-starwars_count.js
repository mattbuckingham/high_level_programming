#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];
const actorId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const data = JSON.parse(body);
    const movies = data.results;

    for (const movie of movies) {
      if (movie.characters.some(character => character.includes(`people/${actorId}`))) {
        count++;
      }
    }
    console.log(count);
  }
});
