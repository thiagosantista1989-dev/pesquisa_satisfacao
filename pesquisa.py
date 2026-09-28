excelente = 0
bom = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao = int(input("Opinião (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

print("\n--- RESULTADO DA PESQUISA ---")
print(f"Respostas EXCELENTE: {excelente}")
print(f"Respostas RUIM: {ruim}")