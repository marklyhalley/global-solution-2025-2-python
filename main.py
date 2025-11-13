
def checarCPF(cpf):
    cpfpuro = ""
    i = 0
    #utilizando while para
    while i < len(cpf):
        if cpf[i] >= "0" and cpf[i] <= "9":
            cpfpuro += cpf[i]
        i += 1

    # verificar se o cpf contem 11 caracteres (após remoção de não numerais) (condição 1)
    if (len(cpfpuro) != 11):
        return False;

    #utilizando for para verificar se todos os caracteres são iguais (condição 2)
    todosIguais = True;
    for i in range (1,11):
        if cpfpuro[i] != cpfpuro[0]:
            todosIguais = False;
            break;

    if todosIguais:
        return False;

    #utilizando for para verificar autenticidade do decimo digito
    soma = 0;
    for i in range (0,9):
        soma += (int(cpfpuro[i])*1) * (10-i);
    resto = (soma * 10) % 11;
    if (resto == 10):
        resto = 0;
    if (resto != int(cpfpuro[9])):
        return False;

    #utilizando for para verificar autenticidade do decimo primeiro digito
    soma = 0;
    for i in range (0,10):
        soma += (int(cpfpuro[i]*1)) * (11-i);
    resto = (soma * 10) % 11;
    if (resto == 10):
        resto = 0;
    if (resto != int(cpfpuro[10])):
        return False;

    return True;


def checarEmail(email):
    # convertendo todas as letras para minusculas e removendo espaços
    # no inicio e final para facilitar o processo
    email = email.lower().strip();
    email2 = email

    # while para remover espaços eventuais dentro da string do email
    email = ""
    i = 0
    while (i < len(email2)):
        if (email2[i] != " "):
            email += email2[i];

        i = i + 1;

    # invalida emails com quantidade minima de carateres nao atingida (ex: x@y.z)
    if len(email) < 5:
        return False;

    # conta a quantidade de @s e ao mesmo tempo marca a posição do @
    posArroba = -1;
    arrobaContagem = 0;
    i = 0
    while i < len(email):
        if email[i] == "@":
            arrobaContagem += 1
            posArroba = i;
        i += 1

    # invalida caso tenha mais de um @
    if arrobaContagem != 1:
        return False;

    # invalida caso o arroba esteja na primeira ou ultima posição
    if posArroba == 0 or posArroba == (len(email) - 1):
        return False;

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

userinfo= []

nomePrograma = "Programa Teste"

print (f""" Bem Vindo ao {nomePrograma} """)

nomeusuario = input("Digite seu nome: ")
userinfo.append(nomeusuario)

cpf = input("Digite seu CPF: ")
userinfo.append(cpf)
# while para deixar o usuario em loop caso digite CPF invalido (chamando função de checarCPF)
while checarCPF(cpf) == False:
    userinfo.pop()
    print ("CPF inválido")
    cpf = input("Digite seu CPF: ");
    userinfo.append(cpf)

email = input("Digite seu email: ");
userinfo.append(email)
while checarEmail(email) == False:
    print("Email inválido")
    userinfo.pop()
    email = input("Digite seu email: ");
    userinfo.append(email)

print(userinfo)
