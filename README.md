# QA-DevOps-Practical-Project  
This repository contains my deliverable for the QA DevOps practical project.

## Contents:  
*  [Project Brief](#Project-Brief)
*  [Project Planning](#Project-Planning)
*  [App Design](#App-Design)
*  [CI/CD Pipeline](#CI/CD-Pipeline)
*  [Known Issues](#Known-Issues)
*  [Future Work](#Future-Work)

## Project Brief:  
The brief for this project was to produce a service-orientated architecture for a chosen application; this application must be composed of at least 4 services that work together.
The requirements of the project are as follows:
* Kanban board for project tracking
* Git for version control
* Jenkins as a CI server
* Ansible for configuration management
* GCP cloud platform
* Docker as a containerisation tool
* Docker swarm for container orchestration
* NGINX as a reverse proxy  

## Project Planning:
When planning this project, a full risk assessment was undertaken in order to identify hazards associated with this project; this is shown below:

![Risk Assessment](https://github.com/Zaksk/QA-DevOps-Practical-Project/blob/main/Screenshot%202022-04-08%20at%2011.21.20.png)

## App Design:  
In response to this brief, I have chosen to develop a random dish generator. This utilises a microservice architecture as follows:  
* Front-end (service 1): The service with which the user interacts. This service sends requests to the other services to generate random dishes, displays the generated dishes to the user, as well as storing them in a database.
* Country API (service 2): This service receives HTTP GET requests from service 1 and responds with a randomly selected country name chosen from a list of countries using random.choice().
* Prep Time API (service 3): This service receives HTTP GET requests from service 1, and responds with a randomly selected prep tipe chosen from a list, again by random.choice().
* Effect API (service 4): This service receives HTTP POST requests from service 1, which provide the randomly generated country names and prep time as JSON objects, service 4 has two dictionaries which use this data to determine the food name associated with the dish.

In addition to these main services, a reverse proxy using NGINX was implemented; the NGINX service listens to port 80 on the host machine and performs a proxy pass, directing traffic from port 80 on the host to port 5000 on the front-end container, where the app is accessible. The images below show the front-end in action:  

![Front-end](https://github.com/Zaksk/QA-DevOps-Practical-Project/blob/main/Screenshot%202022-04-08%20at%2011.25.26.png)

The dishes generated were stored in a database, the entity diagram (ED) for this is shown below:

![ER-Diagram](https://github.com/Zaksk/QA-DevOps-Practical-Project/blob/main/Screenshot%202022-04-08%20at%2011.31.37.png)


## CI/CD Pipeline:
This project utilises a full CI/CD pipeline to test, build, deploy and maintain the application. The major components of this pipeline are:
* Project tracking
* Version control
* Development environment
* CI server
* Deployment environment  

Project tracking was done using the Project Feature hosted by Github. Every time the task was completed and was pushed to github repo, the issue was automatically closed which was linked to the project. Below are the pictures taken at the start and after completing all the tasks:

![Project-Tracking](https://github.com/Zaksk/QA-DevOps-Fundamental-Project-1/blob/main/Screenshot%202022-04-08%20at%2011.50.40.png)

Git was used for version control, with the repository hosted on github. 

The development environment used was a Ubuntu virtual machine, hosted on GCP, accessed via VSCode. 

Jenkins was used as a CI server. In response to a github webhook Jenkins cloned down the repo and executed the pipeline script defined in the Jenkinsfile. This pipeline consists of 4 main stages: test, build/push, deploy and post-build actions. The test stage executes a bash script which cycles through the directories for the four services and runs unit tests using pytest. The front-end and all API's had unit tests written to test all areas of functionality. Unit testing was used to ensure the back-end of my application was functional and data manipulation in the database was done correctly. Assertions were used to ensure that the correct output was being produced, and requests_mock was used to simulate the interaction of the services. Jenkins will then prints out whether the test succeeded and gave a coverage report noting the percentage of the application that was tested. The results of the tests were archived in HTML format, one for each service and is shown below:

insert pic


If the tests are successful, the build/push stage uses docker-compose to build the images for the different services, logs into docker using credentials configured on the Jenkins VM, and then pushes the images to Dockerhub. The use of a Jenkins pipeline, with this stage-by-stage breakdown, makes optimisation of the project easier. For example, initially all pip installs, for tests and deployment, were done using one requirements file, which meant that testing modules were being installed when building the images; since this was not necessary and since the build/push stage was the longest stage in the pipeline the requirements were separated into a requirements.txt file, containing only the pip installs needed to run the app, and a test_requirements.txt file, which contained all requirements including testing modules. This eliminated unnecessary pip installs during the build stage and reduced the average build/push time.


Successful stages appear green, unstable builds are indicated by yellow stages, and failures are indicated via red stages. If a stage fails, later stages will be skipped, preventing failed versions from being deployed, this can be seen here:  

