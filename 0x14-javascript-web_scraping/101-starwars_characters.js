#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const fChars = JSON.parse(body).characters;
    printCharacters(fChars, 0);
  }
});

function printCharacters (fChars, idx) {
  request(fChars[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < fChars.length) {
        printCharacters(fChars, idx + 1);
      }
    }
  });
}
