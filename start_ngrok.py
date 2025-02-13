
from pyngrok import ngrok

# Start ngrok tunnel
url = ngrok.connect(5000)
print(f'Ngrok tunnel is running at: {url}')

# Keep the tunnel open
ngrok_process = ngrok.get_ngrok_process()
try:
    ngrok_process.proc.wait()
except KeyboardInterrupt:
    print("Shutting down tunnel...")
    ngrok.kill()
