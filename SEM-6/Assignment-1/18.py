import pandas as pd
import matplotlib.pyplot as plt
c_to_k = lambda c: c + 273.15

data = {'Celsius': list(range(-10, 41, 10))}
df = pd.DataFrame(data)

df['Kelvin'] = df['Celsius'].apply(c_to_k)
print(df)
plt.plot(df['Celsius'], df['Kelvin'], marker='o', linestyle='-')
plt.xlabel('Celsius')
plt.ylabel('Kelvin')
plt.title('Celsius to Kelvin Conversion')
plt.grid()
plt.show()
