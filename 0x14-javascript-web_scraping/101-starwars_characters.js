#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const url = 'https://swapi.dev/api/films/' + process.argv[2]; // Construct the URL with the film ID

// Make a GET request to the Star Wars API films endpoint
request(url, function (error, response, body) {
  if (!error) {
    let characters = JSON.parse(body).characters; // Parse the response body to access the list of characters
    printCharacters(characters, 0); // Call the function to print characters recursively starting from index 0
  }
});

// Function to print characters recursively
function printCharacters(characters, index) {
  // Make a GET request to the character's endpoint
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name); // Print the name of the character

      // If there are more characters, call the function recursively for the next character
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
