source smart_venv/bin/activate
nohup python3 "Web app/main.py" &  ngrok http --url=starfish-regular-lightly.ngrok-free.app 5000
