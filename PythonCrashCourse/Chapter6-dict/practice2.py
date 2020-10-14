python_dict = {
    'print':'输出',
    'variable':'变量',
    'if':'条件判断',
    'else':'用在if之后',
    'len()':'输出列表的长度'
}

# 遍历dict的时候，使用items()，keys()，values()来遍历所有的项目或者所有的键或值
for n,v in python_dict.items():
    print(f'{n.title()} meaning {v} in python!')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'bob': 'python'
    }

list_people = ['jen','bob','edward']

for name in favorite_languages.keys():
    if name in list_people:
        print('Thanks.')
    else:
        print('Please take the survey.')