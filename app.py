def fazer_receita():
    receitas = {
        ("farinha", "açúcar", "ovos", "manteiga", "leite", "fermento"): "Bolo Simples",
        ("farinha", "ovos", "açúcar", "manteiga", "fermento", "leite"): "Bolo de Pão de Ló",
        ("ovos", "açúcar", "manteiga", "farinha", "fermento", "leite"): "Bolo Fofo",
    }
    
    print("Bem-vindo ao jogo de fazer receitas! Escolha os ingredientes na ordem desejada.")
    
    ingredientes_escolhidos = []
    for i in range(6):
        escolha = input(f"Passo {i+1}: Escolha o ingrediente: ")
        ingredientes_escolhidos.append(escolha.lower())
    
    receita = receitas.get(tuple(ingredientes_escolhidos), "Receita desconhecida")
    print(f"Parabéns! Você fez um {receita}!")

fazer_receita()
