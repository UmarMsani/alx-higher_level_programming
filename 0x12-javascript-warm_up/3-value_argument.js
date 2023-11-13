#!/usr/bin/node

// Get the first argument from command-line arguments
const firstArgument = process.argv[2];

// Print the first argument or "No argument" if none is provided
console.log(firstArgument ? firstArgument : "No argument");
