/*
a JavaScript script that fetches and lists the title for all
movies by using this
URL: https://swapi-api.hbtn.io/api/films/?format=json
 */

const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
