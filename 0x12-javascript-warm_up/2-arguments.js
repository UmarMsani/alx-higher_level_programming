#!/usr/bin/node

// Get the number of command-line arguments
const numArguments = process.argv.length - 2;

// Print a message based on the number of arguments
if (numArguments === 0) {
  console.log("No argument");
} else if (numArguments === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
