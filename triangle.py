#Adewale Adeoluwa

a=int(input('Enter length of side 1:'))
b=int(input('Enter length of side 2:'))
c=int(input('Enter length of side 3:'))
if a+b<c or b+c<a or a+c<b :
    print( 'not a triangle')
elif a==b==c:
    print('equalateral triangle ')
elif a<b<c or b>a>c or c<b>a:
    print('scalene triangle ')
elif a==b or b==c :
	print('isosceles triangle')
else:
	print('A right angle triangle') 