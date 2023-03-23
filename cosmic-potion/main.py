import replit
import time
import colorama as cr
import sys

nome = ""

def limparTela():
    time.sleep(7)  #aumentar tempo
    replit.clear()


def _print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)
    print("\n")


def intro():
    _print(
        f"{cr.Fore.WHITE}Bem-vindo! Este é um jogo em que suas escolhas ditam o rumo da história. Portanto, sempre que precisar fazer uma decisão digite o que prefere: escolha (1) ou (2) para prosseguir no jogo. Caso precise digitar algo além disso, o jogo deixará claro."
    )
    _print(
        f"{cr.Fore.RED}Filho, este gato surgiu de um dos meus experimentos mágicos, pensei que poderia ficar com ele. Aparentemente ele tem poderes além do que um gato normal jamais teria."
    )
    _print(f"{cr.Fore.BLUE}Miau... cof cof. Olá humano! Qual seu nome?")
    global nome
    nome = input(f"{cr.Fore.WHITE}Nome: ")
    _print(
        f"{cr.Fore.BLUE}Olá, {nome}. Já que agora sou seu pet, posso te acompanhar e conversar com você quando necessário."
    )


def poção():
    _print(
        f"{cr.Fore.RED}{nome}, Recentemente venho trablhando numa nova magia muito poderosa, capaz de muita coisa. Se trata de uma poção, a partir do momento que alguém a ingere, muitas coisas acontecem. Mas ainda está nos estágios inciais e gostaria que você experimentasse. Você aceita beber (1), ou não está a fim (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        beber()
    elif (escolha == "2"):
        nbeber()
    else:
        _print(
            f"{cr.Fore.WHITE}Essa não é uma resposta válida, responda apenas 1 ou 2 para confirmar sua escolha sempre que aparecer (1) e (2) no texto."
        )
        limparTela()
        poção()


def beber():
    _print(
        f"{cr.Fore.RED}Ótimo! Tem alguns efeitos colaterais, mas nada preocupante. Pode tomar."
    )
    limparTela()
    mundo1()


def nbeber():
    _print(f"{cr.Fore.RED}Se não quer ajudar, já pode ir para o seu quarto.")
    _print(
        f"{cr.Fore.BLUE}Bem, você está livre agora, podemos brincar (1) ou você prefere praticar magia (2)?"
    )
    escolha = input()
    if (escolha == "1"):
        _print(f"{cr.Fore.WHITE}...")
        _print(
            f"{cr.Fore.BLUE}Foi muito legal brincar, mas você parece cansado, que tal ir se hidratar? \nEspera! Isso não é água! Parece aquela poç..."
        )
        limparTela()
        mundo1()
    elif (escolha == "2"):
        _print(f"{cr.Fore.WHITE}...")
        _print(
            f"{cr.Fore.BLUE}Você realmente estava inspirado com todas aquelas magias que praticou, mas agora parece cansado, que tal ir se hidratar? \nEspera! Isso não é água! Parece aquela poç..."
        )
        limparTela()
        mundo1()
    else:
        _print("Resposta inválida")
        limparTela()
        nbeber()


def mundo1():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Espera, que lugar é esse? Eu consigo te ver no meio desse enorme deserto, mas agora pouco você estava não no quarto comigo? Também acho que você não me vê."
    )
    loop1()


def loop1():
    _print(
        f"{cr.Fore.BLUE}Talvez você possa caminhar e procurar algo (1) ou então se abrigar e esperar alguém te encontrar (2). O que acha?"
    )
    escolha = input()
    if (escolha == "1"):
        _print(f"{cr.Fore.BLUE}Então é melhor seguir ao norte, eu acho.")
        _print(f"{cr.Fore.WHITE}...")
        _print(
            f"{cr.Fore.BLUE}Você já caminhou bastante e ainda não achou nada..."
        )
        loop1()
    elif (escolha == "2"):
        encontro1()
    else:
        _print("Resposta inválida")
        limparTela()
        mundo1()


