#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const apiUrl = process.argv[2]; // Get the API URL from the command-line arguments
const characterId = '18'; // Character ID for Wedge Antilles

// Make a GET request to the Star Wars API films endpoint
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error); // Log an error if the request encounters an error
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const films = JSON.parse(body).results; // Parse the response body to access the films data
  const moviesWithWedgeAntilles = films.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  ); // Filter movies where Wedge Antilles appears

  console.log(`${moviesWithWedgeAntilles.length}`); // Print the count
});
