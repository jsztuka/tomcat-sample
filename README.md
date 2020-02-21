# Tomcat server sample app hosting
A very basic structure for hosting sample application on tomcat application server.

# Prerequisities
1. Docker is installed on the machine
2. Ansible is installed on the machine
3. Python/Pytest is installed on the machine
4. Port 8080 is available

# Steps
* Clone git repo to your local repository
* Run ansible playbook with predefined hosts file : sudo ansible-playbook -i hosts main.yml
* All done - application should be hosted on http://localhost:8080/sample


# Description

* Folder /docker contains Dockerfile and sample app (sample.war).
* File hosts contains localhost address - our app destination.
* File main.yml is playbook containing complete server deployment procedure.
* File test-avialability.py checks if our app is up and running at desired address.

# Main.yml structure

* Ansible first checks via pytest if our app is currently up and running, and if yes, skip whole process.
* If our application is not running at http://localhost:8080/sample, first docker image is build, then run at localhost:8080.
* After that pytest check runs again to make sure that app is up and running.
