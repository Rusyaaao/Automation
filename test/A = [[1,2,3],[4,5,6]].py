# Ищем все соседние значение 1. Посещенные значения 1 и 0 заменяем значением -1.

def func_check_neighbors(matr, i, j):
    if i >= 0 and i < len(matr) and j >= 0 and j < len(matr[0]):    
        if matr[i][j] == 1:
            matr[i][j] = -1
            # соседние значения
            func_check_neighbors(matr, i+1, j)
            func_check_neighbors(matr, i, j+1)
            func_check_neighbors(matr, i-1, j)
            func_check_neighbors(matr, i, j-1)
        else:
            matr[i][j] = -1

#
def calculate(matr):
    count = 0
    for i in range(len(matr)):
        for j in range(len(matr[i])):
            if matr[i][j] == 1:
                func_check_neighbors(matr, i, j)
                count += 1
    return count




def main():
   
    matr = []

    f = open("input.txt", "r")

   
    for line in f.readlines():
        if line == "\n":    
            print(calculate(matr))
            matr.clear()
        else:              
            print(line.split('\n')[0])
            matr.append([int(x) for x in line.split()])

    if len(matr) != 0:
        print(func_count(matr))
        matr.clear()

    f.close()


if __name__ == "__main__":
    main()

