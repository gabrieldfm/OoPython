def cria_conta(numero, titular):
    conta = {"numero": numero, "titula": titular}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))