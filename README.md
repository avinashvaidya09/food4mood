#### Reference - 
 1. https://blogs.sap.com/2018/07/05/writing-and-modifying-data-using-rest-apis-with-python-on-xsa/
 2. https://developers.sap.com/tutorials/btp-cf-buildpacks-python-create.html - Follow this mission to understand how to deploy python app on cf
 3. https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f
 4. https://blogs.sap.com/2018/07/05/writing-and-modifying-data-using-rest-apis-with-python-on-xsa/
 5. https://betterprogramming.pub/10-best-practices-for-naming-rest-api-endpoints-442ae592a3a0

#### Commands used
1. cf login - To login to cloud foundry
2. cf create-service hana hdi-shared healthyhabits - To create hana db instance and service
3. cf logs --recent foodformoodapp - command to check latest logs

#### SQL Used for database

Refer - dbqueries.sql

#### Python env and packages

- To specify python run time, add it in runtime.txt
- To import any python packages, add it in requirements.txt