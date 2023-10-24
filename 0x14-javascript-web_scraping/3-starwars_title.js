#!/usr/bin/node

const request = require('request');
const eNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + eNum, (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const res = JSON.parse(body);
    console.log(res.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
