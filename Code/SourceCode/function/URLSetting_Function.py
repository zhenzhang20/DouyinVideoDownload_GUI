

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QTableWidgetItem, QCheckBox, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt
from SourceCode.user_interface.Gui_URLSetting import Gui_URLSetting
from Resource.config_dir.config import Config


class URLSetting_Function(Gui_URLSetting):
    def __init__(self):
        super(URLSetting_Function, self).__init__()
        self.setupUi()
        # show URL
        self.config = Config()
        self.url_file_path = self.config.get_url_file_path()

        if self.url_file_path != '':
            self.function_load_url_info(self.url_file_path)
        # Browser URL Action
        self.urlbrowserbutton.clicked.connect(self.function_import_url_setting)
        # OK/Cancel button action
        self.buttonBox.accepted.connect(self.function_accept)
        self.buttonBox.rejected.connect(self.function_reject)

    def function_accept(self):
        config = self.config
        config.set_url_file_path(self.url_path.text())
        self.accept()

    def function_reject(self):
        self.reject()

    # Import URL file
    def function_import_url_setting(self):
        self.url_file_path = self.choose_one_file()
        if self.url_file_path == '':
            return
        self.function_load_url_info(self.url_file_path)

    def choose_one_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(self, 'Choose URL File', './',
                                                           "All Files (*);;")
        return file_path


    def function_load_url_info(self, urf_file_path):
        self.url_path.setText(urf_file_path)
        self.url_path.setEnabled(False)
        try:
            self.all_url_info = self.config.load_url_info(urf_file_path)
            self.function_show_url_value()
        except Exception:
            QMessageBox.warning(self, 'Warning', 'Analysis URL failed!', QMessageBox.Close)
            return



    # update table's info - url
    def function_show_url_value(self):
        # self.model_lines.clear()
        self.url_table_show.clear()
        self.url_table_show.setRowCount(0)
        self.url_table_show.setHorizontalHeaderLabels(['No.', 'URL'])

        for url in self.all_url_info:
            self.function_add_one_line_at_table(self.url_table_show.rowCount(), url.strip())

    # Add a new line at table
    # param row:QTableWidgetItem current line, start with the number of line: 0
    # param num.: the first column: parameter
    # param url: the second column: parameter
    def function_add_one_line_at_table(self, row, url):
        num_column_items = QTableWidgetItem(str(row + 1))
        num_column_items.setFlags(Qt.ItemIsEnabled)
        url_column_items = QTableWidgetItem(url)
        url_column_items.setFlags(Qt.ItemIsEnabled)

        self.url_table_show.setRowCount(row + 1)
        self.url_table_show.verticalHeader().setVisible(False)

        self.url_table_show.setItem(row, 0, QTableWidgetItem(num_column_items))
        self.url_table_show.setItem(row, 1, QTableWidgetItem(url_column_items))


