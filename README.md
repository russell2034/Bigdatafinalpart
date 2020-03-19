# Bigdata Final  Project Part 2&3 Combined 

After part 1 of the project we beging by setting up a docker compose with 3 services: ElasticSearch, Kibana, Python Script

After comleting the set up  process we create a script to  push data is taken from NY Open Data Api call  to  Elastic Search 
that can later be queried and further analyzed.

We next test  whether our data was succesffuly loaded by  curling ES several times: 

First try
![](Project_screenshots/ES%20Curl%203.png)
Second Test
![](Project_screenshots/ES%20Curl%202.png)
Control Test
![](Project_screenshots/ES%20Curl%201.png)

After that we configure issue_date to  datetime type to allow Kibana properly index the data that is going to come in:

Then we are ready to analyze our data!



# ANALYSIS

The dashboard was created to  answer specific questions:

![](Project_screenshots/Kibana%201.png)

![](Project_screenshots/Kibana%202.png)

1.  Most popular violation |  Answer:  No standing - bus lane 
2.  Most frequent range of fine amounts | $81-$150
3.  Monthly fine average | To see  whether there is the ongoing tendency
4.  License plate origin( states) with largest number of violations |  Surely NY,  but NJ takes second place. Meaning there 
are probably more people  coming to NY from NJ than from CT.
etc.



