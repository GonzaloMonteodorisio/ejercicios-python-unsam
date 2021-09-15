def propagar(vector):
    l = len(vector)
    nuevo_vector = []    
    for j in range(l):
        nuevo_vector.append(vector[j])
    k = 0
    while k < l:
        for i in range(l):
            if i == 0:
                if nuevo_vector[i] == 1 and nuevo_vector[i+1] == 0:
                    nuevo_vector[i+1] = 1
            
            elif i == l-1:
                if nuevo_vector[i] == 1 and nuevo_vector[i-1] == 0:
                    nuevo_vector[i-1] = 1

            else:
                if nuevo_vector[i] == 1 and nuevo_vector[i-1] == 0:
                    nuevo_vector[i-1] = 1
                if nuevo_vector[i] == 1 and nuevo_vector[i+1] == 0:
                    nuevo_vector[i+1] = 1
        k += 1
    return nuevo_vector

propagar([ 0, 0, 0, 1, 0, 0])
def main():
    print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(propagar([ 0, 0, 0, 1, 0, 0]))
# main() 