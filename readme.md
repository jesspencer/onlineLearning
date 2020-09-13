# Future of Online Learning Dashboard
This project includes a python etl pipeline script for loading and cleaning the world bank .xslx file data downloaded at [worldbanksite](https://datacatalog.worldbank.org/dataset/world-development-indicators).
The python script is a data cleaning script and it uses a configuration json file, which is also included. The data in this project was used to create two Future of Online Learning Dashboards. The first dashboard displays the trends in online learning by region and country. While the second dashboard shows the future demand for online learning. The user is then able to go back and forth from the first and second dashboard with navigation buttons. Also, the users is able to filter each visual by color, region, and country name.  The dashboard itself can be viewed on the Tableau Pulblic website [here](https://public.tableau.com/profile/jessica.spencer6802#!/vizhome/FutureofOnlineLearning_15992334579770/OnlineLearning/)

## Code:
* 1. Python script used to clean the data prior to using the data in Tableau. 
* 2. The script takes the .csv file downloaded from world bank data indicators site, cleans it using pandas, and re-saves the file as "Revised" Excel file.   

## REQUIREMENTS
- python 3.7
- pandas (python library) 
- tableau 2019.3
- tableau public account
- internet 

## RUNNING DOCUMENTATION LOCALLY:
1. Clone the project https://github.com/jesspencer/onlineLearning.git
2. cd onlineLearning

## BUGS AND FEATURE REQUESTS
Have a bug or a feature request? Please open an [issue](https://github.com/jesspencer/onlineLearning/issues/new).


## CREATOR
**Jessica Spencer**
- onlineLearning.com/jesspencer
- twitter.com/js13142
- linkedin.com/in/spenje/
