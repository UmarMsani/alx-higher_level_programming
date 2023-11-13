#!/usr/bin/node

// Get the first argument from command-line arguments
const arg = process.argv[2];

// Convert the argument to an integer
const convertedNumber = parseInt(arg);

// Check if the conversion is successful
if (!isNaN(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log("Not a number");
}
