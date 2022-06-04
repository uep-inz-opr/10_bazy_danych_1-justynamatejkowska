import csv, sqlite3

if __name__ == "__main__":

  !curl https://raw.githubusercontent.com/khashishin/repozytorium_z_plikiem_polaczenia/main/polaczenia_duze.csv > polaczenia_duze.csv

  sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
  cur = sqlite_con.cursor()

  cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);''') 

  with open('polaczenia_duze.csv','r') as fin: 
      reader = csv.reader(fin, delimiter = ";") 
      next(reader, None)
      rows = [x for x in reader]
      cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows) #wartości oznaczane 
      sqlite_con.commit() 

  sqlite_con
  cursor=sqlite_con.cursor()
  cursor.execute("Select sum(duration) from polaczenia")
  result = cursor.fetchone()

  res = int(''.join(map(str, result)))

print(str(res))