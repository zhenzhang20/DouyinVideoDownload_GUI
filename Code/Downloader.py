import sys

from PyQt5.QtWidgets import QApplication
from SourceCode.function.DownloaderMain_Function import DownloaderMain_Function
import PyQt5.sip


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DownloaderMain_Function()
    main_window.show()
    sys.exit(app.exec_())


