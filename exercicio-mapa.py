from collections import deque

def menu():
    print("\n--- Sistema de Controle de Fila - Açougue Bom Preço ---")
    print("1 - Retirar Senha")
    print("2 - Chamar Próxima Senha")
    print("3 - Mostrar Fila Atual")
    print("4 - Sair")
    return input("Escolha uma opção: ")

# Inicialização da fila
fila = deque()
contador_senha = 0

while True:
    opcao = menu()  
    if opcao == '1':
        contador_senha += 1 #Problema identificado, solução foi adicionado um contador pra encrementar a fila e mudar a senha dos clientes
        senha = f"A{contador_senha}"
        fila.append(senha) #Problema identificado, solução trocar a chamada fila.end(senha) para fila.append(senha) pra adicionar a nova senha na fila
        print(f"Senha {senha} retirada com sucesso!")

    elif opcao == '2':
        if fila:
            senha_chamada = (fila.popleft()) # Problema identificado, solução foi adicionado fila.popleft() pois está sendo chamada de uma função global mas está sendo chamada um método da instância fila 
            print(f"Atenção! Senha chamada: {senha_chamada}")
        else:
            print("Fila vazia. Nenhuma senha para chamar.")
    elif opcao == '3':
        if fila:
            print(f"Fila atual de senhas: {fila}") # Problema identificado, solução foi retirado fila.list pois existe o atributo .list e foi colocado pra imprimir a lista
        else:
            print("Fila vazia.")
    elif opcao == '4':
        print("Sistema encerrado. Obrigado por utilizar!")
        break

else:
    print("Opção inválida. Tente novamente.")