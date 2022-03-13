from module import Moeda, Aporte, Saque, Ativo, Carteira

brl = Moeda("Real", "BRL")
btc = Moeda("Bitcoin", "BTC")
eth = Moeda("Ethereum", "ETH")

aporte1 = Aporte(btc, 1.0, brl, 1000.0, "12/01/2022")
aporte2 = Aporte(eth, 1.5, brl, 200.0, "12/01/2022")

ativo_btc = Ativo(btc, aporte2)
# ativo_eth = Ativo(eth, aporte2)

# aporte3 = Aporte(eth, 2.0, brl, 2500.0, "12/01/2022")
# saque1 = Saque(brl, 1000.0, eth, 1.0, "12/01/2022")
#
# ativo_eth.saca(saque1)
#
# print(ativo_eth)

# carteira_hugo = Carteira(ativo_btc)
# carteira_hugo.adiciona_ativo(ativo_eth)
#
# carteira_hugo.retorna_ativos_na_carteira()
#
# carteira_hugo.aporta(ativo_eth, aporte3)
#
# carteira_hugo.retorna_ativos_na_carteira()
