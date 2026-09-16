print(df.isnull().sum)    # jumlah data kosong setiap kolom

df['terjual'] = df['terjual'].fillna(0)   # isi kekosongan dengan 0
df = df.dropna(subset=['menu'])     # hapus baris jika kolom menu kosong