def encontro1():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Espera! Que barulho é esse? \n Você também está vendo aquele enorme ser carregando um... quadro?! Diga-se de passagem é uma bela paisagem montanhosa com esse céu roxo, parece um lugar frio. \n Será que você devia ficar parado apreciando essa estranha arte (1) ou simplesmente sair correndo (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        _print(
            f"{cr.Fore.BLUE}Acho que você demorou demais para pensar... Cuidado!"
        )
        limparTela()
        mundo2()
    elif (escolha == "2"):
        _print(
            f"{cr.Fore.BLUE}Acho que você demorou demais para pensar... Cuidado!"
        )
        limparTela()
        mundo2()
    else:
        _print(
            f"{cr.Fore.BLUE}Acho que você demorou demais para pensar e isso nem me parece uma resposta válida... Cuidado!"
        )
        limparTela()
        mundo2()


def mundo2():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Ok... isso é bizarro mas, você agora está num cenário gélido e montanhoso, assim como naquele quadro! \n Mas calma aí, eu tô vendo alguma coisa, parece uma cabana! Será que finalmente você encontrou alguém? \n Bem que você poderia ir até essa cabana (1) ou então explorar um pouco esse lugar (2). E ai, O que vai ser?"
    )
    escolha = input()
    if (escolha == "1"):
        cabana()
    elif (escolha == "2"):
        lago()
    else:
        _print("Resposta inválida")
        limparTela()
        mundo2()


def cabana():
    _print(
        f"{cr.Fore.BLUE}Uau! Quanta coisa. Muitos baús, pinturas, espelhos, um cofre! \n E essas escrituras na parede? O que será que quer dizer? \n Quem sabe elas são a chave do cofre... Me diz o que você acha que significa."
    )
    _print(f"{cr.Fore.RED}1{cr.Fore.CYAN}2{cr.Fore.GREEN}4{cr.Fore.BLUE}1")
    escolha = input()
    while (escolha != "VIDA" and escolha != "Vida" and escolha != "vida"):
        _print(f"{cr.Fore.BLUE}Nada aconteceu, tente alguma outra coisa.")
        escolha = input()
    _print(
        f"{cr.Fore.BLUE}Abriu! Uma espada! Mas ela parece um pouco velha, não deve fazer muita coisa."
    )
    espada()


def lago():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Certo, {nome}, acho que você já andou bastante, que tal... Olha! Tem algo brilhante vindo daquele lago congelado ali na frente, dá uma olhada."
    )
    _print(f"{cr.Fore.RED}1{cr.Fore.CYAN}2{cr.Fore.GREEN}4{cr.Fore.BLUE}1")
    _print(
        f"{cr.Fore.BLUE}Isso tá me parecendo um código, e ele tá pedindo pra ser decifrado, me diz o que você acha que significa."
    )
    escolha = input()
    while (escolha != "VIDA" and escolha != "Vida" and escolha != "vida"):
        _print(f"{cr.Fore.BLUE}Nada aconteceu, tente alguma outra coisa.")
        escolha = input()
    _print(
        f"{cr.Fore.BLUE}Parece que o lago começou a descongelar. Olha, dentro dele, uma espada! Mas ela parece um pouco velha, não deve fazer muita coisa."
    )
    espada()


def espada():
    _print(f"{cr.Fore.BLUE}Quer pegá-la (1) ou vai procurar outra coisa (2) ?")
    escolha = input()
    if (escolha == "1"):
        _print(
            f"{cr.Fore.BLUE}Parece que ela foi feita pra você, encaixa perfeitamente!"
        )
        limparTela()
        encontro2()
    elif (escolha == "2"):
        _print(
            f"{cr.Fore.BLUE}Ok, então que tal olhar naquele... Eita! De novo alguma coisa me interrompendo, você disse que não ia pegar essa espada, por que ela tá na sua mão? \n Espera, você realmente não a pegou, ela foi atraida por você, parece até que foi feita pra isso!"
        )
        limparTela()
        encontro2()
    else:
        _print("Resposta inválida")
        limparTela()
        espada()


