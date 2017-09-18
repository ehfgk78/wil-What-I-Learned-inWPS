str = 'Fastcampus'
string2list = list(str)
string2tuple = tuple(str) 

print(f'''5-1.
         str = 'Fastcampus'
         string2list = list(str)
         {string2list} \n
         string2tuple = tuple(str)
         {string2tuple}''')


list2string = ''.join(string2list)
tuple2string = ''.join(string2tuple)

print(f'''
list2string = ''.join(string2list)
{list2string} \n
tuple2string = ''.join(string2tuple)
{tuple2string} \n ''')


