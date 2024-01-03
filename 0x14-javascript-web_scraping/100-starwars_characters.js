#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const url = 'https://swapi.dev/api/films/' + process.argv[2]; // Construct the URL with the film ID

// Make a GET request to the Star Wars API films endpoint
request(url, function (error, response, body) {
  if (!error) {
    // Parse the response body to access the list of characters in the film
    const characters = JSON.parse(body).characters;

    // For each character in the film
    characters.forEach((character) => {
      // Make a GET request to the character's endpoint
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name); // Print the name of the character
        }
      });
    });
  }
});
