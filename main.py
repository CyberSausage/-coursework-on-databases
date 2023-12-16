import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel

from main_ui import Ui_MainWindow
from main_light_ui import Ui_MainWindow_Light
from main_dark_ui import Ui_MainWindow_Dark

from edit_tiket_ui import Ui_Edit_tiket
from edit_team_ui import Ui_Edit_team
from edit_people_ui import Ui_edit_people
from edit_reis_ui import Ui_edit_reis
from edit_reis_stop_ui import Ui_Edit_reis_stop

from Connection_db import Data


class MaIn(QMainWindow):
    def __init__(self):
        super(MaIn, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = Data()

        self.setWindowTitle("Airport information system")
        self.draw_clicked(index=0, first_index=True)
        self.get_new_theme(flag=True)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.btn_start_aktive.clicked.connect(self.stackeWidget_tiket)
        self.ui.btn_pilot.clicked.connect(self.stackeWidget_pilot)
        self.ui.btn_people.clicked.connect(self.stackeWidget_people)
        self.ui.btn_reis.clicked.connect(self.stackeWidget_reis)
        self.ui.btn_reis_stop.clicked.connect(self.stackeWidget_reis_stop)

        self.ui.search_tiket_btn.clicked.connect(self.select_table_click)
        self.ui.search_pilot_btn.clicked.connect(self.select_table_click)
        self.ui.search_people_btn.clicked.connect(self.select_table_click)
        self.ui.search_reis_btn.clicked.connect(self.reis_call_view_data)
        self.ui.search_reis_block_btn.clicked.connect(self.select_table_click)

        self.list_Box = [self.ui.tiket_comboBox, self.ui.pilot_comboBox, self.ui.people_comboBox, self.ui.reis_comboBox, self.ui.reis_block_comboBox]
        self.list_Line = [self.ui.tiket_edit, self.ui.pilot_edit, self.ui.people_edit, self.ui.reis_edit, self.ui.reis_block_edit]

        self.model = QSqlTableModel(self)
        self.view_data('Билеты', self.ui.table_tikets)

        self.ui.theme_mod.clicked.connect(self.get_new_theme)

        self.ui.clean_filtr.clicked.connect(self.clear_comboBox_lineEdit)
        self.ui.add_row.clicked.connect(self.edit_row_table)
        self.ui.update_row.clicked.connect(self.get_for_update)
        self.ui.delete_row.clicked.connect(self.get_row_for_delete)

    def stackeWidget_tiket(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clear_comboBox_lineEdit()
        self.draw_clicked(index=0)
        self.view_data('Билеты', self.ui.table_tikets)

    def stackeWidget_pilot(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.clear_comboBox_lineEdit()
        self.draw_clicked(index=1)
        self.view_data('Экипаж', self.ui.table_pilots)
    def stackeWidget_people(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.clear_comboBox_lineEdit()
        self.draw_clicked(index=2)
        self.view_data('Пассажиры', self.ui.table_people)
    def stackeWidget_reis(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.clear_comboBox_lineEdit()
        self.draw_clicked(index=3)
        self.view_data('Рейсы', self.ui.table_reis, True)
    def stackeWidget_reis_stop(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.clear_comboBox_lineEdit()
        self.draw_clicked(index=4)
        self.view_data('Задержанные_рейсы', self.ui.table_reis_block)
    def clear_comboBox_lineEdit(self):
        for i in range(0, len(self.list_Box)):
            self.list_Box[i].setCurrentIndex(0)
            self.list_Line[i].setText("")

    def get_new_theme(self, flag=False):
        value = self.conn.theme_onn()
        if (flag):
            list_style = self.conn.get_style(value[0], value[1])
        else:
            if value[0] == "dark":
                list_style = self.conn.get_style("light", "dark")
            else:
                list_style = self.conn.get_style("dark", "light")

        self.ui.styleSheet.setStyleSheet(list_style[0])
        self.ui.contentTopBg.setStyleSheet(list_style[1])
        self.ui.leftMenuBg.setStyleSheet(list_style[2])
        self.ui.bottomBar.setStyleSheet(list_style[3])
        self.ui.bgApp.setStyleSheet(list_style[4])
        self.ui.stackedWidget.setStyleSheet(list_style[5])
        self.ui.btn_start_aktive.setStyleSheet(list_style[6])
        self.ui.btn_pilot.setStyleSheet(list_style[7])
        self.ui.btn_people.setStyleSheet(list_style[8])
        self.ui.btn_reis.setStyleSheet(list_style[9])
        self.ui.btn_reis_stop.setStyleSheet(list_style[10])
        self.ui.theme_mod.setStyleSheet(list_style[12])
        self.ui.add_row.setStyleSheet(list_style[13])
        self.ui.update_row.setStyleSheet(list_style[14])
        self.ui.delete_row.setStyleSheet(list_style[15])

    def edit_row_table(self):
        list_new_window = [Ui_Edit_tiket(), Ui_Edit_team(), Ui_edit_people(), Ui_edit_reis(), Ui_Edit_reis_stop()]
        self.new_window = QtWidgets.QDialog()
        self.ui_edit = list_new_window[self.ui.stackedWidget.currentIndex()]
        self.ui_edit.setupUi(self.new_window)
        self.new_window.show()
        list_objects = self.new_window.children()[0].children()

        for i in list_objects:
            if (i.objectName().find("send") != -1):
                button_send = i

        button_send.clicked.connect(self.send_info_add)

    def send_info_add(self):
        str_name_table, str_name_column, str_values = self.get_label_content()

        self.conn.add_new_row(str_name_table, str_name_column, str_values)
        self.new_window.deleteLater()
        self.update_table_for_widget(str_name_table)

    def get_for_update(self):
        list_new_window = [Ui_Edit_tiket(), Ui_Edit_team(), Ui_edit_people(), Ui_edit_reis(), Ui_Edit_reis_stop()]
        self.new_window = QtWidgets.QDialog()
        self.ui_edit = list_new_window[self.ui.stackedWidget.currentIndex()]
        self.ui_edit.setupUi(self.new_window)
        self.new_window.show()
        list_objects = self.new_window.children()[0].children()

        for i in list_objects:
            if (i.objectName().find("Title_Label") != -1):
                nameTable = i.text()
            if (i.objectName().find("send") != -1):
                button_send = i

        list_value = self.conn.select_table(nameTable, self.get_query_where())
        for i in list_objects:
            if (i.objectName().find("lineEdit") != -1):
                i.setText(str(list_value[int(i.objectName().split("_")[-1])]))

        button_send.clicked.connect(self.send_info_update)


    def send_info_update(self):
        str_name_table, str_name_column, str_values = self.get_label_content()
        self.conn.update_row(str_name_table, str_name_column, str_values.split(", "), self.get_query_where())
        self.new_window.deleteLater()
        self.update_table_for_widget(str_name_table)

    def get_row_for_delete(self):
        str_where = self.get_query_where()
        list_widget_child = self.ui.stackedWidget.currentWidget().children()
        for i in list_widget_child:
            if (i.objectName().find("title_lab") != -1):
                str_name_table = i.text().replace(" ", "_")
                break
        self.conn.delete_row(str_name_table, str_where)
        self.update_table_for_widget(str_name_table)

    def get_query_where(self):
        list_widget_child = self.ui.stackedWidget.currentWidget().children()
        list_widget_child[1].children()[1].setCurrentIndex(1)
        name_column = list_widget_child[1].children()[1].currentText()
        for i in list_widget_child:
            if (i.objectName().find("table_") != -1):
                index = i.selectedIndexes()[0]
                id = str(i.model().data(index))
        return f"{name_column}='{id}'"

    def get_label_content(self):
        list_objects = self.new_window.children()[0].children()
        str_name_table, str_name_column, str_values = "", "", ""
        for i in list_objects:
            if (i.objectName().find("Title_Label") != -1):
                str_name_table = i.text()
            if (i.objectName().find("_label") != -1):
                search = i.objectName().replace("_label", "")
                if (str_name_column != ""):
                    str_name_column += ", "
                str_name_column += i.text()
                for l in list_objects:
                    if (l.objectName() != i.objectName() and l.objectName().find(search) != -1):
                        if str_values != "":
                            str_values += ", "
                        str_values += f"'{l.text()}'"
        return str_name_table, str_name_column, str_values

    def draw_clicked(self, index, first_index=False):
        left_list_btn = [self.ui.btn_start_aktive, self.ui.btn_pilot, self.ui.btn_people, self.ui.btn_reis, self.ui.btn_reis_stop]
        if self.ui.theme_mod.styleSheet().find("light_") == -1:
            open_color = "#99a2a8"
            close_color = "#b5bfc6"
            str_background_open = f"background-color: {open_color};"
            str_background_close = f"background-color: {close_color};"
        else:
            open_color = "40, 44, 52"
            close_color = "33, 37, 43"
            str_background_open = f"background-color: rgb({open_color});"
            str_background_close = f"background-color: rgb({close_color});"
        for btn in left_list_btn:
            if first_index:
                if btn != left_list_btn[index]:
                    btn.setStyleSheet(str_background_close + btn.styleSheet())
                else:
                    btn.setStyleSheet(str_background_open + btn.styleSheet())
            else:
                if btn != left_list_btn[index]:
                    btn.setStyleSheet(btn.styleSheet().replace(open_color, close_color))
        left_list_btn[index].setStyleSheet(left_list_btn[index].styleSheet().replace(close_color, open_color))

    def update_table_for_widget(self, str_name_table):
        for i in self.ui.stackedWidget.currentWidget().children():
            if (i.objectName().find("table_") != -1):
                self.view_data(str_name_table, i)
                break

    def view_data(self, nameTable, name_table_view, flag=False, where=None):
        self.model.setTable(nameTable)
        self.model.select()
        if where is not None:
            self.model.setFilter(f"{str(where).split('-')[0]}='{str(where).split('-')[1]}'")
        name_table_view.setModel(self.model)
        count = self.model.columnCount()
        if flag:
            name_table_view.resizeColumnsToContents()
        else:
            for colum in range(0, count):
                name_table_view.setColumnWidth(colum, 990/count-5)
    def reis_call_view_data(self):
        self.select_table_click(flag=True)
    def select_table_click(self, flag=False):
        sender = self.sender().parent()
        tableView = sender.parent().children()[0]
        comboBox_text = sender.children()[1].currentText()
        line_edit_text = sender.children()[2].text()
        if (comboBox_text == "" or line_edit_text == ""):
            self.view_data(nameTable=sender.parent().children()[2].text().replace(" ", "_"), name_table_view=tableView, flag=flag, where=None)
        else:
            self.view_data(nameTable=sender.parent().children()[2].text().replace(" ", "_"), name_table_view=tableView, flag=flag, where=f"{comboBox_text}-{line_edit_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MaIn()
    window.show()

    sys.exit(app.exec())