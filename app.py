from flask import Flask
import os
from datetime import datetime
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Kakaraparthi Lokesh Venkata Sai"  
    username = os.getlogin()  
    server_time = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S") 
    top_output = "\n".join([str(proc.info) for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent'])])

    return f"""
    <h1>System Information</h1>
    <p>Name: {full_name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
