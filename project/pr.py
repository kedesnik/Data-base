import sys
from PyQt5.QtWidgets import *
import mysql.connector
from datetime import datetime


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1812",  
        database="hotel_db"
    )


class ManageWindow(QDialog):
    def __init__(self, table_name):
        super().__init__()
        self.table_name = table_name
        self.setWindowTitle(f"Управление {table_name}")
        self.resize(600, 400)

        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)
        self.btn_add = QPushButton("Добавить")
        self.btn_edit = QPushButton("Редактировать")
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_edit)

        self.btn_add.clicked.connect(self.add_entry)
        self.btn_edit.clicked.connect(self.edit_entry)

        self.load_table()

    def load_table(self):
        db = get_connection()
        cur = db.cursor()
        if self.table_name == "rooms":
            cur.execute("SELECT room_id, room_number, room_type, price, status FROM rooms")
            headers = ["ID", "Номер", "Тип", "Цена", "Статус"]
        elif self.table_name == "clients":
            cur.execute("SELECT client_id, first_name, last_name, phone, email FROM clients")
            headers = ["ID", "Имя", "Фамилия", "Телефон", "Email"]
        elif self.table_name == "staff":
            cur.execute("SELECT staff_id, first_name, last_name, position, hire_date FROM staff")
            headers = ["ID", "Имя", "Фамилия", "Должность", "Дата найма"]

        rows = cur.fetchall()
        db.close()

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    def add_entry(self):
        db = get_connection()
        cur = db.cursor()
        try:
            if self.table_name == "rooms":
                number, ok = QInputDialog.getInt(self, "Добавить номер", "Номер комнаты:")
                if not ok: return
                rtype, ok = QInputDialog.getText(self, "Добавить номер", "Тип комнаты:")
                if not ok: return
                price, ok = QInputDialog.getDouble(self, "Добавить номер", "Цена:", min=0)
                if not ok: return
                cur.execute("INSERT INTO rooms (room_number, room_type, price) VALUES (%s,%s,%s)", 
                            (number, rtype, price))

            elif self.table_name == "clients":
                fname, ok = QInputDialog.getText(self, "Добавить клиента", "Имя:")
                if not ok: return
                lname, ok = QInputDialog.getText(self, "Добавить клиента", "Фамилия:")
                if not ok: return
                phone, ok = QInputDialog.getText(self, "Добавить клиента", "Телефон:")
                if not ok: return
                email, ok = QInputDialog.getText(self, "Добавить клиента", "Email:")
                if not ok: return
                cur.execute("INSERT INTO clients (first_name, last_name, phone, email) VALUES (%s,%s,%s,%s)",
                            (fname, lname, phone, email))

            elif self.table_name == "staff":
                fname, ok = QInputDialog.getText(self, "Добавить сотрудника", "Имя:")
                if not ok: return
                lname, ok = QInputDialog.getText(self, "Добавить сотрудника", "Фамилия:")
                if not ok: return
                pos, ok = QInputDialog.getText(self, "Добавить сотрудника", "Должность:")
                if not ok: return
                hire, ok = QInputDialog.getText(self, "Добавить сотрудника", "Дата найма (YYYY-MM-DD):")
                if not ok: return
                cur.execute("INSERT INTO staff (first_name, last_name, position, hire_date) VALUES (%s,%s,%s,%s)",
                            (fname, lname, pos, hire))

            db.commit()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Ошибка", str(e))
        finally:
            db.close()
            self.load_table()

    def edit_entry(self):
        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для редактирования")
            return

        db = get_connection()
        cur = db.cursor()
        try:
            record_id = int(self.table.item(row, 0).text())

            if self.table_name == "rooms":
                number = int(self.table.item(row, 1).text())
                rtype = self.table.item(row, 2).text()
                price = float(self.table.item(row, 3).text())
                status = self.table.item(row, 4).text()
                new_number, ok = QInputDialog.getInt(self, "Редактировать номер", "Номер:", value=number)
                if not ok: return
                new_type, ok = QInputDialog.getText(self, "Редактировать номер", "Тип:", text=rtype)
                if not ok: return
                new_price, ok = QInputDialog.getDouble(self, "Редактировать номер", "Цена:", value=price)
                if not ok: return
                new_status, ok = QInputDialog.getText(self, "Редактировать номер", "Статус:", text=status)
                if not ok: return
                cur.execute("UPDATE rooms SET room_number=%s, room_type=%s, price=%s, status=%s WHERE room_id=%s",
                            (new_number, new_type, new_price, new_status, record_id))

            elif self.table_name == "clients":
                fname = self.table.item(row, 1).text()
                lname = self.table.item(row, 2).text()
                phone = self.table.item(row, 3).text()
                email = self.table.item(row, 4).text()
                new_fname, ok = QInputDialog.getText(self, "Редактировать клиента", "Имя:", text=fname)
                if not ok: return
                new_lname, ok = QInputDialog.getText(self, "Редактировать клиента", "Фамилия:", text=lname)
                if not ok: return
                new_phone, ok = QInputDialog.getText(self, "Редактировать клиента", "Телефон:", text=phone)
                if not ok: return
                new_email, ok = QInputDialog.getText(self, "Редактировать клиента", "Email:", text=email)
                if not ok: return
                cur.execute("UPDATE clients SET first_name=%s, last_name=%s, phone=%s, email=%s WHERE client_id=%s",
                            (new_fname, new_lname, new_phone, new_email, record_id))

            elif self.table_name == "staff":
                fname = self.table.item(row, 1).text()
                lname = self.table.item(row, 2).text()
                pos = self.table.item(row, 3).text()
                hire = self.table.item(row, 4).text()
                new_fname, ok = QInputDialog.getText(self, "Редактировать сотрудника", "Имя:", text=fname)
                if not ok: return
                new_lname, ok = QInputDialog.getText(self, "Редактировать сотрудника", "Фамилия:", text=lname)
                if not ok: return
                new_pos, ok = QInputDialog.getText(self, "Редактировать сотрудника", "Должность:", text=pos)
                if not ok: return
                new_hire, ok = QInputDialog.getText(self, "Редактировать сотрудника", "Дата найма:", text=hire)
                if not ok: return
                cur.execute("UPDATE staff SET first_name=%s, last_name=%s, position=%s, hire_date=%s WHERE staff_id=%s",
                            (new_fname, new_lname, new_pos, new_hire, record_id))

            db.commit()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Ошибка редактирования", str(e))
        finally:
            db.close()
            self.load_table()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hotel Management")
        self.resize(900, 500)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        btn_layout = QHBoxLayout()
        layout.addLayout(btn_layout)
        self.btn_rooms = QPushButton("Номера")
        self.btn_clients = QPushButton("Клиенты")
        self.btn_staff = QPushButton("Сотрудники")
        self.btn_manage_rooms = QPushButton("Управление номерами")
        self.btn_manage_clients = QPushButton("Управление клиентами")
        self.btn_manage_staff = QPushButton("Управление сотрудниками")

        for b in [self.btn_rooms, self.btn_clients, self.btn_staff,
                  self.btn_manage_rooms, self.btn_manage_clients, self.btn_manage_staff]:
            btn_layout.addWidget(b)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.btn_rooms.clicked.connect(lambda: self.load_table("rooms"))
        self.btn_clients.clicked.connect(lambda: self.load_table("clients"))
        self.btn_staff.clicked.connect(lambda: self.load_table("staff"))
        self.btn_manage_rooms.clicked.connect(lambda: self.open_manage("rooms"))
        self.btn_manage_clients.clicked.connect(lambda: self.open_manage("clients"))
        self.btn_manage_staff.clicked.connect(lambda: self.open_manage("staff"))

        self.load_table("rooms")

    def load_table(self, table_name):
        db = get_connection()
        cur = db.cursor()
        query_map = {
            "rooms": "SELECT room_id, room_number, room_type, price, status FROM rooms",
            "clients": "SELECT client_id, first_name, last_name, phone, email FROM clients",
            "staff": "SELECT staff_id, first_name, last_name, position, hire_date FROM staff"
        }
        cur.execute(query_map[table_name])
        rows = cur.fetchall()
        db.close()

        headers_map = {
            "rooms": ["ID", "Номер", "Тип", "Цена", "Статус"],
            "clients": ["ID", "Имя", "Фамилия", "Телефон", "Email"],
            "staff": ["ID", "Имя", "Фамилия", "Должность", "Дата найма"]
        }

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(headers_map[table_name]))
        self.table.setHorizontalHeaderLabels(headers_map[table_name])

        for r, row in enumerate(rows):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(val)))

    def open_manage(self, table_name):
        dlg = ManageWindow(table_name)
        dlg.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
