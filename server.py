from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO
import uuid
import time

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

calls = {}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@socketio.on('connect')
def handle_connect():
    socketio.emit('init', {'calls': [v for v in calls.values()]}, to=request.sid)

@socketio.on('call')
def handle_call(data):
    call_id = str(uuid.uuid4())
    calls[call_id] = {
        'id': call_id,
        'station': data['station'],
        'type': data['type'],
        'time': time.time()
    }
    socketio.emit('call', calls[call_id])

@socketio.on('clear')
def handle_clear(data):
    # remove calls from this station
    ids = [cid for cid, c in calls.items() if c['station'] == data['station']]
    for cid in ids:
        del calls[cid]
        socketio.emit('clear', cid)

@socketio.on('clear_all')
def handle_clear_all(data):
    calls.clear()
    socketio.emit('clear_all')

if __name__ == '__main__':
    print('Starting server on http://0.0.0.0:5000')
    socketio.run(app, host='0.0.0.0', port=5000)
