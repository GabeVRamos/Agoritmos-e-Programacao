#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

planoFunc =  input()
salarioAtual = float(input())

if planoFunc == "A":
    salNovo = salarioAtual + (salarioAtual * 10/100)
elif planoFunc == "B":
    salNovo = salarioAtual + (salarioAtual * 15/100)
else:
    if planoFunc == "C":
        salNovo = salarioAtual + (salarioAtual * 20/100)
print("Novo salário: R$%.2f" %(salNovo)) 