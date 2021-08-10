from tests.main import Usuario, Lance, Leilao

gui = Usuario('Gui', 500.0)
yuri = Usuario('Yuri', 500.0)

lance_do_yuri = Lance(yuri, 150.0)
lance_do_gui = Lance(gui, 200.0)

leilao = Leilao('Celular')

leilao.propoe(lance_do_yuri)
leilao.propoe(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

# avaliador = Avaliador()
# avaliador.avalia(leilao)

print(f'O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}')


