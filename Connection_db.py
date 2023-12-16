from PySide6 import QtWidgets, QtSql
import sqlite3

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
        self.connection = sqlite3.connect("Курсовая_DB.db")
        self.cursor = self.connection.cursor()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName("Курсовая_DB.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Ошибка подключения!", "Закрыть", QtWidgets.QMessageBox.Cancel)
            return False
        query = QtSql.QSqlQuery()
        return True

    def execute_query_with_params(self, str_query, query_value=None):
        query = QtSql.QSqlQuery()
        query.prepare(str_query)

        if query_value is not None:
            for value in query_value:
                query.addBindValue(value)

        query.exec()
        return query

    def select_table(self, name_Table, str_search=None):
        sql_query = f"select * from {name_Table}"

        if str_search is not None:
            sql_query += f" where {str_search}"

        self.cursor.execute(sql_query)
        query_answer = self.cursor.fetchone()

        return query_answer

    def add_new_row(self, name_Table, name_title, values):
        str_query = f"insert into {name_Table} ({name_title}) values ({values})"
        self.cursor.execute(str_query)
        self.connection.commit()

    def update_row(self, name_Table, name_title, values, str_search):
        str_query = f"update {name_Table} set {name_title.split(', ')[0]}={values[0]} where {str_search}"
        self.cursor.execute(str_query)
        self.connection.commit()
        for i in range(1, len(name_title.split(", "))):
            str_query = f"update {name_Table} set {name_title.split(', ')[i]}={values[i]} where {str(str_search).split('=')[0]}={values[0]}"
            self.cursor.execute(str_query)
        self.connection.commit()

    def delete_row(self, name_Table, str_where):
        str_query = f"delete from {name_Table} where {str_where}"
        self.cursor.execute(str_query)
        self.connection.commit()

    def theme_onn(self):
        self.cursor.execute('''select key_word from Style where onn="True"''')
        kkey = self.cursor.fetchone()[0]
        self.cursor.execute('''select key_word from Style where onn="False"''')
        key = self.cursor.fetchone()
        return kkey, key

    def get_style(self, word_key_onn, off):
        self.cursor.execute(f'''update Style set onn="True" where key_word="{word_key_onn}"''')
        self.cursor.execute(f'''update Style set onn="False" where key_word="{off}"''')
        self.connection.commit()

        self.cursor.execute('''select styleSheet, contentTopBg, leftMenuBg,
    bottomBar, bgApp, stackedWidget, btn_start_aktive, btn_pilot, btn_people, btn_reis,
    btn_reis_stop, btn_qwery, theme_mod, add_row, update_row, delete_row from Style where onn="True"''')
        list_values = self.cursor.fetchone()
        return list_values