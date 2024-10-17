import os

output = os.popen("netstat -lpnt | grep :5000").read()

data = output[-21:-16]

os.popen(f"kill {data}")