def encontro2():
    _print(f"{cr.Fore.GREEN}Olá, estranho")
    _print(f"{cr.Fore.BLUE}Quem é esse?")
    _print(
        f"{cr.Fore.GREEN}Silêncio, gato. Estou falando com você, {nome}. Você não pertence a este lugar, estamos te observando e achamos que já está na hora de você partir. Este mundo é dominado por seres cósmicos que nem os mais sábios da sua espécie entenderiam. Se pretende alongar sua passagem, terei que te impedir agora."
    )
    _print(
        f"{cr.Fore.BLUE}Rápido, use a espada! \n Ataque-o (1) ou esquive (2)")
    escolha = input()
    if (escolha == "1"):
        _print(
            f"{cr.Fore.GREEN}Acha que vai me derrotar com essa espada fraca?")
        _print(f"{cr.Fore.BLUE}De novo! \n Ataque-o (1) ou esquive(2)")
        escolha2 = input()
        if (escolha2 == "1"):
            _print(f"{cr.Fore.GREEN}Ugh! Você está começando a me irritar.")
            _print(f"{cr.Fore.BLUE}Mais um vez! \n Ataque-o (1) ou esquive(2)")
            escolha3 = input()
            if (escolha3 == "1"):
                batalha1final()
            elif (escolha == "2"):
                derrota1()
        elif (escolha2 == "2"):
            derrota1()
    elif (escolha == "2"):
        _print(
            f"{cr.Fore.GREEN}É melhor tentar desviar mesmo, um só golpe e você já era!"
        )
        _print(f"{cr.Fore.BLUE}De novo! \n Ataque-o (1) ou esquive(2)")
        escolha2 = input()
        if (escolha2 == "1"):
            derrota1()
        elif (escolha2 == "2"):
            derrota1()
    else:
        _print(f"{cr.Fore.BLUE}O que está fazendo?! Assim você vai morrer!")
        _print(f"{cr.Fore.RED}Você falhou.")
        limparTela()
        encontro2()


def batalha1final():
    _print(
        f"{cr.Fore.GREEN}Chega dessa brincadeira, é melhor sair do meu caminho!"
    )
    _print(
        f"{cr.Fore.BLUE}Ele parece estar carregando um golpe e deve ser muito poderoso, ainda vai atacar ele (1), ou vai se esquivar (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        derrota1()
    elif (escolha == "2"):
        _print(
            f"{cr.Fore.BLUE}Isso! Ele caiu e acertou a si mesmo! Parabéns {nome}, achei que não ia sair vivo dessa."
        )
        limparTela()
        mundo2volta()


def derrota1():
    _print(f"{cr.Fore.GREEN}Erro. Achou mesmo que ia me derrotar?")
    _print(f"{cr.Fore.RED}Você falhou.")
    limparTela()
    encontro2()


def mundo2volta():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Parece que aquele cristal que o monstro deixou cair quando morreu foi bem útil, agora estamos de volta ao mundo desértico e árido. \n Só lhe resta tentar achar um caminho para voltarmos ao mundo real, ou agora seria este o nosso mundo real? De qualquer forma, vejo uma luz à direita (1) e outra a sua esquerda (2). Você quer ir por onde?"
    )
    escolha = input()
    if (escolha == "1"):
        direita()
    elif (escolha == "2"):
        esquerda()


def direita():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Olha, um oasis! Ou será que é uma miragem? Quer ir até lá conferir (1) ou vamos seguir caminho (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        _print(
            f"{cr.Fore.BLUE}Estamos bem perto e não me parece estar sumindo, deve ser um verdadeiro oasis... \n Nossa, você também tá sentindo 4lgo estr4nh0, 1ud0 14 m310 10r10... \n ¡35p3r@! 0 qu3 v0c& &5t@ f4z&nd0?"
        )
        limparTela()
        direita()
    elif (escolha == "2"):
        encontro3()


def esquerda():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}Aquilo são construções? Será que há alguém lá? Quer ir conferir (1) ou vamos seguir caminho (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        _print(
            f"{cr.Fore.BLUE}Cá estamos, várias casinhas de arenito, pode ser que alguém esteve aqui há muito tempo, tudo parece abandonado... \n Que tal irmos de casa em casa, e vemos o que há de útil por aqui? \n Vamos naquel... Nossa, você também tá sentindo 4lgo estr4nh0, 1ud0 14 m310 10r10... \n ¡35p3r@! 0 qu3 v0c& &5t@ f4z&nd0?"
        )
        limparTela()
        esquerda()
    elif (escolha == "2"):
        encontro3()


def encontro3():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.YELLOW}{nome}, gato. O que fazem nessas terras? Vocês deveriam saber que é perigoso. Posso lhe oferecer um objeto extremamente poderoso capaz de fazer qualquer coisa que queira fazer por aqui. É seu, em troca de um favor, claro."
    )
    _print(
        f"{cr.Fore.BLUE}Mais um ser que misteriosamente sabe sobre nós. E então, você vai aceitar (1) ou recusar (2) a oferta?"
    )
    escolha = input()
    if (escolha == "1"):
        oferta1()
    elif (escolha == "2"):
        oferta2()


