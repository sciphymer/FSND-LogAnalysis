#! /usr/bin/python

import psycopg2


def Q1_ans(cursor):

    print("----------------------------------------------------------")
    print("1. What are the most popular three articles of all time?\n")
    cursor.execute("""
        select * from articlesView limit 3;""")
    result = cursor.fetchall()
    for title, views in result:
        print("\"{}\" -- {} views".format(title, views))


def Q2_ans(cursor):

    print("----------------------------------------------------------")
    print("2. Who are the most popular article authors of all time?\n")
    cursor.execute("""
        select authorArts.name as name, sum(articlesView.views) as views
        from authorArts,articlesView
        where authorArts.title=articlesView.title
        group by authorArts.name
        order by views desc; """)
    result = cursor.fetchall()
    for author, views in result:
        print("{} -- {} views".format(author, views))


def Q3_ans(cursor):

    print("----------------------------------------------------------")
    print("""3. On which days did more than 1% of requests lead to errors?""")
    print("")
    cursor.execute("""
        select to_char(date,'Month DD,YYYY'), error_rate::numeric(2,1)
        from (select log_error.date,
            log_error.count*100.0/log_summary.count as error_rate
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
    Q1_ans(cursor)
    Q2_ans(cursor)
    Q3_ans(cursor)
    con.close()
