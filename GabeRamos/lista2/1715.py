#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

client = int(input())

compra = float(input())

if client == 1:
    compra = compra
    print("Valor total a ser pago: R$%.2f" %(compra))
    
elif client == 2:
    compra = compra - (compra * 13/100)
    print("Valor total a ser pago: R$%.2f" %(compra))
elif client == 3:
    compra = compra - (compra * 7/100)
    print("Valor total a ser pago: R$%.2f" %(compra))
else:
    if client > 3:
        print("OPÇÃO INVÁLIDA!")