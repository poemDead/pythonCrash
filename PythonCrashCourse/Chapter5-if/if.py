alien_color = 'green'

if alien_color=='green':
    print('恭喜你，获得5分！')
elif alien_color=='yellow':
    print('恭喜你，获得10分！')
else:
    print('恭喜你，获得15分！')


age = 15
if age<2:
    print('这个人是婴儿')
elif age>=2 and age<4:
    print('这个人是幼儿')
elif age>=4 and age<12:
    print('这个人是儿童')
elif age>=13 and age<20:
    print('这个人是青少年')
elif age>=20 and age<65:
    print('这个人是成年人')
else:
    print('这个人是老人')