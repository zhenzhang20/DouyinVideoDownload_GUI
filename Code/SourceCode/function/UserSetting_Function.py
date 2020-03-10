
import os
import pathlib
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from SourceCode.user_interface.Gui_UserSetting import Gui_UserSetting
from Resource.config_dir.config import Config

class UserSetting_Function(Gui_UserSetting):


    def __init__(self):
        super(UserSetting_Function, self).__init__()
        self.setupUi()
        # get config
        self.config = Config()

        # Browser Download Dir Action
        self.downloadpathbrowserbutton.clicked.connect(self.function_import_download_dir)

        # show Download Dir
        self.download_dir = self.config.get_download_dir()
        self.function_load_download_dir_info(self.download_dir)

        # Browser Trailer Picture Dir Action
        self.trailerpicturebrowserbutton.clicked.connect(self.function_import_trailerpicture_dir)
        # show Trailer Picture Dir
        self.trailerpicture_dir = self.config.get_trailerpicture_dir()
        self.function_load_trailerpicture_dir_info(self.trailerpicture_dir)
        # show Trailer Video Dir
        self.trailervideo_dir = self.config.get_trailervideo_dir()
        self.function_load_trailervideo_dir_info(self.trailervideo_dir)
        # Browser Trailer Video Dir Action
        self.trailervideobrowserbutton.clicked.connect(self.function_import_trailervideo_dir)
        # show md5 change method
        self.md5_opts = self.config.get_MD5options_list()
        self.md5_optionid = self.config.get_MD5optionid()
        self.function_load_md5_opts_info(self.md5_opts, self.md5_optionid)
        self.md5_combobox.currentTextChanged.connect(self.function_refresh_md5_opts)

        # show namingrule change method
        self.namingrule_opts = self.config.get_namingruleoptions_list()
        self.namingrule_optionid = self.config.get_namingruleoptionid()
        self.function_load_namingrule_opts_info(self.namingrule_opts, self.namingrule_optionid)
        self.namingrule_combobox.currentTextChanged.connect(self.function_refresh_namingrule_opts)


        # OK/Cancel button action
        self.buttonBox.accepted.connect(self.function_accept)
        self.buttonBox.rejected.connect(self.function_reject)

    def function_accept(self):

        config = self.config

        # 设置 download dir 信息
        config.set_download_dir(self.downloadpath_lineedit.text())

        # 设置 md5 选项信息
        config.set_MD5optionid(self.config.get_MD5optionid())
        # 设置 trailer picture dir 信息
        config.set_trailerpicture_dir(self.trailerpicture_lineedit.text())
        # 设置 trailer picture dir 信息
        config.set_trailervideo_dir(self.trailervideo_lineedit.text())

        self.accept()

    def function_reject(self):
        self.reject()

    # Import download dir
    def function_import_download_dir(self):
        self.download_dir = self.choose_one_folder()
        if self.download_dir == '':
            return
        self.function_load_download_dir_info(self.download_dir)

    def choose_one_folder(self):
        download_dir = QFileDialog.getExistingDirectory(self, 'Choose Download Director', self.download_dir)
        return download_dir

    def function_load_download_dir_info(self, download_dir):
        self.downloadpath_lineedit.setText(download_dir)
        self.downloadpath_lineedit.setEnabled(False)

    # Import trailer picture dir
    def function_import_trailerpicture_dir(self):
        self.trailerpicture_dir = self.choose_one_picture()
        if self.trailerpicture_dir == '':
            return
        self.function_load_trailerpicture_dir_info(self.trailerpicture_dir)


    def choose_one_picture(self):
        cur_trailerpicture_path = self.trailerpicture_lineedit.text()
        cur_trailerpicture_par_path = os.path.dirname(os.path.realpath(cur_trailerpicture_path))

        if os.path.exists(cur_trailerpicture_par_path):
            show_dir = cur_trailerpicture_par_path
        else:
            show_dir = self.config.get_resource_dir()

        trailerpicture_dir = QFileDialog.getOpenFileName(self, 'Choose Trailer Picture File', show_dir, "Image file (*.jpg;*.png)")[0]
        return trailerpicture_dir

    def function_load_trailerpicture_dir_info(self, trailerpicture_dir):
        self.trailerpicture_lineedit.setText(trailerpicture_dir)
        self.trailerpicture_lineedit.setEnabled(False)

    # Import trailer video dir
    def function_import_trailervideo_dir(self):
        self.trailervideo_dir = self.choose_one_video()
        if self.trailervideo_dir == '':
            return
        self.function_load_trailervideo_dir_info(self.trailervideo_dir)

    def choose_one_video(self):
        cur_trailervideo_path = self.trailervideo_lineedit.text()
        cur_trailervideo_par_path = os.path.dirname(os.path.realpath(cur_trailervideo_path))

        if os.path.exists(cur_trailervideo_par_path):
            show_dir = cur_trailervideo_par_path
        else:
            show_dir = self.config.get_resource_dir()

        trailervideo_dir = QFileDialog.getOpenFileName(self, 'Choose Trailer Video File', show_dir, "Video file (*.mp4)")[0]
        return trailervideo_dir

    def function_load_trailervideo_dir_info(self, trailervideo_dir):
        self.trailervideo_lineedit.setText(trailervideo_dir)
        self.trailervideo_lineedit.setEnabled(False)


    def function_load_md5_opts_info(self, md5_opts, md5_optionid):
        for i in range(len(md5_opts)):
            self.md5_combobox.addItem((str(md5_opts[i]).split(":"))[1].replace("'", ""))
        self.md5_combobox.setCurrentIndex(int(md5_optionid))

        self.function_show_picture_video_area()

    def function_refresh_md5_opts(self):
        self.function_set_MD5optionid()
        self.function_show_picture_video_area()

    def function_set_MD5optionid(self):
        self.config.set_MD5optionid(self.md5_combobox.currentIndex())

    # 检查optionid值，如果是0/1，则同时显示picture、video路径为空；如果是2，则同时显示picture路径、video路径为空；
    # 如果是3，则同时显示video路径、picture路径为空；
    # check optionid
    def function_show_picture_video_area(self):
        md5_optionid = self.config.get_MD5optionid()
        self.trailerpicturepath = self.config.get_trailerpicture_dir()
        self.trailervideopath = self.config.get_trailervideo_dir()
        self.trailerpicture_lineedit.setEnabled(False)
        self.trailerpicture_label.setVisible(False)
        self.trailerpicture_lineedit.setVisible(False)
        self.trailerpicturebrowserbutton.setVisible(False)
        self.trailervideo_lineedit.setEnabled(False)
        self.trailervideo_label.setVisible(False)
        self.trailervideo_lineedit.setVisible(False)
        self.trailervideobrowserbutton.setVisible(False)

        if int(md5_optionid) == 2:
            self.trailerpicture_lineedit.setText(self.trailerpicturepath)
            self.trailerpicture_label.setVisible(True)
            self.trailerpicture_lineedit.setVisible(True)
            self.trailerpicturebrowserbutton.setVisible(True)
            # self.trailervideo_lineedit.setText("")
        elif int(md5_optionid) == 3:
            # self.trailerpicture_lineedit.setText("")
            self.trailervideo_lineedit.setText(self.trailervideopath)
            self.trailervideo_label.setVisible(True)
            self.trailervideo_lineedit.setVisible(True)
            self.trailervideobrowserbutton.setVisible(True)
        # else : #int(md5_optionid) == 0 or int(md5_optionid) == 1:
        #     self.trailerpicture_lineedit.setText("")
        #     self.trailervideo_lineedit.setText("")


    def function_load_namingrule_opts_info(self, namingrule_opts, namingrule_optionid):
        for i in range(len(namingrule_opts)):
            self.namingrule_combobox.addItem((str(namingrule_opts[i]).split(":"))[1].replace("'", ""))
        self.namingrule_combobox.setCurrentIndex(int(namingrule_optionid))


    def function_refresh_namingrule_opts(self):
        self.function_set_namingruleoptionid()


    def function_set_namingruleoptionid(self):
        self.config.set_namingruleoptionid(self.namingrule_combobox.currentIndex())
