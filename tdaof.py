import mysql.connector
import csv
import os
import sys
from tqdm import tqdm

art = '''
 ______  __  __  __  ______  __  __                                   
/\  __ \/\ \/\ \/\ \/\  ___\/\ \/ /                                   
\ \ \/\_\ \ \_\ \ \ \ \ \___\ \  _"-.                                 
 \ \___\_\ \_____\ \_\ \_____\ \_\ \_\                                
  \/___/_/\/_____/\/_/\/_____/\/_/\/_/                                
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
 ______  __  __  ______       _____   ______  ______  ______          
/\__  _\/\ \_\ \/\  ___\     /\  __-./\  __ \/\__  _\/\  __ \         
\/_/\ \/\ \  __ \ \  __\     \ \ \/\ \ \  __ \/_/\ \/\ \  __ \        
   \ \_\ \ \_\ \_\ \_____\    \ \____-\ \_\ \_\ \ \_\ \ \_\ \_\       
    \/_/  \/_/\/_/\/_____/     \/____/ \/_/\/_/  \/_/  \/_/\/_/       
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
 __  ______       ______  __   __       ______  __  ______  ______    
/\ \/\  ___\     /\  __ \/\ "-.\ \     /\  ___\/\ \/\  == \/\  ___\   
\ \ \ \___  \    \ \ \/\ \ \ \-.  \    \ \  __\\ \ \ \  __<\ \  __\   
 \ \_\/\_____\    \ \_____\ \_\\"\_\    \ \_\   \ \_\ \_\ \_\ \_____\ 
  \/_/\/_____/     \/_____/\/_/ \/_/     \/_/    \/_/\/_/ /_/\/_____/ 
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
 __     __  ______       __    __  __  __  ______  ______             
/\ \  _ \ \/\  ___\     /\ "-./  \/\ \/\ \/\  ___\/\__  _\            
\ \ \/ ".\ \ \  __\     \ \ \-./\ \ \ \_\ \ \___  \/_/\ \/            
 \ \__/".~\_\ \_____\    \ \_\ \ \_\ \_____\/\_____\ \ \_\            
  \/_/   \/_/\/_____/     \/_/  \/_/\/_____/\/_____/  \/_/            
                                                                      
                                                                      
                                                                      
                                                                      
                                                                      
 ______  ______  ______     __  ______     ______  __  __  ______     
/\  ___\/\  ___\/\__  _\   /\ \/\__  _\   /\  __ \/\ \/\ \/\__  _\    
\ \ \__ \ \  __\\/_/\ \/   \ \ \/_/\ \/   \ \ \/\ \ \ \_\ \/_/\ \/    
 \ \_____\ \_____\ \ \_\    \ \_\ \ \_\    \ \_____\ \_____\ \ \_\    
  \/_____/\/_____/  \/_/     \/_/  \/_/     \/_____/\/_____/  \/_/    
                                                                      
'''

print(art)                                                                    
                                                                      
  

# Function to export a table to a CSV file
def export_table_to_csv(cursor, table_name):
    # Execute a SELECT query to get all the data in the table
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()

    # Get the column names from the cursor description
    column_names = [description[0] for description in cursor.description]

    # Create a CSV file with the table name and write the data to it
    file_name = f"{table_name}.csv"
    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(data)

    print(f"{table_name} exported to {file_name}")

# Get command line arguments
if len(sys.argv) != 4:
    print("Usage: python export_tables.py <database_name> <mysql_user> <mysql_password>")
    sys.exit(1)

database_name = sys.argv[1]
mysql_user = sys.argv[2]
mysql_password = sys.argv[3]

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user=mysql_user,
    password=mysql_password,
    database=database_name
)

cursor = connection.cursor()

# Get a list of all the tables in the database
cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]

# Export each table to a CSV file
for table in tqdm(tables):
    export_table_to_csv(cursor, table)

# Close the cursor and connection
cursor.close()
connection.close()


#pip install tqdm
#python export_tables.py <database_name> <mysql_user> <mysql_password>


