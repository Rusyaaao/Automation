"""A = [[1,0],[1,1]]
m = 0
k = 0
for i in range(len(A)):
    if A[i]== 1:
        m += 1 
    for j in range(len(A[i])):
        if  A[i][j] == 1:
            k += 1
sum = m+k
print(sum)
   
massiv = [1,3,5,3,1]
 
for i in massiv:
    if massiv.count(i) == 1:
        print (massiv.index(i))
      

index = massiv.index(1)
print(index)
  """




#def calculate(matrix:list)-> int:
#...

#def main()->None:
    #with open("example.txt", "r") as fd:

data = []
s = 0
with open("d:/Automation/test/example.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
  #  print([x for i in data for x in i].index(1))
    
for inner_list in data:
    for number in inner_list:
        if inner_list == 1:
            s = inner_list.index
        else:
            continue
print(data)        
print(s)
                   
# Думаю, что дальше нужно использовать функциональное программирование
# Просуммировать по осям и проверить, что сумма  > 1 ???

"""
def poisk(s):
    return data.index(1)


map_object = map(poisk, data)

print(list(map_object))




print(A)
i = 1
for i in range(len(A)-1):
    sum = int(A[i]) + int(A[i+1])
    if sum > 1:
        pass
    else:   
        pass
        """