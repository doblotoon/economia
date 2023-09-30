import ipeadatapy as ip
from bcb import sgs

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

ip.list_series('Caged')
ip.describe('CAGED12_SALDON12')

#  Importa a série

caged = ip.timeseries('CAGED12_SALDON12',yearGreaterThan = 2020)

# Plota a série

sns.set_theme()

plt.figure(figsize = (15,10))

sns.lineplot(x = caged.index, y = caged['VALUE (Pessoa)']).set(title = "Saldo de empregados admitidos- Novo Caged")

