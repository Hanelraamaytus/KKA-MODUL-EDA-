print(df.duplicated().sum())  # jumlah baris duplikat
df = df.frop_duplicates()

df['harga'] = df['harga'].astype(int)  #memastikan tipe data harga adalah integer
print(df.dtypes)