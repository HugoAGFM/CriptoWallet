class Moeda:
    def __init__(self, nome: str, codigo: str):
        self.nome = nome
        self.codigo = codigo

    def __str__(self):
        return self.codigo


class Aporte:
    def __init__(self, moeda_origem, moeda_destino, qtd_mo, qt_md, data_aporte):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.qtd_mo = qtd_mo
        self.qtd_md = qt_md
        self.data_aporte = data_aporte

    @property
    def aporte(self):
        aporte = {"Moeda destino": self.moeda_destino, "Quantidade moeda destino": self.qtd_md,
                  "Moeda origem": self.moeda_origem, "Quantidade moeda origem": self.qtd_mo,
                  "Data aporte": self.data_aporte}
        return aporte


class Ativo:
    def __init__(self, moeda: Moeda, aporte: Aporte):
        self.moeda = moeda
        self.movimentacoes = [aporte]
        self.quantidade = aporte.aporte["Quantidade moeda destino"]

    def __str__(self):
        return f"Você possui {self.quantidade} {self.moeda.codigo}"


class Carteira:
    def __init__(self, ativo: Ativo):
        self.carteira_ativos = [ativo]

    def adiciona_ativo(self, ativo: Ativo):
        self.carteira_ativos.append(ativo)

    def aporta(self, ativo: Ativo, aporte: Aporte):
        pass

    def saca(self):
        pass

    def retorna_ativos_na_carteira(self):
        for ativo in self.carteira_ativos:
            print(ativo)
