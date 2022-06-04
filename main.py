import csv, sqlite3

if __name__ == "__main__":

  sqlite= sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
  cur = sqlite.cursor()

  cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                    to_subscriber data_type INTEGER, 
                    datetime data_type timestamp, 
                    duration data_type INTEGER , 
                    celltower data_type INTEGER);''') 

  with open('polaczenia_duze.csv','r') as fin: 
      reader = csv.reader(fin, delimiter = ";") 
      next(reader, None)
      rows = [x for x in reader]
      cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows)

  sqlite
  cursor=sqlite.cursor()
  cursor.execute("Select sum(duration) from polaczenia")
  result = cursor.fetchone()

  res = int(''.join(map(str, result)))

print(str(res))