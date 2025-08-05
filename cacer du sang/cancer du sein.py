import pandas as pd
import numpy as np

np.random.seed(42)  # reproductibilité

n = 20  # nombre de lignes

df_test = pd.DataFrame({
    'id': np.arange(1000, 1000 + n),
    'diagnosis': np.random.choice([0, 1], size=n, p=[0.7, 0.3]),  # 70% bénin
    'radius_mean': np.random.uniform(6.0, 28.0, size=n),
    'texture_mean': np.random.uniform(10.0, 40.0, size=n),
    'perimeter_mean': np.random.uniform(40.0, 180.0, size=n),
    'area_mean': np.random.uniform(100.0, 2400.0, size=n),
    'smoothness_mean': np.random.uniform(0.05, 0.15, size=n),
    'compactness_worst': np.random.uniform(0.05, 1.0, size=n),
})

# Affichage
print(df_test.head())

# Enregistrement (facultatif)
df_test.to_csv("test_dataset.csv", index=False)
