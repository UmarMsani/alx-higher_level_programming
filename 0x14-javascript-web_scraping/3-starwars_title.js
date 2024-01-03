#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const movieID = process.argv[2]; // Get the movie ID from the command-line arguments
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`; // URL with the movie ID

// Make a GET request to the Star Wars API
request(url, function (error, response, body) {
  if (error) {
    console.error(error); // Log an error if request encounters an error
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const movie = JSON.parse(body); // Parse the response body to JSON
  console.log(`Title: ${movie.title}`); // Print the title of the movie
});
