import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtCore import QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

base_dir = Path(__file__).parent.parent.parent.resolve()
print(f"Base DIR: {base_dir}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect_db()

        self.model = QSqlTableModel(self)
        self.model.setTable("Track")
        self.model.select()

        self.table = QTableView()
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        self.setMinimumSize(QSize(600, 400))
        self.setWindowTitle("Database")

    def connect_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")

        print("Database PATH")
        db_path = Path(base_dir / "lessons" / "databases" / "chinook.sqlite")
        db.setDatabaseName(str(db_path))
        print(db_path)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
