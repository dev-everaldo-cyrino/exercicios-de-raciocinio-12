print('................................................................')
num = input('digite uma data no formato DD/MM/AAAA entre os anos 2000--2031: ')
print('................................................................')
dia = ['um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatoze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte','vinte e um','vinte e dois','vinte e três','vinte e quatro','vinte e cinco','vinte e seis','vinte e sete',' vinte e oito','vinte e nove','trinta','trinta e um']

mes = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

if len(num) > 10 or len(num) < 10:
    print('ERRO: data invalida !')
else:
    ndia = int(num[0]+num[1])
    nmes = int(num[3]+num[4])
    nano = int(num[8]+num[9])
    print('DATA: {}  de  {}  de  dois mil e {}'.format(dia[ndia-1],mes[nmes-1],dia[nano-1]))
