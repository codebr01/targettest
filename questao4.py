faturamento_mensal_por_estado = [
  {
    "estado":'SP',
    "faturamento": 67836.45,
    "percentual": 0.0
  },
  {
    "estado":'RJ',
    "faturamento": 36678.66,
    "percentual": 0.0
  },
  {
    "estado":'MG',
    "faturamento": 29229.88,
    "percentual": 0.0 
  },
  {
    "estado":'ES',
    "faturamento": 27165.48,
    "percentual": 0.0 
  },
  {
    "estado":'Outros',
    "faturamento": 19849.53,
    "percentual": 0.0 
  },
]

def calcularValorTotalMensal(faturamento_mensal_por_estado):
    valor_total_mensal = 0
    for estado in faturamento_mensal_por_estado:
        valor_total_mensal += estado["faturamento"]
    return valor_total_mensal

def calcularPercentualCadaEstado(valor_total_mensal):
    for estado in faturamento_mensal_por_estado:
        estado["percentual"] = (estado["faturamento"] / valor_total_mensal) * 100

valor_total_mensal = calcularValorTotalMensal(faturamento_mensal_por_estado)

calcularPercentualCadaEstado(valor_total_mensal)

for estado in faturamento_mensal_por_estado:
    print(f"Estado: {estado['estado']} - Percentual: {estado['percentual']:.2f}%")