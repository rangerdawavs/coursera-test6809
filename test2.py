import urllib.request
import time
import os
i = 1
while i==1:
    for x in range(3):
        with urllib.request.urlopen('http://192.168.1.187/') as response:
            html = response.read()
        html2 = html.decode("utf-8")
        print(html2)
        f = open("index.html","w+")
        f.write(html2)
        f.close()
        time.sleep(20)
    os.system("git add .")
    os.system("git commit -m 'hi' ")
    os.system("git push")
    print("60 seconds passed")
