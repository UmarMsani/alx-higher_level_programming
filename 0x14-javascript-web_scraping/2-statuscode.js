#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const url = process.argv[2]; // Get the URL from the command-line arguments

// Make a GET request to the provided URL
request(url, function (error, response) {
  if (error) {
    console.error(error); // Log an error if request encounters an error
    return;
  }
  console.log(`code: ${response.statusCode}`); // Display the status code of the response
});
