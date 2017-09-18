color_en = 'red', 'green', 'blue', 'yellow', 'black', 'white',
color_ko = '빨강', '연두', '파랑', '노랑', '검정', '하양',
colors = dict(zip(color_en, color_ko))

print(f'''6-1. 
color_en = 'red', 'green', 'blue', 'yellow', 'black', 'white',
color_ko = '빨강', '연두', '파랑', '노랑', '검정', '하양',

colors = dict(zip(color_en, color_ko))
colors = {colors} \n''')

ans2 = colors['blue']
print(f'''6-2.
        colors['blue'] = {ans2} \n''')

colors_set = set(colors)
print(f'''6-3.
colors_set = set(colors)
{colors_set} \n''')

is_purple_in_colors_set = ( 'purple' in colors_set )
print(f"6-4. ans = {is_purple_in_colors_set} \n")

li5 = [2,4,3,7,6,8,4,6,5,3,2,5,6,7,3]
ans5 = sorted( list( set(li5) ) )
print(f"6-5. ans = {ans5} \n")

lol = {
        'champions' : {'lux', 'ahri', 'ezreal'},
        'items' : [{ 'Doran Ring': 400,
            'Doran Blade': 450}]
        }
print(f'''6-6. lol =
        {lol} \n''')


x = {1,2,3,4,5,6,8}
y = {4,5,6,9,10,11}
z = {4,6,8,9,7,10,12}

xyz_intersection = x & y & z
yz_not_x = y & z - x
only_x = x - y - z
print(f'''6-7. 
* x, y , z 교집합에 해당하는 숫자: {xyz_intersection}
* y, z의 교집합이며 x에 속하지 않는 숫자: {yz_not_x}
* x에만 속하고 y, z에는 속하지 않는 숫자: {only_x}''')





