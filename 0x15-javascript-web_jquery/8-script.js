const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
  const film = data.results;
  for (let i = 0; i < film.length; i++) {
    $('UL#list_movies').append('<li>' + film[i].title + '</li>');
  }
});
