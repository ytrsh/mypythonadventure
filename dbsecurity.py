import sqlite3 as sql

db = sql.connect("databases/dbsecurity.sqlite3")
im = db.cursor()

im.execute("""CREATE TABLE IF NOT EXISTS 'users'(kullanici_adi,password)""")
datas = [
        ("erenarici1","123456"),
        ("erenarc1","123456"),
        ("ernarici1","123")
]
for i in datas:
    im.execute("""INSERT INTO 'users' VALUES %s """ % (i,))
db.commit()

while True:
   id = input("Username >>> ")
   pw = input("Password >>> ")

   im.execute("""SELECT * FROM 'users' WHERE kullanici_adi=? AND password=?""",(id,pw))
   data = im.fetchone()

   if data:
       print("welcome {}".format(data[0]))
       break
   else:
       print("wrong datas \nTRY AGAIN")
       