def propagar(vector):
    largo = len(vector)
    for i,f in enumerate(vector):
        if f ==1 and (i < (largo-1)) and vector[i+1]==0:
             vector[i+1]=1
        if f ==1:
            j=i
            while (vector[j] ==1) and (j != 0) and (vector[j-1]==0):
                vector[j-1] =1
                j-=1
    return vector

def main():
    print(propagar([0,1,-1,0,0,0,-1,1,0,0,0,0,0]))
    print()
    print()
main()