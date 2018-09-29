## Mapillary QA Challenge 

This is my submission for Mapillary's QA Software Engineer Position.

My task was to create a basic API with persistent storage and website that could both add to and get content from that API and then proceed to right a number of different tests for the API and website. 

I used Flask to create the API and Dash to create the website as it let me stay programming in Python for the entire challenge. 

For my tests, I used the standard python unittest framework as my testing platform, and used requests to query the API and Selenium to test the website. 

Once I had finished the basic website and API, I had some trouble coming up with tests because of the simplicity of the API and the website so I decided to make some changes to the API so I could write slightly more advanced tests. 

For a subset of my tests, I wanted to have some sort of input verification. So when the API gets a POST request to add to the database, prior to adding it to the database, I perform some basic regex to verify that the birthday field is a valid date (when any string could have been the input). If the matches, proceed as usual and add the new user. If it doensn't return a 400 code. 

To run the challenge simply clone the directory and build with `docker-compose build` and then run with `docker-compose up`

In addition to being accessable to the other Docker containers, the API and website are available to anyone running the containers. The API is accessable at `localhost:5000/users` and the website is accessable at `localhost:8050`. To change these ports, simply edit the `docker-compose.yaml` file. 


Questions:
1. Explain how these tests would be run in a ci environment. what type of infrastructure would you set up? for example, “I would create an ubuntu jenkins agent, I would install python, pip, etc. I would also set up this, this and this env var, etc”


    I would use Jenkins to run these tests in a CI environment. This would require me to rewrite the tests in a Jenkins compatible library such as pytest. This would be fairly easy to integrate thanks to the nature of docker containers, python environements and shared volumes. 
2. Explain the test approach used in the tech challenge 

    My approach for creating tests for this challenge was two fold: First attempt to add to the database and second verify the expected result within the database. I did this for both my selenium GUI testing as well as my API testing. Looking at the test cases, this methodology is scene. A test attempts to create a new entry in the database by either the API or the GUI web interface. After that another test is executed to verify the expected results of the prior test. I do this because in case of a failure, the location of the defect is easier to find. 

3. What type of infrastructure would you set up in a CI environment to automate ui test cases for mobile applications

    For mobile apps, I would setup Google's Firebase Test Lab to be integrated with a Jenkins instance to ensure that the tests written get run for each new build of the application. This enables support for testing on both iOS and Android with minimal device overhead.