# 과일 리스트가 있을 때,
# 결과를 저장할 변수를 만들고 초깃값은 0으로 한다.
# 리스트 안에 있는 각 과일에 대해서
# 이름이 사과이면
# 결과를 1 증가시킨다.
# > 결과 출력

fruits = ['사과','배','배','감','수박','귤','바나나','딸기','사과','배','수박','메론']

# z=0
# for x in fruits:
#   if x=='메론':
#     z+=1

# print(z)

def FruitCounter(target):
  z=0
  for x in fruits:
    if x == target:
      z+=1
  return z

apple = print( FruitCounter('사과') )
watermelon = print( FruitCounter('수박') )
pear = print( FruitCounter('배') )
