print("\n"*3)

#1. 
print('''8-1. 중첩 for 문 
for i in range(7):
    for j in range(4):
        t = i, j
        print(t, end= "   ")

ans8-1) 
        ''') 

for i in range(7):
    for j in range(4):
        t = i, j
        print(t, end= "   ")


#2.
ans2 = [ (i, j) for i in range(7) for j in range(4) ]
print(f'''\n8-2. List Comprehension
[ (i, j) for i in range(7) for j in range(4) ]
{ans2}
\n ''')


#3.
print('''8-3-1.
for i in range(0, 7, 2):
    for j in range(4):
        t = i, j
        print(t, end= "  *  ")
ans)))
        ''')
for i in range(0, 7, 2):
    for j in range(4):
        t = i, j
        print(t, end= ",   ")

ans3= [ (i, j) for i in range(7) for j in range(4) if i % 2 == 0]
print(f'''\n
8-3-2.
ans3= [ (i, j) for i in range(7) for j in range(4) if i % 2 == 0]
{ans3} \n      
''')


#4.
sum = 0
for i in range(1001, 2000, 2):
    sum += i
print(f"8-4. sum= {sum} \n")


#5. 
li5 = ['%d x %d = %d' %(i, j, i*j) \
        for i in range(2, 10) \
        for j in range(1, 10) ]
print(f'''8-5. 구구단 결과 by List Comprehension
        {li5}
        ''')
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
        if j == 9: 
            print('\n')


#6.
li6 = [ i for i in range(1, 100) if i % 7 == 0 or i % 9 == 0 ]
print(f'''8-6.
{li6}''')










