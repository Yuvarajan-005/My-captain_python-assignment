import csv
n = []
a = []
c = []
e= []
while True:
    print("Enter Name Age Contact_number e-mail_address")
    s = list(map(str,input().split()))
    n.append(s[0])
    a.append(s[1])
    c.append(s[2])
    e.append(s[3])
    print("Do you want to add another record ?[Y/n]")
    k = input()
    if k=='n':
        break
f = open('student.csv','a',newline = '')
w = csv.writer(f)
w.writerow(["Name","Age","Contact Number","E-Mail"])
for i in range(len(n)):
    w.writerow([n[i],a[i],c[i],e[i]])
f.close()