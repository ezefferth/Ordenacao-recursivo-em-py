#author Ezefferth
#ordenação recursivo
def ordenado(v,i,j):
    if i==j-1:
        return 1
    elif v[i+1]>v[i]:
        return ordenado(v,i+1,j)
    else:
        return 0
    
        
        
i=0
n=[2,6,3]
print ordenado(n,i,len(n))
