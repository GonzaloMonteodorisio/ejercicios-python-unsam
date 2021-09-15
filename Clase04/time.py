import time
# def propagar(vector):
#     l = len(vector)
#     nuevo_vector = []    
#     for j in range(l):
#         nuevo_vector.append(vector[j])
#     k = 0
#     while k < l:
#         for i in range(l):
#             if i == 0:
#                 if nuevo_vector[i] == 1 and nuevo_vector[i+1] == 0:
#                     nuevo_vector[i+1] = 1
            
#             elif i == l-1:
#                 if nuevo_vector[i] == 1 and nuevo_vector[i-1] == 0:
#                     nuevo_vector[i-1] = 1

#             else:
#                 if nuevo_vector[i] == 1 and nuevo_vector[i-1] == 0:
#                     nuevo_vector[i-1] = 1
#                 if nuevo_vector[i] == 1 and nuevo_vector[i+1] == 0:
#                     nuevo_vector[i+1] = 1
#         k += 1
#     return nuevo_vector

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
    start = time.time()
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    end = time.time()
    print(end - start)
main()