import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\PC\Desktop\ai\AAPL.CSV')
print(f"AAPL - Pandas:")
print(f"  Lignes: {len(df)}, Colonnes: {len(df.columns)}")
print(f"  5 premières valeurs:")
print(df.head())

data = df.select_dtypes(include=[np.number]).to_numpy()
print(f"\nAAPL - Numpy:")
print(f"  Shape: {data.shape}")
print(f"  Moyenne: {np.mean(data):.2f}")


if 'Close' in df.columns:
    plt.plot(df.index[:50], df['Close'][:50], 'b-', linewidth=2, label='Close Price')
    plt.grid(True, alpha=0.3)

plt.show()

if 'Close' in df.columns and len(df) >= 10:
    plt.bar(range(10), df['Close'][:10], color='green', alpha=0.7)
plt.figure()


if 'Open' in df.columns and 'Close' in df.columns and len(df) >= 30:
    plt.scatter(df['Open'][:30], df['Close'][:30], color='red', alpha=0.6)

plt.show()

if 'Volume' in df.columns:
    plt.hist(df['Volume'], bins=15, color='purple', alpha=0.7)
plt.show()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\PC\Desktop\ai\StudentPerformance.csv')
print(f"StudentPerformance - Pandas:")
print(f"  Lignes: {len(df)}, Colonnes: {len(df.columns)}")
print(f"  5 premières valeurs:")
print(df.head())


data = df.select_dtypes(include=[np.number]).to_numpy()
print(f"\nStudentPerformance - Numpy:")
print(f"  Shape: {data.shape}")
print(f"  Moyenne: {np.mean(data):.2f}")

if 'Performance Index' in df.columns:
    plt.plot(df.index[:50], df['Performance Index'][:50], 'b-', linewidth=2, label='Performance Index')
    plt.grid(True, alpha=0.3)
plt.figure()   
  
if 'Performance Index' in df.columns and len(df) >= 10:
    plt.bar(range(10), df['Performance Index'][:10], color='green', alpha=0.7)

    plt.grid(True, alpha=0.3)

plt.figure()


if 'Performance Index' in df.columns:
    plt.hist(df['Performance Index'], bins=15, color='purple', alpha=0.7)
    plt.grid(True, alpha=0.3)

plt.show()
