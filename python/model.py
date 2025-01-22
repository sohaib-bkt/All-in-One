def remplir(t):
    list1 = list(t);
    return list1;

def afficher(t):
    print(list(t))

def remplir_matrice(d,p):
    matrice = [[0]*d]*p
    for i in range(d):
        for j in range(p):
            matrice[i][j] = int(input(f"enter {i+1} {j+1}") )
    for i in range(d):
        for j in range(p):
            print(matrice[i][j])

# remplir_matrice(2,2)

def afficher_matrice(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            print(matrice[i][j])

# afficher_matrice([[1,2,3],[3,4,5]])

def min_max(t):
    min = t[0]
    max = t[0]
    for i in range(len(t)):
        if t[i] <= min:
            min = t[i]
        if t[i] >= max:
            max = t[i]
    return max , min

# min_max([1,2,3,4])

def binaire(number):
    list1 = []
    while number > 0 :
        res = number % 2
        number = number // 2
        list1.append(res)
    list1.reverse()
    return list1
# binaire(4)

def consecutif(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

# print(consecutif([1, 2, 3]))  

def symetrique(t):
    for i in range(len(t)):
        for j in range(i, len(t[i])):
            if t[i][j] != t[j][i]:
                return False
    return True

# print(symetrique([[1, 2, 3], [2, 4, 5], [3, 5, 6]]))  

        
        


