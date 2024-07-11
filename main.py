import mysql.connector
import csv

# MySQL Database connection parameters
db_config_cilantro = {
    "host": "cliantro.cmbrsga0s9bx.me-central-1.rds.amazonaws.com",
    "port": 3306,
    "user": "cilantro",
    "password": "LSQiM7hoW7A3N7",
    "database": "cilantrodb"
}

def fetch_all_users_data():
    connection = mysql.connector.connect(**db_config_cilantro)
    cursor = connection.cursor()

    query = """
    SELECT 
        id AS user_id,
        first_name,
        'test' AS fav_item
    FROM cilantrodb.tbl_user;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data

def write_to_csv(data, filename='user_data.csv'):
    headers = ['user_id', 'first_name', 'fav_item']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            writer.writerow(row)

# Fetch data for all users
all_users_data = fetch_all_users_data()

# Write data to CSV
write_to_csv(all_users_data)

print(f"Data has been written to user_data.csv")