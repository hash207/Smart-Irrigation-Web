import os

output = os.popen("netstat -lpnt | grep :5000").read()

data = output[output.index("N")+7:output.index("/")]
#print(data)
os.popen(f"kill {data}")
