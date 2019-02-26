import urllib.request
import time
import os
import datetime
i = 1
times = ["time"]
temps = ["temperature"]
hums = ["humidity"]
table = [times,temps,hums]
p_table = []
while i==1:
    for x in range(3):
        with urllib.request.urlopen('http://192.168.1.187/') as response:
            html = response.read()
        html2 = html.decode("utf-8")
        print(html2)
        time.sleep(20)
    p_table = []
    a,b,c,d,e,f = html2.split("x")
    temps.append(b)
    hums.append(d)
    currentDT = datetime.datetime.now()
    times.append(str(currentDT))
    p_table.append(a)
    p_table.append(b)
    p_table.append(c)
    p_table.append(d)
    p_table.append(e)
    p_table.append("<table style='width:100%'>")
    for x in range(len(temps)):
        p_table.append("<tr>")
        p_table.append("<th>")
        p_table.append(times[x])
        p_table.append("</th>")
        p_table.append("<th>")
        p_table.append(temps[x])
        p_table.append("</th>")
        p_table.append("<th>")
        p_table.append(hums[x])
        p_table.append("</th>")
        p_table.append("</tr>")
    p_table.append("</table>")
    p_table.append(f)
    html3 = ''.join(p_table)
    f = open("index.html","w+")
    f.write(html3)
    f.close()
    os.system("git add .")
    os.system("git commit -m 'hi' ")
    os.system("git push")
    print("60 seconds passed")
