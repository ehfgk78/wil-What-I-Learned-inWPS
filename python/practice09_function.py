print('\n'*2)

#1
def color2fruit(color):
    '''
매개변수로 문자열을 받고, 
해당 문자열이 red면 apple을, 
yellow면 banana를,
green이면 melon을, 
어떤 경우도 아닐 경우 I don't know를 리턴하는 함수
    '''
    if color == 'red': return 'apple'
    elif color == 'yellow': return 'banana'
    elif color == 'green': return 'melon'
    else: return "I don't know"


def color2fruit_dict(color):
    '''
매개변수로 문자열을 받고, 
해당 문자열이 red면 apple을, 
yellow면 banana를,
green이면 melon을, 
어떤 경우도 아닐 경우 I don't know를 
dictionay를 이용하여  리턴하는 함수
    '''    
    c2f_dic = {
            'red': 'apple',
            'yellow': 'banana',
            'green': 'melon',            
            }
    return c2f_dic[color] or "I don't know"


def color2fruit_bool(color):
    '''
매개변수로 문자열을 받고, 
해당 문자열이 red면 apple을, 
yellow면 banana를,
green이면 melon을, 
어떤 경우도 아닐 경우 I don't know를 
Bool operation을 이용하여  리턴하는 함수
    '''
    return (color == 'red') * 'apple' + \
           (color == 'yellow') * 'banana' + \
           (color == 'green') * 'melon' or "I don't know"

result = 'yellow'
print(f'''9-1.
{ color2fruit(result) }
{ color2fruit_dict(result) }
{ color2fruit_bool(result) } \n''')


#2.
#print(f'''\n
#9-2.
#{ help(color2fruit) } 
#\n
#{ help(color2fruit_dict) }
#\n
#{ help(color2fruit_bool) }
#\n ''')


#3. 
def mul(x, y=None):
    if y : return x * y
    else : return x ** 2

def mul_arg(*x):
    if len(x) == 1 : return x[0] ** 2
    elif len(x) >= 2 : return x[0] * x[1]
    elif len(x) == 0 : return "숫자를 입력하여 주세요."

print(f'''\n
9-3.
mul(3, 5) = { mul(3, 5) }
vs mul_arg(3,5)  = { mul_arg(3, 5)}
\n
mul(11) = { mul(11) }
vs mul_arg(11) = { mul_arg(11) }
\n''')


#4.
def plus_minus(x, y):
    return x+y, abs(x-y)

print(f'''\n
9-4.
plus_minus(11, 5) : { plus_minus(11, 5) }
\n''')


#5.
def count_args(*args):
    print(len(args))
    return len(args)

#6. lambda, list comprehension : 구구단
li9x9 = [ (lambda x, y: '%d x %d = %d' %(x, y, x*y))(a,b) \
          for a in range(2,10) \
          for b in range(1,10)
        ]
print(f'''\n
9-6.
li9x9= {li9x9}
\n''')


