#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input())
horasExt = float(input())

salMinimo = 1192.40
valHrExtr = 10

salHrExt = horasExt * valHrExtr
salBruto = (3 * salMinimo) + salHrExt

if salBruto > 2000:
    descINSS = salBruto * 12/100
else:
    if salBruto < 2000:
        descINSS = salBruto * 5/100
        
if salBruto > 2500:
    descImp = salBruto * 20/100
else:
    if salBruto < 2500:
        descImp = salBruto
        
salLiq = salBruto - (descImp) - (descINSS)        

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salLiq))