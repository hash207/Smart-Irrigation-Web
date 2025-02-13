from pyngrok import ngrok, conf
import os

# Configure ngrok
home_dir = os.path.expanduser("~")
ngrok_path = os.path.join(home_dir, "ngrok_bin")
os.makedirs(ngrok_path, exist_ok=True)
conf.get_default().ngrok_path = os.path.join(ngrok_path, "ngrok")

# Set auth token
auth_token = os.environ["NGROK_AUTH_TOKEN"]
if not auth_token:
    raise Exception("Please set NGROK_AUTH_TOKEN in Replit Secrets")
ngrok.set_auth_token(auth_token)

# Start ngrok tunnel with static domain
url = ngrok.connect(5000, hostname="starfish-regular-lightly.ngrok-free.app")
print(f'Ngrok tunnel is running at: {url}')

# Keep the tunnel open
ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down tunnel...")
    ngrok.kill()
