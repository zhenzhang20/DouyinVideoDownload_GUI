
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from SourceCode.user_interface.Gui_SystemSetting import Gui_SystemSetting
from Resource.config_dir.config import Config

class SystemSetting_Function(Gui_SystemSetting):
    MIN_THREAD_NUMBER = 1
    MAX_THREAD_NUMBER = 4
    MIN_FAILED_RETRY_TIMES = 1
    MAX_FAILED_RETRY_TIMES = 4
    MIN_CONNECT_TIMEOUT = 1
    MAX_CONNECT_TIMEOUT = 10


    def __init__(self):
        super(SystemSetting_Function, self).__init__()
        self.setupUi()
        self.config = Config()

        # show thread number
        self.thread_number = self.config.get_thread_number()
        self.function_load_thread_number_info(self.thread_number)
        # show retry times
        self.failed_retry_times = self.config.get_failed_retry_times()
        self.function_load_failed_retry_times_info(self.failed_retry_times)
        # show connect timeout, unit is second
        self.connect_timeout = self.config.get_connect_timeout()
        self.function_load_connect_timeout_info(self.connect_timeout)
        # show header text
        self.headertext = self.config.get_headertext()
        self.function_load_headertext_info(self.headertext)

        # OK/Cancel button action
        self.buttonBox.accepted.connect(self.function_accept)
        self.buttonBox.rejected.connect(self.function_reject)

    def function_accept(self):

        config = self.config

        # 设置 thread 信息
        # 判断 thread 数值，取值范围在[1,4]
        try :
            thread_num = int(self.threads_lineedit.text())
            if thread_num < SystemSetting_Function.MIN_THREAD_NUMBER or thread_num > SystemSetting_Function.MAX_THREAD_NUMBER:
                QMessageBox.warning(self, '线程数（并行数量） 设置失败',
                                    '数值应该大于等于' + str(SystemSetting_Function.MIN_THREAD_NUMBER) + '且小于等于' + str(
                                        SystemSetting_Function.MAX_THREAD_NUMBER))
                return
            else:
                config.set_thread_number(self.threads_lineedit.text())
        except Exception as ex:
            QMessageBox.warning(self, '线程数（并行数量） 设置失败',
                                '应该为 ' + str(SystemSetting_Function.MIN_THREAD_NUMBER) + '~' + str(SystemSetting_Function.MAX_THREAD_NUMBER) + ' 的数值')
            return

        # 设置 failed retry times 信息
        # 判断 failed retry times 数值，取值范围在[1,4]
        try :
            failedretrytimes = int(self.failedretrytimes_lineedit.text())
            if failedretrytimes < SystemSetting_Function.MIN_FAILED_RETRY_TIMES or thread_num > SystemSetting_Function.MAX_FAILED_RETRY_TIMES:
                QMessageBox.warning(self, '下载失败重复次数 设置失败',
                                    '数值应该大于等于' + str(SystemSetting_Function.MIN_FAILED_RETRY_TIMES) + '且小于等于' + str(
                                        SystemSetting_Function.MAX_FAILED_RETRY_TIMES))
                return
            else:
                config.set_failed_retry_times(self.failedretrytimes_lineedit.text())
        except Exception as ex:
            QMessageBox.warning(self, '下载失败重复次数 设置失败',
                                '应该为 ' + str(SystemSetting_Function.MIN_FAILED_RETRY_TIMES) + '~' + str(SystemSetting_Function.MAX_FAILED_RETRY_TIMES) + ' 的数值')
            return


        # 设置 connect timeout 信息
        # 判断 connect timeout 数值，取值范围在[1,10]
        try :
            connecttimeout = int(self.connecttimeout_lineedit.text())
            if connecttimeout < SystemSetting_Function.MIN_CONNECT_TIMEOUT or thread_num > SystemSetting_Function.MAX_CONNECT_TIMEOUT:
                QMessageBox.warning(self, '连接超时（秒） 设置失败',
                                    '数值应该大于等于' + str(SystemSetting_Function.MIN_CONNECT_TIMEOUT) + '且小于等于' + str(
                                        SystemSetting_Function.MAX_CONNECT_TIMEOUT))
                return
            else:
                config.set_connect_timeout(self.connecttimeout_lineedit.text())
        except Exception as ex:
            QMessageBox.warning(self, '连接超时（秒） 设置失败',
                                '应该为 ' + str(SystemSetting_Function.MIN_CONNECT_TIMEOUT) + '~' + str(SystemSetting_Function.MAX_CONNECT_TIMEOUT) + ' 的数值')
            return


        # 设置 报头 信息
        headertext = self.header_textedit.toPlainText()
        if headertext == "":
            QMessageBox.warning(self, "报头 设置失败", "报头不能为空。样例：\n"
                                                 "'accept-encoding': 'gzip, deflate, br',\n"
                                                 "'accept-language': 'zh-CN,zh;q=0.9',\n"
                                                 "'pragma': 'no-cache',\n"
                                                 "'cache-control': 'no-cache',\n"
                                                 "'upgrade-insecure-requests': '1',\n"
                                                 "'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'")
            return
        else :
            config.set_headertext(self.header_textedit.toPlainText().replace('\',\n','\',').strip())

        self.accept()


    def function_reject(self):
        self.reject()

    def function_load_thread_number_info(self, thread_number):
        self.threads_lineedit.setText(thread_number)
        # self.threads_lineedit.setEnabled(True)
        self.threads_lineedit.setEnabled(False)

    def function_load_failed_retry_times_info(self, failed_retry_time):
        self.failedretrytimes_lineedit.setText(failed_retry_time)
        self.failedretrytimes_lineedit.setEnabled(True)


    def function_load_connect_timeout_info(self, connect_timeout):
        self.connecttimeout_lineedit.setText(connect_timeout)
        self.connecttimeout_lineedit.setEnabled(True)


    def function_load_headertext_info(self, headertext):
        self.header_textedit.setText(headertext)
        self.header_textedit.setEnabled(True)

