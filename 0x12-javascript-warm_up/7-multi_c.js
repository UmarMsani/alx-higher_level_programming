#!/usr/bin/node

// Get the first argument from command-line arguments
const arg = process.argv[2];

// Convert the argument to an integer
const numOccurrences = parseInt(arg);
let i;

// Check if the conversion is successful
if (!isNaN(numOccurrences)) {
  // Loop to print "C is fun" x times
  for (i = 0; i < numOccurrences; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences");
}
