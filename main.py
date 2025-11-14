
def checarCPF(cpf):
    cpfpuro = ""
    i = 0
    #utilizando while para remover não numerais do cpf digitado
    while i < len(cpf):
        if cpf[i] >= "0" and cpf[i] <= "9":
            cpfpuro += cpf[i]
        i += 1

    # verificar se o cpf contem 11 caracteres (após remoção de não numerais) (condição 1)
    if (len(cpfpuro) != 11):
        return False

    #utilizando for para verificar se todos os caracteres são iguais (condição 2)
    todosIguais = True
    for i in range (1,11):
        if cpfpuro[i] != cpfpuro[0]:
            todosIguais = False
            break

    if todosIguais:
        return False

    #utilizando for para verificar autenticidade do decimo digito
    soma = 0;
    for i in range (0,9):
        soma += (int(cpfpuro[i])*1) * (10-i)
    resto = (soma * 10) % 11
    if (resto == 10):
        resto = 0
    if (resto != int(cpfpuro[9])):
        return False

    #utilizando for para verificar autenticidade do decimo primeiro digito
    soma = 0
    for i in range (0,10):
        soma += (int(cpfpuro[i]*1)) * (11-i)
    resto = (soma * 10) % 11
    if (resto == 10):
        resto = 0
    if (resto != int(cpfpuro[10])):
        return False

    return True;


def checarEmail(email):
    # convertendo todas as letras para minusculas e removendo espaços
    # no inicio e final para facilitar o processo
    email = email.lower().strip()
    email2 = email

    # while para remover espaços eventuais dentro da string do email
    email = ""
    i = 0
    while (i < len(email2)):
        if (email2[i] != " "):
            email += email2[i]

        i = i + 1

    # invalida emails com quantidade minima de carateres nao atingida (ex: x@y.z)
    if len(email) < 5:
        return False

    # conta a quantidade de @s e ao mesmo tempo marca a posição do @
    posArroba = -1
    arrobaContagem = 0
    i = 0
    while i < len(email):
        if email[i] == "@":
            arrobaContagem += 1
            posArroba = i
        i += 1

    # invalida caso tenha mais de um @
    if arrobaContagem != 1:
        return False

    # invalida caso o arroba esteja na primeira ou ultima posição
    if posArroba == 0 or posArroba == (len(email) - 1):
        return False

    # verifica se há um ponto depois do @ (para qualquer domínio)
    temDominio = False
    i = posArroba + 1
    while i < len(email):
        if email[i] == ".":
            # garante que não é grudado após o @ nem o ultimo caractere
            if i > posArroba + 1 and i < len(email) - 1:
                temDominio = True
                break
        i += 1

    # invalida caso não haja dominio
    if not temDominio:
        return False
    # retorna True no final caso não caia nos Falses
    return True

#Declarando a lista de informações do usuario e as variaveis do quiz
userinfo= []
countA = 0
countB = 0
countC = 0
countD = 0
perfil = ''

#declarando a variavel nome do programa para eventuais mudanças
nomePrograma = "Nome da Empresa"

print (f"""Bem Vindo ao  Formulário de Iniciação da {nomePrograma}""")

#perguntando o nome do usuario e adcionando o nome digitado a lista
nomeusuario = input("Digite seu nome: ")
userinfo.append(nomeusuario)

#perguntando o cpf e o adicionando a lista
cpf = input("Digite seu CPF: ")
userinfo.append(cpf)
# while para deixar o usuario em loop caso digite CPF invalido (chamando função de checarCPF) (removendo da lista caso cpf invalido)
while checarCPF(cpf) == False:
    userinfo.pop()
    print ("CPF inválido")
    cpf = input("Digite seu CPF: ")
    userinfo.append(cpf)

#perguntando email do usuario e adicionando a lista
email = input("Digite seu email: ")
userinfo.append(email)
# while para deixar o usuario em loop caso digite email invalido (chamando função de checarEmail) (removendo da lista caso email invalido)
while checarEmail(email) == False:
    print("Email inválido")
    userinfo.pop()
    email = input("Digite seu email: ")
    userinfo.append(email)


print("Quiz de Perfil de Trabalhador")

#função para padronizar a resposta do Usuário evitando erros de contagem
def quiz(pergunta):
    pergunta = pergunta.lower()

    if pergunta == "a":
        return "A"
    elif pergunta == "b":
        return "B"
    elif pergunta == "c":
        return "C"
    elif pergunta == "d":
        return "D"
    else:
        return None

#função para apenas validar respostas entre a e d, aceitando minusculas ou maiusculas (não validando outras strings)
def validar(resposta):
    resposta = resposta.lower()

    if resposta == "a":
        return True
    elif resposta == "b":
        return True
    elif resposta == "c":
        return True
    elif resposta == "d":
        return True
    else:
        return False


