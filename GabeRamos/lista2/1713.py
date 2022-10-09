#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

salHora = float(input())

horasTrab = float(input())

salBruto = salHora * horasTrab

descImp = salBruto * 11/100

descInss = salBruto * 8/100

descSind = salBruto * 5/100

salLiq = salBruto - descImp - descInss - descSind

print("Salário bruto: R$%.2f" %(salBruto))
print("Imposto: R$%.2f" %(descImp))
print("INSS: R$%.2f" %(descInss))
print("Sindicato:R$%.2f" %(descSind))
print("Líquido: R$%.2f" %(salLiq))