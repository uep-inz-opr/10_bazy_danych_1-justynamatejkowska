import csv, sqlite3
if __name__ == "__main__":
    
    sqlite_con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = sqlite_con.cursor()

    cur.execute('''CREATE TABLE polaczenia (from_subscriber data_type INTEGER, 
                      to_subscriber data_type INTEGER, 
                      datetime data_type timestamp, 
                      duration data_type INTEGER , 
                      celltower data_type INTEGER);''') # use your column names here

    #Otwieramy plik.csv i przerzucamy go w najprostszy sposób do naszej nowo utworzonej bazy sqlite
    with open('polaczenia_duze.csv','r') as fin: 
        # csv.DictReader uses first line in file for column headings by default
        reader = csv.reader(fin, delimiter = ";") 
        next(reader, None) 
        rows = [x for x in reader]
        cur.executemany("INSERT INTO polaczenia (from_subscriber, to_subscriber, datetime, duration , celltower) VALUES (?, ?, ?, ?, ?);", rows) #wartości oznaczane 
        sqlite_con.commit() 

    sqlite_con
    cursor=sqlite_con.cursor()
    cursor.execute("Select sum(duration) from polaczenia")
    result = cursor.fetchall()