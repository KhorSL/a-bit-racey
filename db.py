import sqlite3

class Database:
    def __init__(self):
        print ('Initializing Database...')
        self.connection()


    def connection(self):
        print ('Setting up connection...')
        self.conn = sqlite3.connect('a_bit_racey_db.db')
        self.cursor = self.conn.cursor()


    def setup(self):
        # Preparing the queries for execution
        # Basically creating the table if it does not exist
        # and inserting the admin player if it does not exist
        table_player = "CREATE TABLE IF NOT EXISTS Player (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), highscore INTEGER, coins INTEGER, gems INTEGER);"
        table_vehicle = "CREATE TABLE IF NOT EXISTS Vehicle (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255) NOT NULL);"
        table_player_vehicle = "CREATE TABLE IF NOT EXISTS Player_Vehicle (player_id INTEGER, vehicle_id INTEGER, FOREIGN KEY (player_id) REFERENCES Player(id), FOREIGN KEY (vehicle_id) REFERENCES Vehicle(id), PRIMARY KEY (player_id, vehicle_id));"
        admin_player = "INSERT OR IGNORE INTO Player (id, name, highscore, coins, gems) VALUES (1,'admin',0,0,0);"
        
        self.cursor.execute(table_player)
        self.cursor.execute(table_vehicle)
        self.cursor.execute(table_player_vehicle)
        self.cursor.execute(admin_player)
        self.conn.commit()

    def get_highscore(self, player_id):
        stmt = "SELECT highscore FROM Player WHERE id = ?"
        args = (player_id, )
        self.cursor.execute(stmt, args)
        return self.cursor.fetchone()[0]

    def update_highscore(self, player_id, highscore):
        stmt = "UPDATE Player SET highscore = ? WHERE id = ? "
        args = (highscore, player_id, )
        self.cursor.execute(stmt, args)
        self.conn.commit()
