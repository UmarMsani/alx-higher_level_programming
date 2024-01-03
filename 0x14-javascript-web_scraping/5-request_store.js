#!/usr/bin/node

const request = require('request'); // Import the 'request' module
const fs = require('fs'); // Import the 'fs' module

const url = process.argv[2]; // Get the URL from the command-line arguments
const filePath = process.argv[3]; // Get the file path to store the response body

// Make a GET request to the specified URL
request(url, { encoding: 'utf-8' }, function (error, response, body) {
  if (error) {
    console.error(error); // Log an error if the request encounters an error
    return;
  }

  // Write the body content to the specified file in utf-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err); // Log an error if writing to the file encounters an error
      return;
    }
    console.log(`Content successfully written to ${filePath}`); // Success message
  });
});
