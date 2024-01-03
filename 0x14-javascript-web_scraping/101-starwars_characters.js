#!/usr/bin/node

const request = require('request'); // Import the 'request' module

const apiUrl = process.argv[2]; // Get the API URL from the command-line arguments

// Make a GET request to the specified API URL
request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error); // Log an error if the request encounters an error
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status Code ${response.statusCode}`); // Handle non-200 status codes
    return;
  }

  const tasks = JSON.parse(body); // Parse the response body to access task data

  // Object to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Loop through each task
  tasks.forEach((task) => {
    if (task.completed) {
      // Increment the completed task count for the respective user
      completedTasksByUser[task.userId] = (completedTasksByUser[task.userId] || 0) + 1;
    }
  });

  // Print users with completed tasks
  Object.keys(completedTasksByUser).forEach((userId) => {
    console.log(`User ${userId}: ${completedTasksByUser[userId]} completed tasks`);
  });
});
