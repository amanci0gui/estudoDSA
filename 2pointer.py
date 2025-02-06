
def reverseWords_manual(array):
    res = '' #a response
    l, r = 0, 0 #ponteiros esquerdo e direito 

    while r < len(array): #enquanto o ponteiro direito não chegar no fim do array
        if array[r] != ' ': 
            r += 1 #se o ponteiro r não apontar para um espaço em branco ele avança
        
        
        else:#pega do ponteiro l até o ponteiro r (palavra)
            res += array[l:r+1][::-1] #inverte a palavra
            r += 1
            l = r

    res += ' '
    res += array[l:r][::-1]

    print(res)

    return res[1:]

reverseWords_manual('Neymar Messi Suarez')           

            