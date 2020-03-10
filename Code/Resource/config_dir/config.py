"""
Define all path.
Note: absolute path
"""
import os
import json
from collections import OrderedDict
from SourceCode.pub_func import utils_filepath
import shutil
import pathlib
import ast

url_init_dir = os.path.join('Resource', 'config_dir')
config_init_dir = os.path.join('Resource', 'config_dir')
config_dir = os.path.join('Resource', 'config_dir')

download_dir = os.path.join(os.getcwd(), 'download')
resource_dir = os.path.join(os.getcwd(), 'Resource')
url_dir = os.path.join(os.getcwd(), 'Resource')

md5_optionid_default = "1"
# md5_optionvalue_default = "自动修改"
md5_options_default = "'0': '不修改','1': '自动修改','2': '片尾自动合并给定图片','3': '片尾自动合并给定视频'"
namingrule_optionid_default = "0"
# namingrulevalue_default = "视频标识_视频名称"
namingrule_options_default = "'0': '视频标识_视频名称','1': '视频编号_主播ID_主播名称_视频标识_视频名称'"
trailer_dir = os.path.join('Resource', 'config_trailer')
trailerpicture_default = 'def_tailerpicture.jpg'
trailervideo_default = 'def_tailervideo.mp4'
debug_flag = False


class Config(object):
    def __init__(self):
        self.configfiledir = utils_filepath.resource_path(os.path.join(resource_dir))
        self.configfilepath = utils_filepath.resource_path(os.path.join(resource_dir, 'config.json'))
        self.configfilepath_init = utils_filepath.resource_path(os.path.join(config_init_dir, 'config_init.json'))
        self.url_file_init = utils_filepath.resource_path(os.path.join(url_init_dir, 'url_init.txt'))
        self.url_file = utils_filepath.resource_path(os.path.join(url_dir, 'url.txt'))
        self.js_file = utils_filepath.resource_path(os.path.join(config_dir, 'byted_decode.js'))
        self.trailerpicture_default = utils_filepath.resource_path(os.path.join(resource_dir, trailerpicture_default))
        self.trailervideo_default = utils_filepath.resource_path(os.path.join(resource_dir, trailervideo_default))
        self.trailerpicture_default_init = utils_filepath.resource_path(os.path.join(trailer_dir, trailerpicture_default))
        self.trailervideo_default_init = utils_filepath.resource_path(os.path.join(trailer_dir, trailervideo_default))

        self.THREADS = 1
        self.HEADERS = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }
        self.RETRY = 1
        self.TIMEOUT = 1
        self.current_folder = pathlib.Path(__file__).parent
        # self.SAVEFOLDER = str(self.current_folder / 'download')

    def load_config(self):
        if not os.path.exists(self.configfilepath):
            if not os.path.exists(self.configfiledir):
                os.makedirs(self.configfiledir)
            shutil.copyfile(self.configfilepath_init, self.configfilepath)
        if not os.path.exists(self.trailerpicture_default):
            if not os.path.exists(self.configfiledir):
                os.makedirs(self.configfiledir)
            shutil.copyfile(self.trailerpicture_default_init, self.trailerpicture_default)
        if not os.path.exists(self.trailervideo_default):
            if not os.path.exists(self.configfiledir):
                os.makedirs(self.configfiledir)
            shutil.copyfile(self.trailervideo_default_init, self.trailervideo_default)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        with open(self.configfilepath, encoding='UTF-8') as f:
            config = json.load(f, object_pairs_hook=OrderedDict)
            return config

    def save_config(self, config):
        with open(self.configfilepath, 'w', encoding='UTF-8') as f:
            json.dump(config, f)
        return

    def get_resource_dir(self):
        return resource_dir

    def get_url_file_path(self):
        config = self.load_config()
        url_file_path = config[0]["urlpathlist"][0]["path"]
        url_file_path_file = pathlib.Path(url_file_path)
        if not url_file_path_file.is_file():
            url_file_path = ''
        if url_file_path == '' :
            if not os.path.exists(self.url_file) :
                if not os.path.exists(resource_dir):
                    os.makedirs(resource_dir)
                shutil.copyfile(self.url_file_init, self.url_file)
            url_file_path = self.url_file
            self.set_url_file_path(url_file_path)
        return url_file_path

    def set_url_file_path(self, file_path):
        config = self.load_config()
        config[0]["urlpathlist"][0]["path"] = file_path
        Config().save_config(config)
        return


    def load_url_info(self, file_path):
        try:
            all_url_info = open(file_path).readlines()
            return all_url_info
        except Exception:
            return ""

    def get_download_dir(self):
        config = self.load_config()
        download = config[1]["downloaddirlist"][0]["dir"]
        if download=="":
            download = download_dir
        return download

    def set_download_dir(self, dir):
        config = self.load_config()
        config[1]["downloaddirlist"][0]["dir"] = dir
        Config().save_config(config)
        return

    def get_thread_number(self):
        config = self.load_config()
        download_dir = config[2]["threadnumberlist"][0]["number"]
        return download_dir

    def set_thread_number(self, number):
        config = self.load_config()
        config[2]["threadnumberlist"][0]["number"] = number
        Config().save_config(config)
        return


    def get_failed_retry_times(self):
        config = self.load_config()
        download_dir = config[3]["failedretrytimeslist"][0]["time"]
        return download_dir


    def set_failed_retry_times(self, time):
        config = self.load_config()
        config[3]["failedretrytimeslist"][0]["time"] = time
        Config().save_config(config)
        return


    def get_connect_timeout(self):
        config = self.load_config()
        download_dir = config[4]["connecttimeoutlist"][0]["time"]
        return download_dir

    def set_connect_timeout(self, time):
        config = self.load_config()
        config[4]["connecttimeoutlist"][0]["time"] = time
        Config().save_config(config)
        return


    def get_headertext(self):
        config = self.load_config()
        headertext = config[5]["headertextlist"][0]["text"]
        if isinstance(headertext, str):
            headertext = ''.join(headertext).replace('\',', '\',\n')
        if isinstance(headertext, list):
            headertext = ','.join(headertext).replace('\',','\',\n')
        return headertext


    def get_headerdict(self):
        config = self.load_config()
        headertext = config[5]["headertextlist"][0]["text"]
        headerdict = ast.literal_eval("{"+headertext+"}")
        return headerdict


    def set_headertext(self, headertext):
        config = self.load_config()
        config[5]["headertextlist"][0]["text"] = headertext
        Config().save_config(config)
        return


    def get_debugflag(self):
        return debug_flag


    def set_debugflag(self, flag):
        global debug_flag
        self.debug_flag = flag


    # Numbers of downloading threads concurrently
    def setThreadNum(self, num):
        self.THREADS = num

    def getThreadNum(self):
        return self.THREADS


    # def setHeaders(self, headers):
    #     self.HEADERS = headers
    #
    # def getHeaders(self):
    #     return self.HEADERS


    # Retry times
    def setRetryTimes(self, times):
        self.RETRY = times

    def getRetryTimes(self):
        return self.RETRY


    # Setting timeout
    def setTimeOut(self, timeoutval):
        self.TIMEOUT = timeoutval


    def getTimeOut(self):
        return self.TIMEOUT


    # # Setting save folder/path
    # def setSaveFolder(self, path):
    #     self.SAVEFOLDER = path
    #
    # def getSaveFolder(self):
    #     return self.SAVEFOLDER


    def get_trailerpicture_dir(self):
        md5_optvalues = self.get_MD5optionvaluses_dict()
        trailerpicturepath = ""
        for optionid, optionval in md5_optvalues.items():
            if int(optionid) == 2:
                return optionval
        return trailerpicturepath


    def set_trailerpicture_dir(self, dir):
        md5_optvalues = self.get_MD5optionvaluses_dict()
        md5_optvalues['2'] = dir
        md5_optvalues_str = str(md5_optvalues)
        if md5_optvalues_str.startswith("{"):
            md5_optvalues_str = md5_optvalues_str.replace("{", "")
        if md5_optvalues_str.endswith("}"):
            md5_optvalues_str = md5_optvalues_str.replace("}", "")
        self.set_MD5optionvalues(md5_optvalues_str)
        return


    def get_trailervideo_dir(self):
        md5_optvalues = self.get_MD5optionvaluses_dict()
        trailervideopath = ""
        for optionid, optionval in md5_optvalues.items():
            if int(optionid) == 3:
                return optionval
        return trailervideopath


    def set_trailervideo_dir(self, dir):
        md5_optvalues = self.get_MD5optionvaluses_dict()
        md5_optvalues['3'] = dir
        md5_optvalues_str = str(md5_optvalues)
        if md5_optvalues_str.startswith("{"):
            md5_optvalues_str = md5_optvalues_str.replace("{", "")
        if md5_optvalues_str.endswith("}"):
            md5_optvalues_str = md5_optvalues_str.replace("}", "")
        self.set_MD5optionvalues(md5_optvalues_str)
        return


    # current used option id
    def get_MD5optionid(self):
        config = self.load_config()
        optionid = config[6]["md5optionlist"][0]["md5optionid"]
        if optionid == "" or optionid == "-1":
            optionid = md5_optionid_default
            self.set_MD5options(md5_options_default)
        return optionid


    def set_MD5optionid(self, optionid):
        config = self.load_config()
        config[6]["md5optionlist"][0]["md5optionid"] = str(optionid)
        Config().save_config(config)
        return


    def get_MD5options(self):
        config = self.load_config()
        md5options = config[6]["md5optionlist"][0]["md5options"]
        if md5options == "":
            md5options = md5_options_default
        return md5options


    def get_MD5options_list(self):
        config = self.load_config()
        md5options = config[6]["md5optionlist"][0]["md5options"]
        if md5options == "":
            md5options = md5_options_default
        try:
            options_list = md5options.split(",")
        except  Exception as ex:
            options_list = md5_options_default.split(",")
            self.set_MD5options(md5_options_default)
        return options_list


    def set_MD5options(self, options):
        config = self.load_config()
        config[6]["md5optionlist"][0]["md5options"] = options
        Config().save_config(config)
        return


    def get_MD5optionvaluses_dict(self):
        config = self.load_config()
        md5optionvalues = config[6]["md5optionvaluelist"][0]["md5optionvalues"]
        if md5optionvalues == "":
            md5optionvalues = "'0': '','1': '','2':" + self.trailerpicture_default + ",'3': " + self.trailervideo_default
        try:
            if md5optionvalues.startswith("{"):
                md5optionvalues = md5optionvalues.replace("{", "")
            if md5optionvalues.endswith("}"):
                md5optionvalues = md5optionvalues.replace("}", "")
            md5optionvalues_dict = eval("{" + md5optionvalues + "}")
            if md5optionvalues_dict['2'].strip() == "" :
                md5optionvalues_dict['2'] = self.trailerpicture_default
                self.set_MD5optionvalues(str(md5optionvalues_dict))
            if md5optionvalues_dict['3'].strip() == "":
                md5optionvalues_dict['3'] = self.trailervideo_default
                self.set_MD5optionvalues(str(md5optionvalues_dict))
        except  Exception as ex:
            md5optionvalues = "'0': '','1': '','2':'" + self.trailerpicture_default + "','3':'" + self.trailervideo_default + "'"
            md5optionvalues_dict = eval("{" + md5optionvalues + "}")
            self.set_MD5optionvalues(md5optionvalues)
        return md5optionvalues_dict


    def set_MD5optionvalues(self, options):
        config = self.load_config()
        config[6]["md5optionvaluelist"][0]["md5optionvalues"] = options
        Config().save_config(config)
        return

    # current used option id
    def get_namingruleoptionid(self):
        config = self.load_config()
        optionid = config[7]["namingruleoptionlist"][0]["namingruleoptionid"]
        if optionid == "" or optionid == "-1":
            optionid = namingrule_optionid_default
            self.set_namingruleoptions(namingrule_options_default)
        return optionid

    def set_namingruleoptionid(self, optionid):
        config = self.load_config()
        config[7]["namingruleoptionlist"][0]["namingruleoptionid"] = str(optionid)
        Config().save_config(config)
        return

    def get_namingruleoptions(self):
        config = self.load_config()
        options = config[7]["namingruleoptionlist"][0]["namingruleoptions"]
        if options == "":
            options = namingrule_options_default
        return options

    def get_namingruleoptions_list(self):
        config = self.load_config()
        options = config[7]["namingruleoptionlist"][0]["namingruleoptions"]
        if options == "":
            options = namingrule_options_default
        try:
            options_list = options.split(",")
        except  Exception as ex:
            options_list = namingrule_options_default.split(",")
            self.set_namingruleoptions(namingrule_options_default)
        return options_list

    def set_namingruleoptions(self, options):
        config = self.load_config()
        config[7]["namingruleoptionlist"][0]["namingruleoptions"] = options
        Config().save_config(config)
        return

