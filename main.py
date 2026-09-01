# print("Ola voce!")

# nome = "João"
# variável que recebe um valor de input
# senha = input("Digite uma senha: ")

# if senha == "abóbora":
#     print("Senha correta!")
# elif senha == "skol beats": 
#     print("Senha corretissima")
# else: 
#     print("Senha errada!")

print("Bem vindo ao bot da manu ;p")
opçao = input("Digite um valor de 1 a 10: ")


match opçao:
    case "1":
        print("setor de atendimento")
        print("qual atendente voce deseja falar? SAC ou RH")
        atendente = input("Digite o atendimento desejado: ")

        if atendente == "SAC": 
            print("Voce vai ser direcionado para o SAC")
        elif atendente == "RH": 
            print("Voce vai ser direcionado para o RH")
        else: 
            print("Não exite esse atendimento...")
    case "2": 
        print("segunda via do boleto")
        print("Sobre qual boleto voce deseja falar?")
        segundavia = input("Digite a opçao de pagamento: ")

        if segundavia == "PIX": 
            print("A chave de pagamento vai ser gerada")
        elif segundavia == "CREDITO":
            print("Digite ou escaneie o cartao para pagamento parcelado:")
        else: 
            print("Nao exite essa opçao")
    case "3":
        print("opçoes de musica")
        print("melhores musicas!")
        musica = input("Digite sua musica favorita: ")

        if musica == "BOKALOCA":
            print("Seu gosto é invrivel")
        elif musica == "SET DO DJ PEDRO 2.0":
            print("Voce tem bom gosto")
        else: 
            print("Muda sua musica favorita, porque essa musica é horrivel")
    case "4":
        print("Historico de compra")
        print("Mes desejado")
        historico = input("De qual mes voce desja ver o historico, digite: ")

        if historico == "MAiO":
            print("Seu historico sera mostrado apos voce digitar seu cpf")
        elif historico == "OUTUBRO":
            print("Seu historico vai ser mostrado depois de colocar o seu numero do cpf")
        else: 
            print("Esse mes é invalido!")
    case "5":
        print("Mostrar cardapio")
        print("Opçoes de pratos")
        cardapio = input("Qual cardapio de pizza voce eseja ver?")

        if cardapio == "DOCE":
            print("Esse cardapio esta diponivel, para abrir digite doce como senha")
        elif cardapio == "SALGADAS":
            print("Esse cardapio esta disponivel, para abrir didite salgadas para abrir")
        else: 
            print("Essa opçao nao existe")
    case "6":
        print("Fazer compra pelo instagram")
        print("De qual nicho voce desja comprar? ")
        instagram = input("Digite o nicho desejado:")

        if instagram == "SKINCARE":
            print("Essa opçao de compra é valida")
        elif instagram == "DISPOSITIVOS DIGITAIS":
            print("Essa opçao de compra esta disponivel no momento")
        else:
            print("Nao exite esse nicho de compra:")
    case "7":
        print("Lojas bmw")
        print("Horarios para visitaçao")
        bmw = input("Digite o horario que voce deseja ir visitar a nossa loja")

        if bmw == "16:30":
            print("Horario disponivel")
        elif bmw == "10:40":
            print("Horario disponivel")
        else:
            print("Esse horario ja foi reserado!")
    case "8":
        print("Ver preços dos iphones 17")
        print("Modelos do iphone:")
        preços = input("De qual modelo voce deseja ver o preço?")

        if preços == "IPHONE 17 PRO MAX":
            print("Esse celular esta custando nove mil")
        elif preços == "IPHONE 17 256GB AZUL":
            print("Esse ceclular custa cinco mil")
        else: 
            print("Esse celular nao esta disponivel na loja")
    case "9": 
        print("Gastra dinheiro atoa")
        print("Motivos para gastar seu dinheiro")
        dinheiro = input("Como voce vai gastar o seu dinheiro? ")

        if dinheiro == "COM ROUPAS DE MARCA":
            print("Essa forma é valida!")
        elif dinheiro == "COM BEBIDAS":
            print("Essa forma é super valida")
        else: 
            print("Essa opçao nao é aceita!!!!")
    case "10":
        print("Programçao do fim de ano")
        print("Opçoes para o fim do ano")
        fimdeano = input("Qual o seu destino para a virada? ")

        if fimdeano == "RIO DE JANEIRO":
            print("Essa opçao é muito boa")
        elif fimdeano == "PORTO SEGURO BAHIA":
            print("Essa opçao é maravilhosa")
        else:
            print("Muda essa opçao nao é boa!!")0
    case _:
        print("Não exite essa opçao, digite de 1 a 10")    