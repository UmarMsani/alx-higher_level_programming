#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const movieId = process.argv[2]; // Get the movie ID from the command-line arguments
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId); // Construct the full URL with the movie ID

// Make a GET request to the specified movie URL
request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters; // Parse the response body to access character URLs
    let charactersProcessed = 0; // Counter to track the number of characters processed
    const characterNames = []; // Array to store character names

    // Iterate through each character URL
    characters.forEach((characterUrl) => {
      // Make a GET request to the character's URL
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name; // Get the character's name from the response
          characterNames.push(charName); // Add the character's name to the array
        }
        charactersProcessed++;

        // If all characters have been processed, print their names
        if (charactersProcessed === characters.length) {
          characterNames.forEach((actor) => {
            console.log(actor); // Print each character's name
          });
        }
      });
    });
  } else {
    console.log(error); // Log an error if the request encounters an error
  }
});
