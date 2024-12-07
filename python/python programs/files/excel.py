import csv 
with open('emp.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Eid','Ename','Ephno','Eadd'])
    n = int(input('enter number of empolyees:'))
    for i in range (n):
        Eid=input('enter employee id:')
        Ename=input('enter employee name:')
        Ephno=input('enter employee phno:')
        Eadd=input('enter employee address:')
        w.writerow([Eid,Ename,Ephno,Eadd])
    print('total employyee data to csv file')