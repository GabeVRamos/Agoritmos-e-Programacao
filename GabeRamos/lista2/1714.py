#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

produto = float(input())

lucro1 = produto * 45/100

lucro2 = produto * 30/100

if produto < 20:
    print("Valor de venda: R$%.2f" %(produto + lucro1 ))
    
else:
    print("Valor de venda: R$%.2f" %(produto + lucro2))