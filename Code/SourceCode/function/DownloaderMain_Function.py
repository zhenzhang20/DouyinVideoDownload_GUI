
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
from SourceCode.user_interface.Gui_DownloaderMain import Gui_DownloaderMain
from SourceCode.function.URLSetting_Function import URLSetting_Function
from SourceCode.function.UserSetting_Function import UserSetting_Function
from SourceCode.function.SystemSetting_Function import SystemSetting_Function
from Resource.config_dir.config import Config
from Resource.config_dir.videoconfig import VideoConfig
from SourceCode.downloader.douyin_video import CrawlerScheduler_Douyin
from SourceCode.downloader.douyin_video import Time_Consume
import os, platform, time, threading, sys


class DownloaderMain_Function(Gui_DownloaderMain):
    REFRESH_TIME_INTERVAL  = 5
    def __init__(self):
        super(DownloaderMain_Function, self).__init__()
        # init UI
        self.setupUi()

        if Config().get_debugflag():
            print("debug on: in DownloaderMain_Function, before load config ")
            print("configfilepath: " + Config().configfilepath)
            print("configfilepath_init: " + Config().configfilepath_init)

        self.config = Config()
        self.videoconfig = VideoConfig()
        self.videoconfigs = []
        if self.config.get_debugflag():
            print("debug on: in DownloaderMain_Function, after load config ")

        self.myTimer = QTimer(self)
        self.myTimer.timeout.connect(self.function_show_downloadvideo_info)
        self.myStartTimer()
        # self.function_show_downloadvideo_info()

        # About Action
        self.actionAbout.triggered.connect(self.function_about_information)
        # URL Action		
        self.actionURL.triggered.connect(self.function_url_setting)
        self.URLSettingBtn.clicked.connect(self.function_url_setting)
        # User Config Action
        self.actionUser_Config.triggered.connect(self.function_userconfig)
        # System Config Action
        self.actionSystem_Config.triggered.connect(self.function_systemconfig)
        # Open Download Path
        self.DownloadResultBtn.clicked.connect(self.function_open_download_path)
        # Start Action
        self.startdownload_btn.clicked.connect(self.function_start_download)
        # Stop Action
        # self.stopdownload_btn.clicked.connect(self.function_stop_download)
        # Pause Action
        # self.pausedownload_btn.clicked.connect(self.function_pause_download)


        # refreshThread = threading.Thread(target=self.monitor_download_info)
        # refreshThread.start()



    # Actions detail
    # Pop up a window to confirm whether you want to quit or not.
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', '确定要退出吗', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
            # 为了解决终止进程时，主窗口关闭，子线程不结束而加入下面关闭语句
            sys.exit(self.exec_())
        else:
            event.ignore()



    # About
    def function_about_information(self):

        #tagtime = file_modify_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
        tagtime = "2020-02-09"
        message = '''
        版本 Ver 2020.0.1 alpha  BuildTime : '''  + tagtime + '''

        声明：
            此版本为第一版，未对程序进行优化。现有如下问题：
        1. 启动过程比较慢
        2. 开始爬取后，获取加密签名过程较慢
        请耐心~~~



        该程序为视频爱好者服务，提供下载指定抖音账号的全部视频
        目前由两人进行维护，如果您希望参与或有需求，请联系：
            微信： 15600203112
            邮件： zhen_zhang20@163.com

        '''
        QMessageBox.about(self, 'About', message)

    # URL Setting
    def function_url_setting(self):
        urlsetting_Dialog = URLSetting_Function()
        urlsetting_Dialog.show()
        urlsetting_Dialog.exec_()


    # User Config Settinguser
    def function_userconfig(self):
        userconfig_Dialog = UserSetting_Function()
        userconfig_Dialog.show()
        userconfig_Dialog.exec_()

    # System Config Setting
    def function_systemconfig(self):
        systemconfig_Dialog = SystemSetting_Function()
        systemconfig_Dialog.show()
        systemconfig_Dialog.exec_()

    # Open Download Path
    # Linux/Mac 没有测试过； Windows会闪一个批处理窗口
    #   platform.system()
	#       Linux: Linux
    #       Mac: Darwin
    #       Windows: Windows
    def function_open_download_path(self):
        download_path = Config().get_download_dir()
        if(download_path == ""):
            curdir = os.getcwd()
            download_path = os.path.join(curdir, "download")
        if not os.path.exists(download_path) or not os.path.isdir(download_path):
            os.mkdir(download_path)
        platform_info = platform.system()
        if platform_info == 'Linux':
            os.system('xdg-open "%s"' % download_path)
        elif platform_info == 'Windows':
            os.startfile(download_path)
        elif platform_info == 'Darwin':
            os.system('open "%s"' % download_path)
        else:
            QMessageBox.about(self, '打开失败', '无法打开，请手动打开下载目录')
        # os.system('start explorer.exe %s' % (download_path))
        # os.popen('explorer.exe %s' % (download_path))


    def function_start_download(self):
        # myStartTimer and new thread 是为了刷新界面
        self.myStartTimer()
        download_thread = threading.Thread(target=self.download)
        download_thread.start()

    def download(self):
        self.startdownload_btn.setText("下载中...")
        self.startdownload_btn.setEnabled(False)
        urf_file_path = self.config.get_url_file_path()
        all_url_info = self.config.load_url_info(urf_file_path)
        cs = CrawlerScheduler_Douyin(all_url_info, self.config, self.videoconfig)
        while True:
            if cs.download_status == CrawlerScheduler_Douyin.STATUS_FINISH:
                # 弹出窗口会导致主线程死掉，需改进
                # QMessageBox.about(self, '下载完成', '下载完成，请查看数据')
                self.startdownload_btn.setText("开始")
                self.startdownload_btn.setEnabled(True)
                break
            elif cs.download_status == CrawlerScheduler_Douyin.STATUS_INVALIDURL:
                # QMessageBox.about(self, '警告', '没有可以用于下载的连接，请检查URL是否可以正常打开')
                self.startdownload_btn.setText("开始")
                self.startdownload_btn.setEnabled(True)
                break


    def myStartTimer(self):
        # 设置刷新界面倒计时时间，秒为单位
        self.myTimer.start(self.REFRESH_TIME_INTERVAL)

    def myStopTimer(self):
        self.myTimer.stop()


    def function_stop_download(self):
        print("need implement... in DownloaderMain_Function ...")


    def function_pause_download(self):
        print("need implement... in DownloaderMain_Function ...")

    def function_show_downloadvideo_info(self):
        self.myStopTimer()
        # 显示下载的视频信息
        if not self.videoconfig.is_empty_config():
            self.videoconfigs = self.videoconfig.load_vconfig()
        # 取消clear/setRowCount 来解决刷新问题
        # self.download_info_table_show.clear()
        # self.download_info_table_show.setRowCount(0)
        self.download_info_table_show.setHorizontalHeaderLabels(['序号', '主播ID', '标题', '状态', '类型', '下载时间', '大小'])
        self.video_numbers = self.videoconfig.get_video_numbers()
        for videoconfig in self.videoconfigs:
            self.function_add_one_line_at_table(videoconfig, self.video_numbers)
        self.download_info_table_show.scrollToBottom()
        self.myStartTimer()
    # Add a new line at table
    # param video_pos: current line, start with the number of line: 0
    # param blogger_column_items.: the first column: parameter
    # param vtitle_column_items: the second column: parameter
    # ....
    def function_add_one_line_at_table(self, config, rownumbers):
        # num_column_items = QTableWidgetItem(str(row + 1))
        # num_column_items.setFlags(Qt.ItemIsEnabled)
        # url_column_items = QTableWidgetItem(config.)
        # url_column_items.setFlags(Qt.ItemIsEnabled)
        # '序号'      : number
        # '主播'      : blogger
        # '主播ID'    : bloggerid
        # '标题'      : vtitle
        # '状态'      : status
        # '类型'      : filetype
        # '下载时间'   : downtime
        # '大小'      : vsize
        # '文件标识'    ： identifykey
        # blogger_column_items = QTableWidgetItem(config.get('blogger'))
        # blogger_column_items.setFlags(Qt.ItemIsEditable)
        number_column_items = QTableWidgetItem(config.get('number'))
        number_column_items.setFlags(Qt.ItemIsEditable)
        bloggerid_column_items = QTableWidgetItem(config.get('bloggerid'))
        bloggerid_column_items.setFlags(Qt.ItemIsEditable)
        vtitle_column_items = QTableWidgetItem(config.get('vtitle'))
        vtitle_column_items.setFlags(Qt.ItemIsEditable)
        status_column_items = QTableWidgetItem(config.get('status'))
        status_column_items.setFlags(Qt.ItemIsEditable)
        filetype_column_items = QTableWidgetItem(config.get('filetype'))
        filetype_column_items.setFlags(Qt.ItemIsEditable)
        downtime_column_items = QTableWidgetItem(config.get('downtime'))
        downtime_column_items.setFlags(Qt.ItemIsEditable)
        vsize_column_items = QTableWidgetItem(config.get('vsize'))
        vsize_column_items.setFlags(Qt.ItemIsEditable)

        self.download_info_table_show.setRowCount(rownumbers)
        self.download_info_table_show.verticalHeader().setVisible(False)

        video_pos = self.videoconfig.get_vconfig_pos_by_id(config.get('number'))
        if video_pos is None :
            return
        # number_column_items = QTableWidgetItem(video_pos)
        self.download_info_table_show.setItem(video_pos, 0, QTableWidgetItem(number_column_items))
        self.download_info_table_show.setItem(video_pos, 1, QTableWidgetItem(bloggerid_column_items))
        self.download_info_table_show.setItem(video_pos, 2, QTableWidgetItem(vtitle_column_items))
        self.download_info_table_show.setItem(video_pos, 3, QTableWidgetItem(status_column_items))
        self.download_info_table_show.setItem(video_pos, 4, QTableWidgetItem(filetype_column_items))
        self.download_info_table_show.setItem(video_pos, 5, QTableWidgetItem(downtime_column_items))
        self.download_info_table_show.setItem(video_pos, 6, QTableWidgetItem(vsize_column_items))

    # def monitor_download_info(self):
    #     while (True):
    #         self.function_show_downloadvideo_info()
    #         time.sleep(self.REFRESH_TIME_INTERVAL)
