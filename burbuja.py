def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            #print("paso")
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
    return A


def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def burbuja_optimizado(A):
	n = len(A)
	cambio=False
	for i in range(1, n):
		print("paso")
		for j in range(0, n - i):
			if A[j] > A[j + 1]:
				swap(A, j, j + 1)
				cambio=True
		if(cambio==False):
			return A
		cambio=False

	return A

#p=burbuja_optimizado([6,5,4,3,2,1])
#print(p)








"""def burbuja(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def burbuja_optimizado(A):
    raise NotImplementedError()
    
    
"""
