import os
import re

output = os.popen("netstat -lpnt | grep :5000").read()

try:
    data = ''.join(re.findall('\d', output[output.index("N")+1:]))
    os.popen(f"kill {data}")
    print("operation termenated succesfully")
except ValueError:
    print("Operation did not termenat succeafully")
