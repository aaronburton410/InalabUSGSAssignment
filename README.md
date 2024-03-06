# Simple Flask App

A Python Flask application that says "Hello, World!"

## Goal

* "Dockerize" the application, providing an image and a configuration for
  running locally with Docker Compose.
* Provide a script to retrieve data from application and perform basic parsing.
* Provide a reverse proxy configuration.

## How to run the application
* make sure your environment has docker installed and running smoothly
* Run the Flask application and Nginx reverse proxy by executing
* docker-compose up --build
* command and the navigate to the http://localhost:5000 url in your browser
* to adjust the custom greeting, you edit the CUSTOM_MESSAGE tag in the docker-compose file to which message you want
* or else it will default to the default Hello world greeting