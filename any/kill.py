import os

output = os.popen("netstat -lpnt | grep :5000").read()

data = output[-21:-17]
#print(data)
os.popen(f"kill {data}")
