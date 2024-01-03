#!/usr/bin/node

const fs = require('fs');

// Ensure both file path and content to write are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./writeFile.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the string content to the specified file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  // Check for errors during file writing
  if (err) {
    console.error(err); // Print the error object if an error occurred
    return;
  }
  console.log(`Content successfully written to ${filePath}`);
});
