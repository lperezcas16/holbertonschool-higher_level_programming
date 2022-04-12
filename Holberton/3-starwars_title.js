#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
