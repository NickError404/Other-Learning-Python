import pandas as pd

data = {
  'Alunos': ['caio', 'jorge', 'ana', 'maria', 'julia', 'clara', 'yuna'],
  'Idade': [16, 15, 43, 12, 32, 12, 45],
  'Nota': [8, 5, 10, 7, 5, 3, 8]
}

df = pd.DataFrame(data, columns=['Alunos', 'idade', 'Nota'])

print(df.max())