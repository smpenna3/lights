from flask import Flask, render_template
from flask.socketio import SocketIO
import fade

# Setup flask app
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
	return render_template('index.html')

@socketio.on('fade', namespace='/channel')
def fade_routine():
	fade.fadeSingleLoop(10, 1000)

if __name__ == '__main__':
	socketio.run(host='0.0.0.0', port='6600', debug=True, use_reloader=False)