p1 = input("""1. O que mais te motiva em um trabalho?

a) Resolver problemas e criar soluções inovadoras
b) Ajudar pessoas e causar impacto positivo na sociedade
c) Trabalhar com números, dados e análises lógicas
d) Lidar com tecnologia e entender como as coisas funcionam

Sua Resposta: """)

#deixando o usuario em loop caso a validação não ocorra
while not validar(p1):
    print("Insira uma Resposta Válida")
    p1 = input("Sua Resposta: ")

p2 = input("""2. Como você se sente em relação ao uso de novas tecnologias no trabalho?

a) Adoro aprender e explorar ferramentas novas
b) Gosto quando facilitam o contato humano
c) Prefiro quando são práticas e ajudam a tomar decisões
d) Quero entender como são feitas e talvez até criá-las

Sua Resposta: """)

#deixando o usuario em loop caso a validação não ocorra
while not validar(p2):
    print("Insira uma Resposta Válida")
    p2 = input("Sua Resposta: ")

p3 = input("""3. Qual dessas atividades você mais gostaria de fazer no futuro?

a) Criar conteúdo digital ou campanhas online
b) Atender e orientar pessoas em momentos importantes
c) Analisar informações para apoiar decisões estratégicas
d) Programar, automatizar processos ou desenvolver sistemas

Sua Resposta: """)

#deixando o usuario em loop caso a validação não ocorra
while not validar(p3):
    print("Insira uma Resposta Válida")
    p3 = input("Sua Resposta: ")

p4 = input("""4. Que tipo de ambiente de trabalho te atrai mais?

a) Dinâmico, criativo e com liberdade de ideias
b) Colaborativo, empático e voltado a pessoas
c) Estruturado, com metas claras e foco em resultados
d) Técnico, com desafios de inovação e aprendizado constante

Sua Resposta: """)

#deixando o usuario em loop caso a validação não ocorra
while not validar(p4):
    print("Insira uma Resposta Válida")
    p4 = input("Sua Resposta: ")

p5 = input("""5. Se você pudesse aprender algo novo agora, o que escolheria?

a) Marketing digital e redes sociais
b) Psicologia, gestão de pessoas ou coaching
c) Finanças, análise de dados ou gestão de negócios
d) Programação, inteligência artificial ou automação

Sua Resposta: """)

#deixando o usuario em loop caso a validação não ocorra
while not validar(p5):
    print("Insira uma Resposta Válida")
    p5 = input("Sua Resposta: ")

#definindo lista das respostas
respostas = [p1, p2, p3, p4, p5]

#utilizando for para calcular as escolhas do quiz  (leve variação para que no caso de empate priviliegie as areas Humanas)
for i in respostas:
    escolha = quiz(i)
    if escolha == "A":
        countA += 1.04
    elif escolha == "B":
        countB += 1.03
    elif escolha == "C":
        countC += 1.02
    elif escolha == "D":
        countD += 1.01


print("Seu Perfil de Trabalho é:")
#condicional para exibir o Resultado do Quiz
if countA > countB and countA > countC and countA > countD:
    print("""Perfil Criativo e Comunicativo:
→ Áreas recomendadas: Marketing Digital, UX/UI Design, Produção de Conteúdo e Comunicação Estratégica.""")
    perfil = "Criativo e Comunicativo"
    userinfo.append(perfil)

elif countB > countA and countB > countC and countB > countD:
    print("""Perfil Humano e Social:
→ Áreas recomendadas: Recursos Humanos, Psicologia Organizacional, Atendimento ao Cliente e Educação.""")
    perfil = ("Humano e Social")
    userinfo.append(perfil)

elif countC > countA and countC > countB and countC > countD:
    print("""Perfil Analítico e Estruturado:
→ Áreas recomendadas: Análise de Dados, Finanças, Planejamento Estratégico e Gestão de Projetos.""")
    perfil = "Analítico e Estruturado"
    userinfo.append(perfil)

elif countD > countA and countD > countB and countD > countC:
    print("""Perfil Técnico e Inovador:
→ Áreas recomendadas: Programação, Automação Industrial, Inteligência Artificial e Cibersegurança.""")
    perfil = "Técnico e Inovador"
    userinfo.append(perfil)


#Lista userinfo sendo gravada em um arquivo txt separado
with open("forms.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("\n=== NOVA INSCRIÇÃO ===\n")
    arquivo.write(f"Nome: {userinfo[0]}\n")
    arquivo.write(f"CPF: {userinfo[1]}\n")
    arquivo.write(f"Email: {userinfo[2]}\n")
    arquivo.write(f"Perfil: {userinfo[3]}\n")

# Confirmação da Inscrição sendo enviada ao arquivo
print(f"""Sua Inscrição foi Enviada:
        Nome: {nomeusuario}
        CPF: {cpf}
        Email: {email}
        Perfil:{perfil}""")