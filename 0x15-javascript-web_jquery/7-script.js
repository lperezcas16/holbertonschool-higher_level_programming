const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, textStatus) => {
  $('DIV#character').text(data.name);
});
