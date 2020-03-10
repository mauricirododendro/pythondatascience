Vendite={'prezzo':3.24,'numero':4,'nome':'Anna'}
#{}
Ven_rapporto='{} ha comprato {} oggetti al prezzo di {} ciascuno per un tot di {}'
print(Ven_rapporto.format(Vendite['nome'],Vendite['numero'],Vendite['prezzo'],Vendite['numero']*Vendite['prezzo']))
