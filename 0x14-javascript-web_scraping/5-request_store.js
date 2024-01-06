#!/usr/bin/node

const request = require('request'); // Import the 'request' module
const fs = require('fs'); // Import the 'fs' module

const url = process.argv[2]; // Get the URL from the comma
const filePath = process.argv[3]; // Get the file path 

// Make a GET request to the specified URL
request(url, { encoding: 'utf-8' }, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Write the body content to specified file in utf-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
  });
});
