import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

def get_data():
    df: DataFrame = pd.read_csv('ecommerce_data.csv')
    return df

# Fonksiyon sonucunu bir değişkene atayın
df = get_data()

# Histogram oluşturun
df['time_of_day'].hist(bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Time of Day')
plt.ylabel('Frequency')
plt.title('Histogram of Time of Day')
plt.show()
