# relação de assosiação entre classes

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('claudio')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()

# associando escritor com caneta
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# essa é uma associação fraca, onde um objeto não depende do outro para existir
# por exemplo, seu eu apagar o escritor, a caneta vai continuar a existir, como mostrado abaixo
del escritor
#print(escritor)
print(caneta.marca)     # caneta ainda existe