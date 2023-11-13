#!/usr/bin/node

// Get the first argument from command-line arguments
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);
let i, j;

// Check if the conversion is successful
if (!isNaN(size)) {
  // Loop to print a square of size x size
  for (i = 0; i < size; i++) {
    let row = '';
    for (j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log("Missing size");
}
