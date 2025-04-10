from flask import Flask, Response
import subprocess
import datetime
import getpass
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Saketh Ram"  # Replace with your full name
    user = getpass.getuser()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f")

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    output = f"""Name: {name}
Username: {user}
Server Time (IST): {server_time}
TOP output:

{top_output}
"""
    return Response(output, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
