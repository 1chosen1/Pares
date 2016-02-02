n = 10
p = 0
while n <= 5000:
#print (n)
    if n%2 == 0:
        if n==100 or n==1000:
            pass
        else:
            p += n
    n += 1
print ("La suma de los numeros pares entre 10 y 5000 omitiendo los numeros 100 y 1000 es de: %i"% p)