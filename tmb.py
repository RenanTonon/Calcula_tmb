print("*********Bem-vindo**********")
print(" Vamos calcular sua TMB ")

def duvidas():
    print("Antes de começar você sabe o que é Taxa metabolica basal(TMB):")
    resposta = int(input("(1)Sim (2)Não : "))

    if(resposta == 2):
        print("A Taxa Metabólica Basal (TMB) é o mínimo de energia necessária para manter as funções do organismo em repouso, como os batimentos cardíacos, a pressão arterial, a respiração e a manutenção da temperatura corporal")
    else:
        print("ok vamos calcular!!")
    print("Antes de começar você sabe o que é Necessidades Calóricas Diárias(NDC):")
    resposta2 = int(input("(1)Sim (2)Não : "))
    if(resposta2 == 2):
        print("Identificar, calcular e administrar o NDC (também conhecido como Necessidades Calóricas Diárias) é importante, visto que a saúde e o bem estar tem ganhado mais destaque a cada dia.")
    else:
        print("ok vamos calcular")
def tmb():
    massa_str = input(" Qual seu peso ( em KG ): ")
    massa = int(massa_str)
    print(massa," Kg ")

    altura_str = input("Qual sua altura ( em Centimentros ): ")
    altura = int(altura_str)
    print(altura," centimentos ")

    idade_str = input("Qual sua idade : ")
    idade = int(idade_str)
    print(idade," anos ")
    print("(1)masculino (2)feminino")
    genero_xx = input("Qual seu sexo femenino ou masculino : ")
    genero = int(genero_xx)
    femenino = int(genero == 2)
    masculino = int(genero == 1)

    if(femenino) :
         tmb_str = 665 + (9.6 * massa) + (1.7 * altura ) - (4.7 * idade)
         tmb_fem = int(tmb_str)
         print("Seu TMB é : ", tmb_fem," /kcal")
         #calculo NDC da mulher
         sedentario_m = tmb_fem + (0.20*tmb_fem)
         saudavel_m =  tmb_fem + (0.30*tmb_fem )
         atleta_m =    tmb_fem + (0.40*tmb_fem)

         print("Agora vamos calcular sua NDC ,para isso precisamos saber se você é: ")
         print("(1)sendentario (2)saudavel (3)atleta")
         pratica =int(input("Você é :"))
         if(pratica == 1):
                         print("Seu NDC é :" , sedentario_m," /kcal")
         elif(pratica == 2):
                         print("Seu NDC é :" , saudavel_m," /kcal")
         else:
                         print("Seu NDC é : ", atleta_m," /kcal")
    else:
         if( masculino ):
              tmb_strm = 66 + (13.7 * massa) + (5 *altura ) - (6.8 *idade)
              tmb_mac = int(tmb_strm)
              print("Seu TMB é :", tmb_mac," /kcal")
              #calculo NDC do homem
              sedentario_h = tmb_mac + (0.25*tmb_mac)
              saudavel_h =  tmb_mac + (0.35 *tmb_mac)
              atleta_h =    tmb_mac+ (0.45*tmb_mac)

              print("Agora vamos calcular sua NDC ,para isso precisamos saber se você é: ")
              print("(1)sendentario (2)saudavel (3)atleta")
              pratica =input("Você é :")

              if(pratica == 1):
                  print("Seu NDC é : ",sedentario_h," /kcal" )
              elif(pratica == 2):
                  print("Seu NDC é : ", saudavel_h," /kcal")
              else:
                  print("Seu NDC é : ", atleta_h," /kcal")


    print("Fim")
    ''
duvidas();
tmb();
