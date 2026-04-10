import pandas as pd
import matplotlib.pyplot as plt

# Dados simulados
dados = {
    "mes": ["Jan", "Fev", "Mar", "Abr"],
    "cancelamentos": [50, 45, 30, 20]
}

df = pd.DataFrame(dados)

# Mostrar dados
print(df)

# Gráfico
df.plot(x="mes", y="cancelamentos", kind="bar")
plt.title("Cancelamento de Clientes por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de Cancelamentos")
plt.show()
