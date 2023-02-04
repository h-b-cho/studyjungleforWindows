def f(x):
	return 2*x+3

print(f(2))  # 7

#------------------------

def sum_all(a,b,c):
	return a+b+c
def mul(a,b):
	return a*b		
result = sum_all(1,2,3) + mul(10,10)

print(result)

#------------------------

def is_adult(age):
	if age > 20:
		print('성인입니다') 
	elif age >= 13:
		print('청소년이에요')  
	else:
		print('어린이네요!')
		
is_adult(30)

#------------------------

fruits = ['사과','배','감','귤']

for i in range(len(fruits)):  # i 가 0, 1, 2, 3일 때 
	fruit = fruits[i]	
	print(fruit)