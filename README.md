# FSND-Project1-LogAnalysis

#Introduction

This project is to build an internal reporting tool that will use information from the database to discover what kind of articles the a newspaper company website's readers like.

The company's database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.

The following questions are analyzed by this python program:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#Dependencies:
This project is developed using:
- PostgreSQL v9.5.14
- Python v2.7
- Vagrant v1.8.1
- Virtual Box v5.1.34

#How to run

##Linux Virtual Machine:
A linux server is need to run the DataBase and Python project. If you don't have a linux OS, you can use Linux-based virtual machine (VM) instead.
The VM can be setup by installing:
- Vagrant: https://www.vagrantup.com/downloads.html
- Virtual Box: https://www.virtualbox.org/wiki/Downloads
After installing, copy the Vagrantfile (a vagrant configuration file) from the project to your local pc, access it's directory through command line.
Then use `vagrant up`, the VM environment will be setup for you automatically. After finished the setup, you can `vagrant ssh` to connect to the VM started on the virtual box. The login name and password are both "vagrant".
The linux environment setup using VagrantFile already included the tools of PostgreSQL, Python and also create a database named "news" automatically.

##Prepare the backend environment:
In the linux VM program directory, before we run the data analyze program, firstly we need to load the company's data to the "news" database by running:
```psql -d news -f newsdata.sql```
Then create database views by running:
```psql -d news -f createViews.sql```

Afterwards we can run the program by ```python analyzeResult.py```, and start the logs analysis program and the answers to the 3 questions will be generated.
You can find the expect result in the output.txt.

Hope you enjoy this project!

*This project is created by Vincent Ng for Udacity FullStack Nanodegree course @2019*
