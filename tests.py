import pytest

from module import Moeda, Aporte, Saque, Ativo

@pytest.fixture
def brl():
    return Moeda("Real", "BRL")

@pytest.fixture
def btc():
    return Moeda("Bitcoin", "BTC")

@pytest.fixture
def eth():
    return Moeda("Ethereum", "ETH")

@pytest.fixture
def aporte_btc(btc, brl):
    return Aporte(btc, 1.0, brl, 1000.0, "12/01/2022")

@pytest.fixture
def aporte_eth(eth, brl):
    return Aporte(eth, 1.5, brl, 200.0, "12/01/2022")

@pytest.fixture
def saque_btc(btc, brl):
    return Saque(brl, 1000.0, btc, 1.0, "12/01/2022")

@pytest.fixture
def saque_eth(eth, brl):
    return Saque(brl, 250.0, eth, 1.0, "12/01/2022")

def test_deve_criar_ativo_se_moeda_do_ativo_for_igual_moeda_do_aporte(btc, aporte_btc):
    ativo_btc = Ativo(btc, aporte_btc)
    assert ativo_btc.quantidade == aporte_btc.qtd_md

def test_nao_deve_criar_ativo_se_moeda_do_ativo_for_diferente_moeda_do_aporte(btc, aporte_eth):
    with pytest.raises(ValueError):
        ativo_btc = Ativo(btc, aporte_eth)
