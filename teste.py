nome = input("Olá, seja muito bem-vindo(a). Para prosseguirmos, insira seu nome: ")
print(f"Muito bem, {nome}! é um prazer ter você conosco.")

idade = input("Ajude-nos a conhecê-lo(a) melhor. Informe sua idade: ")
print("Maravilha! {} anos é uma ótima idade para se começar aprender Pyhton. ☜(ﾟヮﾟ☜)" .format(idade))

mediador = input("""
Em qual das alternativas abaixo você melhor se encaixa ?
                 
A) Iniciante
B) Intermediário
C) Avançado               
""")

if mediador == "A" or mediador == "a":
    print("""
Ok! Pronto para começar uma nova jornada ? """) 
    caso_A = input("""
sim ou com certeza ? (☞ﾟヮﾟ)☞
""")
    print(f"{caso_A} ? é assim que se fala! vamos lá! ^(●'◡'●)^")
    
elif mediador == "B" or mediador == "b":
    print("Excelente! o processo de aprendizagem será ainda mais tranquilo para você.")
elif mediador == "C" or mediador == "c":
    print("Que maravilha! revisar o conteúdo para solidificar o conhecimento é sempre uma ótima escolha.")



