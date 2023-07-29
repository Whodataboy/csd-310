#pysports_join_queries.py
#Brendan Spurlock
#July 29, 2023
#Assignment 9.2


#import statements
import mysql.connector
from mysql.connector import errorcode

#DB Config
config = {
    "user": "root",
    "password": "IBe327512Man",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
#try/catch for DB errors
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    
    #join query
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    
    #gets the results
    players = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS --")

    for player in players:
        #displays the results
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
        input("\n\n Press any key to continue...")

except mysql.connector.Error as err:

#displays one of the following depending on error type
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

#close DB
finally:
    db.close()