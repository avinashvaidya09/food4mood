## About this file

### This file contains reference to all the technical details used to create this project and also information about the project set up

#### Environment configuration, python runtime and packages

1. The application configuration is maintained in manifest.yml
2. To specify python run time, add it in runtime.txt
3. To import any python packages, add it in requirements.txt

#### Cloud foundry commands used
1. cf login - To login to cloud foundry
2. cf create-service hana hdi-shared healthyhabits - To create hana db instance and service
3. cf logs --recent foodformoodapp - command to check latest logs

#### SQL Used for database

1. healthyhabits - database is created in HANA
2. Refer - dbqueries.sql

#### Reference - 
 1. https://blogs.sap.com/2018/07/05/writing-and-modifying-data-using-rest-apis-with-python-on-xsa/
 2. https://developers.sap.com/tutorials/btp-cf-buildpacks-python-create.html - Follow this mission to understand how to deploy python app on cf
 3. https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
 4. https://blogs.sap.com/2018/07/05/writing-and-modifying-data-using-rest-apis-with-python-on-xsa/
 5. https://betterprogramming.pub/10-best-practices-for-naming-rest-api-endpoints-442ae592a3a0