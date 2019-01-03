#! /usr/bin/python

import psycopg2


def create_view(cursor):

	cursor.execute("""drop view log_summary;""")
	cursor.execute("""drop view log_error;""")
	cursor.execute("""drop view authorArts;""")
	cursor.execute("""drop view articlesView;""")
	cursor.execute("""drop view articlesLog;""")

	cursor.execute("""
		create view articlesLog as
		select substring(path from 10) as slug,count(*) as views
		from log
		where path like '/article%'
		group by path
		order by views desc;""")
	cursor.execute("""
		create view articlesView as
		select articles.title, articlesLog.views
		from articles, articlesLog
		where articles.slug=articlesLog.slug;""")
	cursor.execute("""
		create view authorArts as
		select authors.name, articles.title
		from authors,articles
		where articles.author=authors.id;""")
	cursor.execute("""
		create view log_summary as
		select to_char(time,'Month DD,YYYY') as date, count(*)
		from log
		group by date;""")
	cursor.execute("""
		create view log_error as
		select to_char(time,'Month DD,YYYY') as date, count(*)
		from log
		where status like '4%'
		group by date;""")


def Q1_ans(cursor):
	print("----------------------------------------------------------")
	print("1. What are the most popular three articles of all time?\n")
	cursor.execute("""
		select * from articlesView;""")
	result = cursor.fetchall()
	for title, views in result:
		print("\"{}\" -- {} views".format(title, views))


def Q2_ans(cursor):
	print("----------------------------------------------------------")
	print("2. Who are the most popular article authors of all time?\n")
	cursor.execute("""
		select authorArts.name, articlesView.views
		from authorArts,articlesView
		where authorArts.title=articlesView.title;""")
	result = cursor.fetchall()
	for author, views in result:
		print("{} -- {} views".format(author, views))


def Q3_ans(cursor):
	print("----------------------------------------------------------")
	print("""3. On which days did more than 1% of requests lead to errors?"""+'\n')

	cursor.execute("""
		select date, error_rate
		from (select log_error.date,
			((log_error.count::float)*100/log_summary.count::float)::numeric(2,1) as error_rate
			from log_error,log_summary
			where log_error.date=log_summary.date) as result
		where error_rate>1.0;""")
	result = cursor.fetchall()
	for date, error in result:
		temp_date = date.split()
		print('%s -- %s%% errors \n' % (temp_date[0]+" "+temp_date[1], error))


if __name__ == '__main__':
	con = psycopg2.connect("dbname=news")
	cursor = con.cursor()
	#  This function only need to run for the first time
	#  for adding views to database
	create_view(cursor)
	Q1_ans(cursor)
	Q2_ans(cursor)
	Q3_ans(cursor)
	con.close()



