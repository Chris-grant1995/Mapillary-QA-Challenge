## Mapillary QA Challenge 

This is my submission for Mapillary's QA Software Engineer Position.

My task was to create a basic API with persistent storage and website that could both add to and get content from that API and then proceed to right a number of different tests for the API and website. 

I used Flask to create the API and Dash to create the website as it let me stay programming in Python for the entire challenge. 

For my tests, I used the standard python unittest framework as my testing platform, and used requests to query the API and Selenium to test the website. 

Once I had finished the basic website and API, I had some trouble coming up with tests because of the simplicity of the API and the website so I decided to make some changes to the API so I could write slightly more advanced tests. 

For a subset of my tests, I wanted to have some sort of input verification. So when the API gets a POST request to add to the database, prior to adding it to the database, I perform some basic regex to verify that the birthday field is a valid date (when any string could have been the input). If the matches, proceed as usual and add the new user. If it doensn't return a 400 code. 

To run the challenge simply clone the directory and build with `docker-compose build` and then run with `docker-compose up`

In addition to being accessable to the other Docker containers, the API and website are available to anyone running the containers. The API is accessable at `localhost:5000/users` and the website is accessable at `localhost:8050`. To change these ports, simply edit the `docker-compose.yaml` file. 
