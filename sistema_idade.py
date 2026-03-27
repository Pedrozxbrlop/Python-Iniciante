#Sistema de verificação de Idade pra entrar em um parque de diversões!
Idade = int(input("Qual a sua idade? ")) # O input está sendo usado para perguntar.
if Idade < 4: # if = se. Traduzindo: Se Idade for menor que 4, vai printar aquilo ali debaixo.
    print("Vc é um bebe, não pode entrar!")
elif Idade < 18: # elif = senão se. Traduzindo: Senão se Idade for menor que 18, vai printar isso abaixo.
    print("Vc é menor de idade, poderá ir em quase todos os brinquedos, menos na Big Tower. Divirta-se!")
elif Idade == 18:
    print("Vc tem exatamente 18 anos, pode entrar e divirta-se em todos os brinquedos!")
elif Idade < 60:
    print("Vc é maior de idade, um adulto! Pode entrar e divirta-se em todos os brinquedos!")
elif Idade >= 60:
    print("Pode entrar senhor!")
else: ("Tente novamente") # else = senão. Ou seja, senão for nada de tudo acima vai printar: Tente novamente.

# if= se, elif= senão se, else= senão.
