#!/usr/bin/node

const fs = require('fs'); // Import the 'fs' module to work with the file system
const file = process.argv[2]; // Get the file path from the command-line arguments
const string = process.argv[3]; // Get the string to be written from the command-line arguments

// Write the string content to the specified file in utf-8 encoding
fs.writeFile(file, string, 'utf-8', function (err) {
  if (err) console.log(err); // Print the error object if an error occurred during file writing
});
