_autor_ = 'Gisella Ineira Sanchez '


def descomposicion(num):
    if num==10:
        return descomposicion(1)
    else:
        print(num,"(num= -1)+1" ,end=" 1 ")
        return descomposicion(num)


#5=4+1
#5=(3+1)+1
#5=(2+1)+1+1

