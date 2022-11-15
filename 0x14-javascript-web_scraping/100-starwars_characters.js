#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const fChars = data.characters;
  for (const i of fChars) {
    request.get(i, function (error, response, otherBody) {
      if (error) {
        console.log(error);
      }
      const otherData = JSON.parse(otherBody);
      console.log(otherData.name);
    });
  }
});
