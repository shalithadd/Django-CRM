import mysql.connector


def create_database(database_name="crmdb", host="localhost", user="root", password="pw123"):
  """
  Connects to a MySQL server and creates a database if it doesn't exist.

  Args:
      database_name (str, optional): The name of the database to create. Defaults to "crmdb".
      host (str, optional): The hostname or IP address of the MySQL server. Defaults to "localhost".
      user (str, optional): The username to connect to the MySQL server. Defaults to "root".
      password (str, optional): The password to connect to the MySQL server. Defaults to "pw123".

  Returns:
      None
  """


  try:
      mydb = mysql.connector.connect(
          host=host,
          user=user,
          password=password
      )

      mycursor = mydb.cursor()

      sql = "CREATE DATABASE IF NOT EXISTS {}".format(database_name)
      mycursor.execute(sql)

      mydb.commit()

      print(f"Database '{database_name}' created successfully!")

  except mysql.connector.Error as err:
      print(f"Error creating database: {err}")

  finally:
      if mycursor is not None:
          mycursor.close()
      if mydb is not None:
          mydb.close()

# Example usage with default parameters
create_database()


