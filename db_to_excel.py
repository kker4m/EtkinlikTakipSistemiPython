import sqlite3
import pandas as pd

conn = sqlite3.connect('rozetler.db')
df = pd.read_sql_query("SELECT * FROM uyeler", conn)

df.to_excel('uyeler.xlsx', index=False)

conn.close()
