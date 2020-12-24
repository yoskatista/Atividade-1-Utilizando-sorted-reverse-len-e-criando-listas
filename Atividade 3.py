#Criar uma lista com 5 lugares PG85
lista = ['Brasil','Argentina','Bolivia','Chile','Paraguai']
print('A lista original é: {}'.format(lista))

#Colocar a lista em ordem alfabética com sorted()
OrdemAlfabética = sorted(lista)
print('\nA lista em Ordem alfabética é: {}'.format(OrdemAlfabética))

#Agora a ordem é inversa
lista.sort(reverse=True)
print('A lista em ordem contrária ficará {}'.format(lista))

#voltar com a lista no formato padrão ABC
lista.sort(reverse=False)

#utilizar o len para contar o número de itens na lista.
print('\nO numero de itens disponiveis na lista é: {}'.format(len(lista)))

listinha = str(input('\nJa que temos uma lista acima de países da america do sul, diga para gente outros países proximos:'))
listinha2 = str(input('Fale mais um!, mas não vale repetir!'))
listinha3 = str(input('Diga o ultimo país'))
itens = [listinha, listinha2, listinha3,]
print('A sua lista é:{} e {}'.format(itens,lista))