#!/usr/bin/node

const fs = require('fs');

// Ensure a file path argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the file in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  // Check for errors during file reading
  if (err) {
    console.error(err); // Print the error object if an error occurred
    return;
  }
  console.log(data); // Print the content of the file
});
