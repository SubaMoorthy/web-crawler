from  key_change import custom_dictionary
import psycopg2

required_keys = ['player_name','current_team','goals'];

def change_dict_key(data):
    row  =  dict(data)
    for key in row.keys():
        try:
            new_key = key.replace(key,custom_dictionary[key])
            if new_key != key:
                row[new_key] = row[key]
                del row[key]
        except: 
            pass
    filter_dict(row)
    
def filter_dict(row):
    filtered_values = { req_key: row[req_key] for req_key in required_keys }
    insert_into_db(filtered_values)
    
def insert_into_db(row_data):
    connect_DB();
    column_data = ''
    'required array has the column names to be inserted '
    for i in range (0 , len(required_keys)):
        column_data += '%(' + required_keys[i] + ')s'
        if i != len(required_keys)-1:
            column_data += ','

    'insert from python list into postgres'
    cursor.execute("INSERT INTO nasl VALUES (" + column_data+ ")", row_data)
    conn.commit()

def connect_DB():
    HOSTNAME = 'localhost'
    DBNAME = 'webscraping'
    USER = 'postgres'
    PASSWORD = 'postgres'
    conn_string = "host=\'"+ HOSTNAME + "\' dbname=\'" + DBNAME +'\' user=\'' + USER + '\' password=\''+ PASSWORD + '\''
    global conn
    conn = psycopg2.connect(conn_string)
    global cursor
    cursor = conn.cursor()