# import libraries and utlites
from http.server import *
import mysql.connector
import json
import os

# DB connector function
def connectTo(_database) :
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = _database        
    )
    return database

# Handler class for web server
class Server(BaseHTTPRequestHandler) :
    def process(self):
        # Set response headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Acesss-Control-Request-Headers", "X-Requested-With")
        self.send_header("Acesss-Control-Request-Headers", "Content-Type")
        self.end_headers()
        # Initializing databse and setting query executor
        conn = connectTo("passwordManager")
        cursor = conn.cursor()
        # home route
        if self.path.endswith("/") :
            self.wfile.write(bytes("Cannot GET /", "utf-8"))
        # login route
        elif self.path.endswith("/login") :
            # executing query
            cursor.execute("select * from auth")
            # Getting content length to read the http request body from frontend
            content_length = int(self.headers.get("Content-Length"))
            post_body = self.rfile.read(content_length)
            request = json.loads(post_body.decode("utf-8"))
            # Authentication function and condition
            def authenticate(_username, _password) :
                records = cursor.fetchall()[0]
                if _username == records[1] and _password == records[2] :
                    return True
                else :
                    return False
            # Auth logic
            if authenticate(request["user"], request["pass"]) :   
                self.wfile.write(bytes("Success", "utf-8"))
            else :
                self.wfile.write(bytes("Failure", "utf-8"))
        # Dashboard route
        elif self.path.startswith('/getdata') :
            cursor.execute("select * from auth")
            response = cursor.fetchall()
            # writing query results into array to send as a response
            response_array = []
            for i in range(len(response)) :
                response_array.append({
                    "username": response[i][1],
                    "password": response[i][2],
                    "site": response[i][3]
                })
            self.wfile.write(bytes(json.dumps(response_array), "utf-8"))
        # Delete user route
        elif self.path.startswith("/delete") :
            # Getting content length to read the HTTP request body form frontend
            content_length = int(self.headers.get("Content-Length"))
            post_body = self.rfile.read(content_length)
            # Typecasting the post body to integer
            sql_username = json.loads(post_body.decode("utf-8"))["name"]
            # Executing and commiting query
            query = f"DELETE FROM auth WHERE username = '{sql_username}'"
            cursor.execute(query)
            conn.commit()
        # Change password route
        elif self.path.startswith("/changepassword") :
            # Getting content length to read the HTTP request body form frontend
            content_length = int(self.headers.get("Content-Length"))
            post_body = self.rfile.read(content_length)
            # Typecasting the post body to integer
            sql_username = json.loads(post_body.decode("utf-8"))["user"]
            sql_password = json.loads(post_body.decode("utf-8"))["pass"]
            # Executing and commiting query
            query = f"UPDATE auth SET pass = '{sql_password}' WHERE username = '{sql_username}'"
            cursor.execute(query)
            conn.commit()
        # Add new user route
        elif self.path.startswith("/adduser") :
            # Getting content length to read the HTTP request body form frontend
            content_length = int(self.headers.get("Content-Length"))
            post_body = self.rfile.read(content_length)
            # Typecasting the post body to integer
            sql_username = json.loads(post_body.decode("utf-8"))["user"]
            sql_password = json.loads(post_body.decode("utf-8"))["pass"]
            sql_site = json.loads(post_body.decode("utf-8"))["site"]
            # Executing and commiting query
            query = f"INSERT INTO auth (username, pass, site) VALUES ('{sql_username}', '{sql_password}', '{sql_site}')"
            cursor.execute(query)
            conn.commit()
        # Closing DB connection
        conn.close()
    # Various request handlers
    def do_OPTIONS(self) :
        self.send_response(200)
        self.process()
    def do_POST(self) :
        self.send_response(200)
        self.process()
    def do_GET(self) :
        self.send_response(200)
        self.process()
            
            
# Main function
def main() :
    PORT = 3001
    SERVER = HTTPServer(("", PORT), Server)
    print("Serving on {port}".format(port = PORT))
    SERVER.serve_forever()

if __name__ == "__main__" :
    os.system("clear")
    main()