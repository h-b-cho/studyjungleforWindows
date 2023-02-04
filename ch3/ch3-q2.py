# 사람 정보가 담긴 리스트가 있을 때,
# 리스트 안의 딕셔너리인 각 사람에 대해서
# 만약 사람의 이름이 'bob'이면
# 그 사람의 나이를 출력해라.

people = [{'name': 'bob', 'age': 20}, 
        {'name': 'carry', 'age': 38},
        {'name': 'john', 'age': 7},
        {'name': 'smith', 'age': 17},
        {'name': 'ben', 'age': 27}]

# for x in people:
#   if x['name']=='bob':
#     print(x['age'])
    
def getAge(target):
  for x in people:
    if x['name'] == target:
      text = x['name'] + ' is ' + str( x["age"] ) + ' years old.'
      return text 
  return 'No one has that name here.'
  
print( getAge('ben') )