def oferta1():
    _print(
        f'{cr.Fore.YELLOW}Então vamos lá: realmente te dou o objeto combinado, desde que você resolva esse enigma para mim. Venho tentando desvendá-lo há tempos, e você é minha última esperança, sinto que é o único capaz de revelar esse segredo. Se trata de algo que está sempre entre dois números, seja lá o que isso quer dizer. Esse "algo", também está entre o real e o sonho, ainda que o mesmo não tenha percebido. Sei que a resposta se trata de uma única palavra. O que me diz, qual sua tentativa?'
    )
    escolha = input()
    while (escolha != "EU" and escolha != "Eu" and escolha != "eu"
           and escolha != nome):  #variavel nome
        _print(
            f"{cr.Fore.YELLOW}Eu tentei exatamente isso um tempo atrás. Tenho certeza que não é essa a resposta, tente alguma outra coisa."
        )
        escolha = input()
    _print(
        f"{cr.Fore.YELLOW}É claro! Só podia ser isso. Pensando bem, até que estava fácil. Enfim, aqui está seu objeto, como prometido."
    )
    _print(
        f"{cr.Fore.BLUE}Parece o cristal que aquele monstro no mundo de montanhas derrubou quando o derrotamos, e levou a gente de volta pra esse mundo. Onde será que ele vai nos levar agora?"
    )
    cristal()


def oferta2():
    _print(
        f"{cr.Fore.YELLOW}Imaginei que poderia me dar essa resposta, mas quero deixar bem claro que realmente preciso desvendar aquele enigma. Sendo assim, te faço uma nova oferta: ou você me ajuda com o enigma (1) ou teremos que batalhar aqui e agora (2)."
    )
    escolha = input()
    if (escolha == "1"):
        oferta1()
    elif (escolha == "2"):
        _print(f"{cr.Fore.YELLOW}Se é o que você quer...")
        _print(
            f"{cr.Fore.BLUE}Você vai ter que ser rápido, ataque quando eu dis")
        _print(f"{cr.Fore.RED}Você falhou.")
        limparTela()
        _print(
            f"{cr.Fore.BLUE}É, ele veio rápido demais, cá estamos novamente.")
        oferta2()


def cristal():
    _print(f"{cr.Fore.WHITE}...")
    _print(
        f"{cr.Fore.BLUE}{nome}, finalmente! Voltamos para o mundo real. Mas o que foi isso? Acho melhor ir perguntar para o seu pai sobre essa poção."
    )
    _print(
        f"{cr.Fore.RED}Ah, olá {nome}. Como foi a experiência? Estive te acompanhando durante sua jornada. Talvez tenha percebido minha interferência no seu caminho, mas caso não... A espada que conseguiu, é uma das coisas que coloquei lá. Todos que te encontraram lá sabiam seu nome, óbvio, eu que os criei. Claro que seria difícil fazer você seguir todo o planejado, e confesso que não foi possível sempre. Quando chegou perto de algo que eu não queria que visse, simplesmente te fiz voltar no tempo. Enfim, acho que se saiu bem. Vou voltar para meus aposentos e fazer minhas anotações."
    )
    _print(
        f"{cr.Fore.BLUE}Nossa, então foi tudo um teste. Você não vê problema no fato de ele ter te usado para um experimento (1), ou quer ir questioná-lo (2) ?"
    )
    escolha = input()
    if (escolha == "1"):
        final1()
    elif (escolha == "2"):
        final2()


def final1():
    _print(
        f"{cr.Fore.BLUE}Bom, se não foi problema, tenho que admitir que foi muito divertido, mas fiquei com um pouquinho de medo de você não sair vivo de lá, mas como foi ideia do seu pai, acho que ele não deixaria isso acontecer... Essa aventura me deu fome, quer dizer... Miau."
    )
    _print(f"{cr.Fore.WHITE}FIM")


def final2():
    _print(f"{cr.Fore.BLUE}Bom, é melhor ir logo então.")
    _print(
        f"{cr.Fore.BLUE}Essa sala é realmente muito bonita, mas cadê seu pai? Olha, o frasco que você usou pra tomar a poção, imagine se tivesse bebido inteiro, estáriamos lá até agora, mas se você não bebeu toda a poção, por que o frasco está vazio? Será que... É, acho que somos só nós dois agora, quer dizer... Miau."
    )
    _print(f"{cr.Fore.WHITE}FIM")


intro()
poção()
