import pandas as pd
import numpy as np
import random

# Генерация данных
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание пустого DataFrame с нулями
one_hot = pd.DataFrame(0, index=np.arange(len(data)), columns=data['whoAmI'].unique())

# Заполнение DataFrame единицами по соответствующим столбцам
for i, val in enumerate(data['whoAmI']):
    one_hot.loc[i, val] = 1

# Вывод первых строк результата
print(one_hot.head())
