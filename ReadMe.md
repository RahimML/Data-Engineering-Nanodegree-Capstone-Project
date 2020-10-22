# Introduction
No one likes flight cancellation nor delays. This project will help answering many questions regarding flight cancellations and the reasons behind it and how common there are. This project contains two data sources, the first is the 2015 Flight Delays and Cancellations and U.S. City Demographic Data.

# Data sources
2015 Flight Delays and Cancellations:
The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled, and diverted flights is published in DOT's monthly Air Travel Consumer Report and in this dataset of 2015 flight delays and cancellations.
Includes three datasets:
airlines.csv: IATA airline codes and names.
airports.csv: IATA airport codes, names, cities and states.
flights.csv: includes all the information about the flights.

U.S. City Demographic Data:
This dataset contains information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000. 
This data comes from the US Census Bureau's 2015 American Community Survey.
Includes one data set:
us-cities-demographics.csv: cities names, states, population, median age and race. 

# Project's Scope
The scope of the project is to stage the dataset into Redshift from S3 bucket. Loading tables, running quality checks. The dataset has been uploaded to an S3 bucket. The objective of implementing this project is to help people find out which airline has lowest number of delays and cancellation. Also, data scientists can benefit from this project, as they can find a relationship between flight cancellations and delays and cities demographic data. An example to illustrate that is going to be this list of questions:
What is the relationship between the city population and number of flights cancelled?
What airport has the highest number of flight delays?

# Schema design
The schema of this project includes four tables. One fact table, three dimensional tables as follows:
Flights:
airline: The airline IATA code.
FLIGHT_NUMBER: Flight Identifier.
ORIGIN_AIRPORT: Departure Airport.
DESTINATION_AIRPORT: Destination Airport.
Month: the month of the flight.
day: day of the flight.
DAY_OF_WEEK: the day of the week of the flight.
SCHEDULED_DEPARTURE: the scheduled time of flight departure.
DEPARTURE_DELAY: the amount of delay.
CANCELLED: Cancelled or not? 1 if yes.
CANCELLATION_REASON: Reason for Cancellation of flight:
A - Airline/Carrier; B - Weather; C - National Air System; D - Security.

Airlines: 
IATA_CODE: the IATA code of the airline.
Airline: the name of the airline.
number_of_flights: the total number of the flights during 2015.

Airports:
IATA_CODE: the IATA code of the airline.
AIRPORT: the name of the airport.
CITY: city name.
depatured_flights: the of departure flights during 2015.
arrived_flights: the of arrived flights during 2015.

Cities:
CITY: city name.
state_code: State code.
median_age: the median age in the city.
total_population: total population.

# Technologies
the used technologies in this project are :
Airflow: it has been use because of its powerful capability of handling large datasets.
Amazon Web Services: it has been used due the need of cloud storage and Redshift.

# Other Scenarios
The data was increased by 100x: It possible to be 100x if the database included large amount of flights data. we can modify the sittings of Redshift to handle this scenario.
The pipelines would be run on a daily basis by 7 am every day: The DAG can be scheduled to run @daily and if something wrong happened Airflow SLA will notify the user.
The database needed to be accessed by 100+ people: By the help of AWS Redshift more than 100 users can access the database.

# Resources
Links to the data sources:
1. 2015 Flight Delays and Cancellations: 
https://www.kaggle.com/usdot/flight-delays/data#airports.csv
2. U.S. City Demographic Data:
https://public.opendatasoft.com/explore/dataset/us-cities-demographics/information/

