create or replace view articlesLog as
		select path,count(*) as views
		from log
		where path like '/article%'
		group by path
		order by views desc;

create or replace view articlesView as
		select articles.title, articlesLog.views
		from articles, articlesLog
		where articles.slug=substring(articlesLog.path from 10);

create or replace view authorArts as
		select authors.name, articles.title
		from authors,articles
		where articles.author=authors.id;

create or replace view log_summary as
		select time::date as date, count(*)
		from log
		group by date;

create or replace view log_error asd
		select time::date as date, count(*)
		from log
		where status like '4%'
		group by date;