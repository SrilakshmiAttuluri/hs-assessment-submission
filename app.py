from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask,request
from mysql.connector import Error
from mysql.connector import pooling
import os

app = Flask(__name__)

@app.route("/healthz")
def health():
    return "Hunger Station Health is up and running"

@app.route("/")
def hello():
    return "Welcome to Hunger Station!"


@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('Username')
    password = request.args.get('Password')
    try:
      connection_pool = pooling.MySQLConnectionPool(pool_name="hs_pool",
                                                  pool_size=5,
                                                  pool_reset_session=True,
                                                  host='db',
                                                  database=os.env('MYSQL_DATABASE'),
                                                  user=os.env('MYSQL_USER'),
                                                  password=os.env('MYSQL_ROOT_PASSWORD'),
                                                  auth_plugin='mysql_native_password')
      print("Printing connection pool properties ")
      print("Connection Pool Name - ", connection_pool.pool_name)
      print("Connection Pool Size - ", connection_pool.pool_size)

      # Get connection object from a pool
      connection_object = connection_pool.get_connection()

      if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)

        cursor = connection_object.cursor()
        cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
        record = cursor.fetchone()
        if record is None:
            return "Username or Password is wrong"
        else:
            return "Logged in successfully"
    except Error as e:
      print("Error while connecting to MySQL using Connection pool ", e)
    finally:
      # closing database connection.
      if connection_object.is_connected():
         cursor.close()
         connection_object.close()
         print("MySQL connection is closed")

if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
