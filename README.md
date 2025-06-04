# Dental Office Call System

This project provides a simple web based communication tool for operatories in a dental office. Stations can call for a doctor or assistant, clear individual calls or clear all calls.

## Requirements
- Python 3.8+
- `flask`, `flask-socketio`, `eventlet`

Install dependencies:
```bash
pip install flask flask-socketio eventlet
```

## Running
Start the server:
```bash
python server.py
```
The server listens on port `5000`.

Open the client in a web browser, passing a station name via the `station` query parameter. Example for `Op 1`:
```
http://localhost:5000/?station=Op%201
```
Open the page in multiple tabs or machines with different station names to simulate multiple stations.

## Usage
- **Call Doctor** or **Call Assistant** broadcasts a request to all stations showing the origin and elapsed time.
- After 5 minutes the request will chime and flash every 5 minutes until cleared.
- **Clear** removes all calls originating from the current station.
- **All Clear** clears every call when the button is held for 3 seconds.
