# FSND-Project1-LogAnalysis

#Introduction

This project is to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. 
Data is prepared as "newsdata.sql" and pre-loaded to a linux virtual box environment with database named "news".
This project is developed using PostgreSQL v9.5.14 as the database and Python v2.7 for report generation and database connection.

The following questions are analyzed by this python program:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

#How to run
On the local Database which contains the newsdata.sql, just run by ```python analyzeResult.py``` .
In the python __main___, function ```create_view()``` only need to run for the first time for creating views in the database. 
Inside the function, ```drop views``` are added before the view creation, there will not have any errors if keeping the line of code uncomment.
But for not duplicate running, after the first time, it can be commented.  

This project is created by Vincent Ng for Udacity FullStack Nanodegree course @2019
