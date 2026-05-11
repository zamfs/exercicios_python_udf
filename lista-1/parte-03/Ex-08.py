"""
Desconto na Compra: Uma loja oferece desconto se o valor da compra for maior que R$ 500,00 OU se o cliente for "VIP"
(dado lógico). Leia o valor e o status VIP e exiba o direito ao desconto.
"""

valor_compra = float(input())
verif_compra = valor_compra > 500.00

vip = input().capitalize()

if vip == "False":
    vip = False
elif vip == "True":
    vip = True

desconto = vip or verif_compra

print(f'Terá direito ao dessconto? {desconto}')