#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];

request(url + id + '/', function (error, response, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
