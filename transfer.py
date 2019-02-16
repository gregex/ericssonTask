import pandas as pd
import sys
import psycopg2 as pg

if len(sys.argv) == 1:
    print(">you didn't specify a file!")

#ucitaj samo bitne stupce
df = pd.read_excel(sys.argv[1], sheet_name=1, usecols=[0,1,2,3])

#makni redove koji nemaju bar jednu informaciju osim kljuca
df = df.dropna(thresh=2)

#makni pratece razmake
df['Naziv'] = df['Naziv'].apply(lambda x: str(x).strip() if x else None)

#spoji se na bazu
try:
    conn = pg.connect("dbname='oprema' user='ericsson' host='localhost' password='qwerty'")
    cur = conn.cursor()
    print(">connected to DB successfully")
except:
    print("I am unable to connect to the database")

#prebaci podatke u bazu
for row in df.iterrows():
    index, data = row
    cur.execute("INSERT INTO PlannedEquipment VALUES (%s,%s,%s,%s)",[d if str(d)!='nan' else None for d in data])
    conn.commit()
    print(">data inserted")

cur.close()
conn.close()
print(">connection with DB stopped")