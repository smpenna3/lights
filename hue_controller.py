from flask import Flask, render_template
from flask.socketio import SocketIO

# Setup flask app
app = Flask()
socket = SocketIO(app)

@app.route('/'):
def home():
	return render_template('index.html')

if __name__ == '__main__':
	socket.run(host=0.0.0.0, port='6600', debug=True)
