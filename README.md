### Amazon Vehicle Parts crawler with request solution

# Install [python](https://www.python.org/downloads/)
# Install dependency
1. run `CTRL + R` to open **cmd.exe**
1. run `pip install -r requests.txt` in **cmd.exe**
1. run `pyhton db.py` to dump data to csv format in **cmd.exe**
# start to crawler data
1. modify `inputs.py` to edit `Amazon` and year `infor`
1. run `pyhton crawler.py` to crawler car parts in **cmd.exe**
1. run `pyhton fits.py` to update car fits info in **cmd.exe**

# error & debug
# other
1. online view data: https://sqliteviewer.app/
1. sqlite3 convert to csv: https://www.rebasedata.com/convert-sqlite-to-csv-online
1. sqlite3 op:

```shell
sqlite3 data.db
.schema parts;
select * from parts;
select * from parts where fit is not null;
select asin, year,fit,count(*) as c from parts group by asin,year,fit order by c desc;
select asin, year,fit,count(*) as c from parts group by asin,year,fit order by year desc;
select asin, year,fit,count(*) as c from parts where asin='B098DWSXT2' group by asin,year,fit order by year desc;
.exit

```
