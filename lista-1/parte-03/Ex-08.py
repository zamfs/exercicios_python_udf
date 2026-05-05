valor_compra = float(input())
verif_compra = valor_compra > 500.00

vip = input().capitalize()

if vip == "False":
    vip = False
elif vip == "True":
    vip = True

desconto = vip or verif_compra

print(f'Terá direito ao dessconto? {desconto}')