# FSND-Project1-LogAnalysis

#Introduction

This project is to build an internal reporting tool that will use information from the database to discover what kind of articles the a newspaper company website's readers like.

The company's database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The following questions are analyzed by this python program:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#How to run

This project is developed using PostgreSQL v9.5.14 as the database and Python v2.7 for report generation and database connection. Using linux virtual box environment as database server with a database named "news".

To prepare the backend environment:
First we need to load the company's data by running:
```psql -d news -f newsdata.sql```
Then create database views by running:
```psql -d news -f createViews.sql```

Afterwards we can run the program by ```python analyzeResult.py```, and start the logs analysis program and the answers to the 3 questions will be generated.


*This project is created by Vincent Ng for Udacity FullStack Nanodegree course @2019*
