from time import sleep

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
        global saldo, extrato

        valor: float = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Depósito efetuado com sucesso!')
            sleep(2)
        else:
            print('Operação falhou! O valor informado é inválido.')
            sleep(2)

def sacar():
    global saldo, extrato, numero_saques, LIMITE_SAQUES

    valor: float = float(input('Informe o valor que deseja sacar: '))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print('Você não tem saldo suficiente. Operação falhou.')

    elif excedeu_limite:
        print(f'Operação falhou! o valor de {valor} excede o limite.')
        
    elif excedeu_saques:
        print('Operação falhou! Número máximo de saques excedido.')

    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque efetuado com sucesso!')
        sleep(2)

def ver_extrato():
    global saldo, extrato

    print('\n' + ' EXTRATO '.center(20, '='))

    if not extrato:
        print('Não foram realizadas movimentações')
    else:
        print(extrato)

    print(f'\nSaldo: R$ {saldo:.2f}')
    print('=' * 20)
    sleep(2)

while True:

    print('\n=== Menu ===')
    print('[1] - Depositar')
    print('[2] - Sacar')
    print('[3] - Extrato')
    print('[4] - Sair')


    try:
        opcao: int = int(input('Escolha uma opção: '))

        if opcao == 1:
            depositar()

        elif opcao == 2:
            sacar()

        elif opcao == 3:
            ver_extrato()
    
        elif opcao == 4:
            print('Obrigado por utilizar!')
            sleep(2)
            exit(0)
    
        else:
            print('Operação inválida! Tente novamente.') 
            sleep(2)
    
    except ValueError:
        print('Valor inválido! Tente novamente')
        sleep(2)



if __name__ == '__main__':
    pass
