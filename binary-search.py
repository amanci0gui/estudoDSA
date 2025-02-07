def binary_search(nums, n):
    lo = 0 #ponteiro que fica no início do array
    hi = len(nums) #ponteiro que fica no final do array
    steps = 0 #número de passos para comprovar O(log n)

    while lo < hi: 
        steps += 1
        mid = (lo+hi)/2 #ponteiro que ficará no meio do array

        if nums[mid] == n: #Se o valor do ponteiro mid for igual ao número buscado
            print("Número de steps: ", steps)
            return mid #retorna o ponteiro
        elif nums[mid] < n: #se o numero buscado for maior que o valor do mid
            lo = mid + 1 #coloca o ponteiro do inicio uma posição depois do mid 
        else: 
            #se o valor buscado for menor que o valor do mid ele coloca o ponteiro do final do array no lugar do mid 
            hi = mid
    return -1

a = [1, 2, 3, 4, 5]  
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,  
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]  

binary_search(d, 21)

