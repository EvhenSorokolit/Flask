import math
import sqlite3
import time


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
    def addPost(self,title,text):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO posts VALUES(NULL,?,?,?)",(title,text,tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print(" Ошибка добавления статьи  в БД"+ str(e))
            return False
        return True

    def getMenu(self):
        sql = '''SELECT * FROM mainmenu'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()

            if res: return res
        except:
            print(" Ошибка чтения BD")
        return []


    def getPost(self,postID):
        sql = f'''SELECT title, text FROM posts WHERE id = {postID} LIMIT 1'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()

            if res:
                return res
        except sqlite3.Error as e:
            print(" Ошибка чтения BD"+ str(e))
        return (False,False)
    def getPostsAnonce(self):
        sql = f'''SELECT id,title, text FROM posts ORDER BY time  DESC'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()

            if res:
                return res
        except sqlite3.Error as e:
            print(" Ошибка чтения BD" + str(e))
        return []
