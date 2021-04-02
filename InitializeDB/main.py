import mysql.connector
from mysql.connector import errorcode

def initialize_db():
    try:
        con = mysql.connector.connect(
            host="us-cdbr-east-03.cleardb.com",
            user="b799abdf4a1604",
            password="b68b32bc",
            database="heroku_3916ab6d68a088d"
        )

        cursor = con.cursor()

        # cursor.execute("CREATE TABLE player (name varchar(255) NOT NULL PRIMARY KEY, password varchar(255) NOT NULL, preferred_colour varchar(255) NOT NULL, role varchar(255) NOT NULL);")
        cursor.execute("INSERT INTO player VALUES ('admin', '$2a$12$hB0DoJ2PAIEdUmWiQh.9d.f9IuO/L85ZY.Gxf/iHbnyTWgZM0zgS2', 'CAFFEE', 'ROLE_ADMIN');")
        cursor.execute("INSERT INTO player VALUES ('maex', '$2a$12$6.McsTs654WOtJTB8ItKK.ARPo05Wv2ErCKiXKbXudvjE/EGJrZTy', 'FCBA03', 'ROLE_PLAYER');")
        cursor.execute("INSERT INTO player VALUES ('joerg', '$2a$12$6.McsTs654WOtJTB8ItKK.ARPo05Wv2ErCKiXKbXudvjE/EGJrZTy', '03FC9D', 'ROLE_PLAYER');")
        cursor.execute("INSERT INTO player VALUES ('hyacinth', '$2a$12$6.McsTs654WOtJTB8ItKK.ARPo05Wv2ErCKiXKbXudvjE/EGJrZTy', '0367FC', 'ROLE_PLAYER');")
        cursor.execute("INSERT INTO player VALUES ('ryan', '$2a$12$6.McsTs654WOtJTB8ItKK.ARPo05Wv2ErCKiXKbXudvjE/EGJrZTy', 'FC0356', 'ROLE_PLAYER');")
        cursor.execute("INSERT INTO player VALUES ('xox', '$2a$12$i9TOyr9T04CKaoff7Tt9vuoIeH0zmuKj7KQ1O22Uk.h47WruSoTf.', 'FC0356', 'ROLE_ADMIN');")


    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("CLOSED")
        con.close()


if __name__ == '__main__':
    initialize_db()

