#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const episodeNum = process.argv[2]; // Get the movie episode number from the command-line arguments
const API_URL = 'https://swapi-api.hbtn.io/api/films/'; // Base URL for the Star Wars API

// Make a GET request to the Star Wars API for the specified episode number
request(API_URL + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err); // Log an error if the request encounters an error
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body); // Parse the response body to JSON
    console.log(responseJSON.title); // Print the title of the movie
  } else {
    console.log('Error code: ' + response.statusCode); // Log an error code for non-200 status codes
  }
});
