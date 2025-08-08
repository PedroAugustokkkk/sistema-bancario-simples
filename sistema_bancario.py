# DEPOSITO, SAQUE E EXTRATO
# APENAS 1 USUÁRIO
# TODOS OS DEPOSITOS DEVEM SER ARMAZENADOS EM 
# UMA VARIAVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO
# 3 SAQUES DIARIOS COM LIMITE DE 500 REAIS POR SAQUE
# CASO NAO TENHA SALDO EM CONTA, EMITE MENSAGEM
# TODOS OS SAQUES DEVEM SER ARMAZENADOS EM UMA 
# VARIÁVEL E EXIBIDOS NA OPERAÇÃO DE EXTRATO
# EXTRATO DEVE LISTAR TODOS OS DEPOSITOS E SAQUES
# NO FIM DA LISTAGEM, MOSTRA O SALDO ATUAL NA CONTA
# EXIBIÇÃO: R$ xxx.xx,


menu = """
================
[d] DEPÓSITO
[s] SAQUES
[e] EXTRATO
[sair] SAIR
================
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "s":
        valor = float(input("Informa o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do daque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else: 
            print("Operação falhou! O valor informado é inválido.")
    
        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizados moviementações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")
        

    elif opcao == "sair":
        break

    else:
        print("DIGITE ALGUM DIGITO VÁLIDO.")
