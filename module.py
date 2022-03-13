class Moeda:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return self.codigo


class Movimentacao:
    def __init__(self, moeda_destino, qtd_md, moeda_origem, qtd_mo, data_movimentacao):
        self.moeda_destino = moeda_destino
        self.qtd_md = qtd_md
        self.moeda_origem = moeda_origem
        self.qtd_mo = qtd_mo
        self.data_movimentacao = data_movimentacao

    @property
    def movimentacao(self):
        movimentacao = {"Moeda destino": self.moeda_destino, "Quantidade moeda destino": self.qtd_md,
                        "Moeda origem":  self.moeda_origem, "Quantidade moeda origem": self.qtd_mo,
                        "Data movimentacao": self.data_movimentacao}
        return movimentacao


class Aporte(Movimentacao):
    pass


class Saque(Movimentacao):
    pass


class Ativo:
    def __init__(self, moeda: Moeda, aporte: Aporte):
        self.moeda = moeda
        self.movimentacoes = []
        self.quantidade = 0.0
        self.aporta(aporte)

    def __str__(self):
        return f"Você possui {self.quantidade} {self.moeda.codigo}"

    def aporta(self, aporte: Aporte):
        moeda_eh_igual = aporte.movimentacao["Moeda destino"] == self.moeda
        if moeda_eh_igual:
            self.movimentacoes.append(aporte)
            self.quantidade += aporte.movimentacao["Quantidade moeda destino"]
        else:
            raise ValueError("Moeda do aporte não corresponde a moeda do ativo")

    def saca(self, saque: Saque):
        moeda_eh_igual = saque.movimentacao["Moeda origem"] == self.moeda
        possui_qtd = saque.movimentacao["Quantidade moeda origem"] <= self.quantidade

        if moeda_eh_igual:
            if possui_qtd:
                self.movimentacoes.append(saque)
                self.quantidade -= saque.movimentacao["Quantidade moeda origem"]
            else:
                raise ValueError("Valor do saque maior que a quantidade disponível")
        else:
            raise ValueError("Moeda do saque não corresponde a moeda do ativo")


class Carteira:
    def __init__(self, ativo: Ativo):
        self.carteira_ativos = [ativo]

    def adiciona_ativo(self, ativo: Ativo):
        self.carteira_ativos.append(ativo)

    def retorna_ativos_na_carteira(self):
        for ativo in self.carteira_ativos:
            print(ativo)
