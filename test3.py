import urllib.request
import time
import os
i = 1
times = ["time"]
temps = ["temperature"]
hums = ["humidity"]
table = [times,temps,hums]
while i==1:
    for x in range(3):
        with urllib.request.urlopen('http://192.168.1.187/') as response:
            html = response.read()
        html2 = html.decode("utf-8")
        print(html2)
        time.sleep(20)
    a,b,c,d,e,f = html2.split("x")
    temps.append(b)
    hums.append(d)
    html3 = ''.join([a,b,c,d,e,f])
    f = open("index.html","w+")
    f.write(html3)
    f.close()
    os.system("git add .")
    os.system("git commit -m 'hi' ")
    os.system("git push")
    print("60 seconds passed")
