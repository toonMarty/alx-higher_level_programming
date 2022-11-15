#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + episode, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const response = JSON.parse(body);
    console.log(response.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
