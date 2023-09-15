
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
import mysql.connector

class FirstWindow(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.title = "ATC Technology"
        self.theme_cls.theme_style = "Light"

class LoginWindow(Screen):
    def build(self):
        #self.title = "ATC Technology"
        #self.theme_cls.theme_style = "Light"
    
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "MySQLgo%321x!",
            database = "project_db",
            auth_plugin='mysql_native_password',
        )

        c = my_db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS project_db")

        my_db.commit()
        my_db.close()

    def check_info(self):
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "MySQLgo%321x!",
            database = "project_db",
            auth_plugin='mysql_native_password',
        )

        c = my_db.cursor()

        U_name = self.ids.Name.text
        U_passwd = self.ids.passWord.text

        c.execute("SELECT * FROM Users WHERE name = %s AND password = %s", (U_name, U_passwd))

        all_data = c.fetchall()

        #if all_data:
            #print("Find user")
        #else:
            #print("Not found user")

class RegisterWindow(Screen):
    def check_data(self):
        my_db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "MySQLgo%321x!",
            database = "project_db",
            auth_plugin='mysql_native_password',
        )

        c = my_db.cursor()

        name = self.ids.F_Name.text

        c.execute("SELECT * FROM Users WHERE name = %s", (name,))

        result = c.fetchone()

        if result:
            #print("User already exists")
            pass
        else:
            value_name = (self.ids.F_Name.text)
            value_pass = (self.ids.F_passWord.text)

            c.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (value_name, value_pass))
            my_db.commit()
            #print("User has been added!")
        c.close()
        


if __name__ == "__main__":
    MainApp().run()