#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error, data) {
      if (error) {
        console.log(error);
      }
    });
  }
});
