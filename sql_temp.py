import sqlite3

# Connect database temperature
conn = sqlite3.connect('temperature.db')
sql = conn.cursor()

# Create table Southern_cities and drop if exists
sql.execute('drop table if exists Southern_cities;')
sql.execute("""create table Southern_cities(city text, country text, latitude text, longitude text)""")

# List distinctive major cities located in southern hemisphere
sql.execute("""select distinct city, country, latitude, longitude
from GlobalTemperatureByMajorCity where latitude LIKE '%S' order by country""");
results = sql.fetchall()

# Import southern city information from table 'GlobalTemperatureByMajorCity' to 'Southern_cities'
for row in results:
    print('| %20s | %20s | %20s | %20s |' % row)
    sql.execute('insert into Southern_cities values("{city}", "{country}","{latitude}","{longitude}");'.format(
        city=row[0], country=row[1], latitude=row[2], longitude=row[3]
    ))
conn.commit()


"""sql.execute('select * from Southern_cities;')
result = sql.fetchall()
for r in result:
    print('| %20s | %20s | %20s | %20s |' % r)"""


# Query table GlobalTemperatureByState
sql.execute("""select max(AverageTemperature), min(AverageTemperature), avg(AverageTemperature) from GlobalTemperatureByState 
where state = 'Queensland' and date like '2000%' """);
result = sql.fetchall()
for r in result:
    print(r)








