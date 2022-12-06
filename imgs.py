root='swswshwbx'

print(root.find('x'))
name = 'Gumby'
names = ['gumby', 'smith', 'jones']
if name.lower in names: print('Found it!') 
else :print('333')

names ='bewenx23'
for  name  in names : print(name.split())

ros ='323252s2'


xs='22'
ss='222'
if(xs is ss) :
    print('sss')
elif( xs is not ss):
    print("ws")

x=1
while x<=100:
    print(x)
    x+=1
d = {'x': 1, 'y': 2, 'z': 3}


for key in d:
    print(key ,'as',d[key])

for key, value in d.items():
 print(key, 'corresponds to', value)    

for x in xs:
    print(x)
fibs = [0, 1]
for i in range(8):
 fibs.append(fibs[-2] + fibs[-1])

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: ')) 

try:
 x = int(input('Enter the first number: '))
 y = int(input('Enter the second number: '))
 print(x / y)
except ZeroDivisionError:
 print("The second number can't be zero!")