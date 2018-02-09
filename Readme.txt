Requirement:
# Run python3 (按顺序依次运行：db_create.py, sql_temp.py, excel_temp.py, numpy_temp.py) in terminal(终端).
1.Run 'db_create.py' to
    - Open the excel files,
    - Create a SQLite database with three tables,
    - Import data from the excel files to the corresponding tables in the database.

2. Run 'sql_temp.py' to query the database
    - Print distinctive major cities located in southern hemisphere ordered by country,
    - Write their name, country, and geo-location into a new table called “Southern cities”,
    - Print maximum, minimum and average temperature of Queensland for year 2000 and print this information to the CONSOLE.

3. Run 'excel_temp.py' to
    - Create a new workbook named “World Temperature.xlsx”.
    - Create a sheet named “Temperature by city”.
    - Calculate the yearly mean temperature of each city in China (Contain some missing data).
    - Write the relevant data into the worksheet you created.
    - Generate a line chart for the above data.

4. Run 'numpy_temp.py' to
    - Open the World Temperature workbook,
    - Create another sheet called “Comparison”,
    - Calculate mean yearly temperature of Australian states,
    - Calculate mean yearly temperature of Australia,
    - Calculate yearly differences between each state and the national data,
    - Use MatPlotLib to plot the difference across years,
    - Write the data into the sheet.

