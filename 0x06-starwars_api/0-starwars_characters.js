#!/usr/bin/node
// Star wars api

const request = require('request');

const id = process.argv[2];

const base = 'https://swapi-api.alx-tools.com/api/';
const fullUrl = `${base}films/${id}`;

request(fullUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = body.characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  const chid = characters[index].split('/')[5];
  const charUrl = `${base}people/${chid}`;
  request(charUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(body.name);
      printCharacters(characters, index + 1);
    }
  });
}
