import easygui

easygui.msgbox("Bem-vindo ao programa em EasyGUI!", title="Aviso")

resposta = easygui.ynbox("Você deseja continuar?", title="Confirmação")
if resposta:
  
    opcao = easygui.buttonbox(
        msg="Escolha sua linguagem favorita:",
        title="Opções",
        choices=["Python","C++"]
    )
    easygui.msgbox(f"Você escolheu: {opcao}", title="Resultado")

    
    nome = easygui.enterbox("Qual é o seu nome?", title="Cadastro")
    if nome:
        easygui.msgbox(f"Olá, {nome}!", title="Saudação")

    
    caminho_arquivo = easygui.fileopenbox("Escolha um arquivo para abrir")
    easygui.msgbox(f"Arquivo selecionado:\n{caminho_arquivo}", title="Arquivo")

else:
    easygui.msgbox("Operação cancelada pelo usuário.", title="Cancelado")