import urllib.request
import time
import os
with urllib.request.urlopen('http://192.168.1.187/') as response:
    i = 1
while i==1:
    html = response.read()
    print(html)
    print("done")
    html2 = html.decode("utf-8")
    print(html2)
    f = open("index.html","w+")
    f.write(html2)
    f.close()
    os.system("git add .")
    os.system("git commit -m 'hi' ")
    os.system("git push")
    time.sleep(60)
    print("60 seconds passed")
