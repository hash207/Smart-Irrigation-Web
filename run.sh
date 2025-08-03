# Activate the virtual environment
source smart_venv/bin/activate

# Start the Flask app in the background
python3 "Web app/main.py" &

# Wait a few seconds for Flask to start
sleep 3

# Start ngrok tunnel
python3 any/start_ngrok.py

# End working in background
python3 any/kill.py
