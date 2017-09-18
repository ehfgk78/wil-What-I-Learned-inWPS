multi_lines = '''1. 여러 줄의 텍스트를 
multi_lines 변수에 할당하고,
print()함수로의 출력과 
인터프리터의 자동 출력(변수명 입력)을 비교해보시요.'''

print('''4-1 print() 출력: \n''', multi_lines)
print('''4-1 인터프리터의 자동출력)''')
multi_lines

str1 = "str1, str2변수에 각각 문자열을 할당하고, "
str2 = "두 변수를 결합해 str3변수에 할당해보시오."
str3 = str1 + str2
print(f'''\n 4-2. 
        str1 = {str1}, \n
        str2 = {str2}, \n
        str3 = str1 + str2 = {str3} \n''')

print(f'''4-3. str1 * 3 = \n {str1*3} ''')

