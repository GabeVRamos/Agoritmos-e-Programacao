#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

numero = int(input())
fatorial = 1
p = 2
while p <= numero:
    fatorial = fatorial * p
    p = p + 1
print("%d! =" %numero, fatorial)
