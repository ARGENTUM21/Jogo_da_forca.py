"""print("Jogo da Forca - Filmes")
print(" O ")
print(" | ")
print("/|")
print("/|\\")
print("/")
print("/ \\")
print("Game Over, você foi enforcado!")
print(" O ")
print("/|\\")
print("/ \\")"""

import random 
lista_palavras = ["Star Wars", "Ada Lada", "Karater kid"]
total_palavras = len(lista_palavras) - 1
posicao_palavra = random.randint(0, total_palavras)
palavra_secreta = lista_palavras[posicao_palavra].upper()
print(palavra_secreta)
palavra_correta = list()
for i in range(0, len(palavra_secreta)):
  palavra_correta.append("_")

lista_posicoes_letra = list()

print("Você pode chutar até cinco letras.")
qtd_erros = 0
for k in range(1, 7):
  letra = str(input("Qual a letra? ")).upper()
  #print(letra)
  if k < 6:
    if letra in palavra_secreta:
      for j in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[j]:
          lista_posicoes_letra.append(j)
      for posicao in  lista_posicoes_letra:
        palavra_correta.pop(posicao)
        palavra_correta.insert(posicao, letra)
      
      lista_posicoes_letra.clear()
      print(palavra_correta)
      
    else:
      qtd_erros += 1
      if qtd_erros == 1:
        print("Você errou uma vez, tente novamente!")
        print(" O ")
      elif qtd_erros == 2:
        print("Você errou duas vez, tente novamente!")
        print(" O ")
        print(" | ")
      elif qtd_erros == 3:
        print("Você errou três vez, tente novamente!")
        print(" O ")
        print("/|")
      elif qtd_erros == 4:
        print("Você errou quatro vez, tente novamente!")
        print(" O ")
        print("/|\\")
      elif qtd_erros == 5:
        print("Você errou cinco vez, tente novamente!")
        print(" O ")
        print("/|\\")
        print("/")
        print("Você é obrigado a falar a palavra completa.")
        palavra_completa = str(input("Informe a palavra secreta")).upper()
        if palavra_completa == palavra_secreta:
          print("Você ganhou o jogo!")
        else: 
          print("Você errou seis vez!")
          print("Game Over, você foi enforcado!")
          print(" O ")
          print("/|\\")
          print("/ \\")
  else:
    print("Você é obrigado a falar a palavra completa.")
    palavra_completa = str(input("Informe a palavra secreta")).upper()
    if palavra_completa == palavra_secreta:
      print("Você ganhou o jogo!")
    else: 
      print("Game Over, você foi enforcado!")
      print(" O ")
      print("/|\\")
      print("/ \\")
  #print(lista_posicoes_letra)