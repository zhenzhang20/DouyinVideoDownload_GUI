"""
Define all path.
Note: absolute path
"""
import os
import json
from collections import OrderedDict
from SourceCode.pub_func import utils_filepath
import shutil

#url_init_dir = os.path.join('Resource', 'config_dir')
#config_init_dir = os.path.join('Resource', 'config_dir')

# resource_dir = os.path.join(os.getcwd(), 'Resource')
download_dir = os.path.join(os.getcwd(), 'download')
#url_dir = os.path.join(os.getcwd(), 'Resource')

debug_flag = False


class VideoConfig(object):
    def __init__(self):
        self.vconfigfiledir = utils_filepath.resource_path(os.path.join(download_dir))
        self.vconfigfilepath = utils_filepath.resource_path(os.path.join(download_dir, 'videosdownload.json'))
        # self.configfilepath_init = utils_filepath.resource_path(os.path.join(config_init_dir, 'config_init.json'))
        # self.url_file_init = utils_filepath.resource_path(os.path.join(url_init_dir, 'url_init.txt'))
        # self.url_file = utils_filepath.resource_path(os.path.join(url_dir, 'url.txt'))


    def load_vconfig(self):
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        if not os.path.exists(self.vconfigfilepath):
            open(self.vconfigfilepath, 'w').close()
            return None
        else:
            with open(self.vconfigfilepath) as f:
                try:
                    vconfig = json.load(f, object_pairs_hook=OrderedDict)
                except Exception as ex:
                    # QMessageBox.warning(self, '加载下载记录文件失败，记录将被清空')
                    return None
            return vconfig

    def save_vconfig(self, vconfig):
        with open(self.vconfigfilepath, 'w') as f:
            json.dump(vconfig, f)
        return

    # number, blogger, bloggerid, title, size, status, downtime, filetype
    # def construct_one_vconfig(self, number, blogger, bloggerid, vtitle, vsize, status, downtime, filetype ):
    #     oneconfig = OrderedDict()
    #     oneconfig['number'] = number
    #     oneconfig['blogger'] = blogger
    #     oneconfig['bloggerid'] = bloggerid
    #     oneconfig['vtitle'] = vtitle
    #     oneconfig['vsize'] = vsize
    #     oneconfig['status'] = status
    #     oneconfig['downtime'] = downtime
    #     oneconfig['filetype'] = filetype
    #     return oneconfig

    # number, blogger, bloggerid, title, size, status, downtime, filetype, identifykey, savedfilename
    # identifykey： 默认的文件名，不一定是存储时用的文件名
    # savedfilename： 用户定义的，真实存储时用的文件名
    def construct_one_vconfig(self, number, blogger, bloggerid, vtitle, vsize, status, downtime, filetype, identifykey, savedfilename ):
        oneconfig = OrderedDict()
        oneconfig['number'] = str(number)
        oneconfig['blogger'] = blogger
        oneconfig['bloggerid'] = bloggerid
        oneconfig['vtitle'] = vtitle
        oneconfig['vsize'] = vsize
        oneconfig['status'] = status
        oneconfig['downtime'] = downtime
        oneconfig['filetype'] = filetype
        oneconfig['identifykey'] = identifykey
        oneconfig['savedfilename'] = savedfilename
        return oneconfig


    def add_one_vconfig(self, config):
        vconfig = self.load_vconfig()
        if vconfig is None:
            vconfig = []
        vconfig.append(config)
        self.save_vconfig(vconfig)

    def update_one_vconfig(self, config):
        vconfig = self.load_vconfig()
        for i in range(len(vconfig)):
                if vconfig[i].get("identifykey") == config.get("identifykey"):
                    print("will update number " + config.get('number') + "    identifykey " + config.get("identifykey"))
                    vconfig[i]['number'] = config.get('number')
                    vconfig[i]['blogger'] = config.get('blogger')
                    vconfig[i]['bloggerid'] = config.get('bloggerid')
                    vconfig[i]['vtitle'] = config.get('vtitle')
                    vconfig[i]['vsize'] = config.get('vsize')
                    vconfig[i]['status'] = config.get('status')
                    vconfig[i]['downtime'] = config.get('downtime')
                    vconfig[i]['filetype'] = config.get('filetype')
                    vconfig[i]['identifykey'] = config.get('identifykey')
                    vconfig[i]['savedfilename'] = config.get('savedfilename')
        self.save_vconfig(vconfig)

    def update_one_video_savedfilename(self, identifykey, newsavedfilename):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                vconfig[i]['number'] = self.get_video_number_by_identifykey(identifykey)
                vconfig[i]['blogger'] = self.get_video_blogger_by_identifykey(identifykey)
                vconfig[i]['bloggerid'] = self.get_video_bloggerID_by_identifykey(identifykey)
                vconfig[i]['vtitle'] = self.get_video_optionvalue_by_identifykey(identifykey, 'vtitle')
                vconfig[i]['vsize'] = self.get_video_optionvalue_by_identifykey(identifykey, 'vsize')
                vconfig[i]['status'] = self.get_video_optionvalue_by_identifykey(identifykey, 'status')
                vconfig[i]['downtime'] = self.get_video_optionvalue_by_identifykey(identifykey, 'downtime')
                vconfig[i]['filetype'] = self.get_video_optionvalue_by_identifykey(identifykey, 'filetype')
                vconfig[i]['identifykey'] = self.get_video_optionvalue_by_identifykey(identifykey, 'identifykey')
                vconfig[i]['savedfilename'] = newsavedfilename
        return None


    def get_video_numbers(self):
        vconfig = self.load_vconfig()
        if vconfig is None:
            vconfig = []
        return len(vconfig)

    def get_key_values(self, key):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        values = []
        for i in range(len(vconfig)):
            values.append(vconfig[i].get(key))
        return values

    # config is OrderedDict
    def get_key_value(self, config, key ):
        if config is None:
            return None
        return config.get(key)

    def get_vconfiginfo_by_id(self, number):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['number'] == number:
                return config
        return None

    def get_vconfig_pos_by_id(self, number):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['number'] == number:
                return i
        return None

    def get_vconfiginfo_by_infos(self, bloggerid, vtitle, filetype):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['bloggerid'] == bloggerid \
                and int(config['vtitle']) == vtitle \
                and int(config['filetype']) == filetype :
                return config
        return None

    def is_empty_config(self):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return True
        return False

    # def is_video_exist(self, bloggerid, vtitle, filetype, status):
    #     vconfig = self.load_vconfig()
    #     if vconfig is None:
    #         return False
    #     for i in range(len(vconfig)):
    #         config = vconfig[i]
    #         if config['bloggerid'] == bloggerid \
    #             and config['vtitle'] == vtitle \
    #             and config['filetype'] == filetype \
    #             and config['status'] == status    :
    #             return True
    #     return False

    # def is_video_exist_by_identifykey(self, identifykey):
    #     vconfig = self.load_vconfig()
    #     if vconfig is None:
    #         return False
    #     for i in range(len(vconfig)):
    #         config = vconfig[i]
    #         if config['identifykey'] == identifykey :
    #             return True
    #     return False

    def is_video_downloaded_success(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey \
                and config['status'] == "success" :
                return True
            elif config['identifykey'] == identifykey \
                and config['status'] == "failed" :
                return False
        return None



    def get_video_number_by_identifykey(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                return config['number']
        return None


    def get_video_savedfilename_by_identifykey(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                return config['savedfilename']
        return None


    def get_video_bloggerID_by_identifykey(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                return config['bloggerid']
        return None


    def get_video_blogger_by_identifykey(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                return config['blogger']
        return None


    def get_video_title_by_identifykey(self, identifykey):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey :
                return config['vtitle']
        return None


    def get_video_optionvalue_by_identifykey(self, identifykey, key):
        vconfig = self.load_vconfig()
        if vconfig is None:
            return None
        for i in range(len(vconfig)):
            config = vconfig[i]
            if config['identifykey'] == identifykey:
                return config[key]
        return None

    # def get_vconfiginfo_by_infos(self, blogger, bloggerid, vtitle, filetype):
    #     vconfig = self.load_vconfig()
    #     if vconfig is None:
    #         return None
    #     for i in range(len(vconfig)):
    #         config = vconfig[i]
    #         if int(config['blogger']) == blogger \
    #             and config['bloggerid'] == bloggerid \
    #             and int(config['vtitle']) == vtitle \
    #             and int(config['filetype']) == filetype :
    #             return config
    #     return None

    def get_debugflag(self):
        return debug_flag

    def set_debugflag(self, flag):
        global debug_flag
        self.debug_flag = flag

            # def load_config(self):
    #     if not os.path.exists(self.configfilepath):
    #         if not os.path.exists(self.configfiledir):
    #             os.makedirs(self.configfiledir)
    #         shutil.copyfile(self.configfilepath_init, self.configfilepath)
    #         if not os.path.exists(download_dir):
    #             os.makedirs(download_dir)
    #     with open(self.configfilepath) as f:
    #         config = json.load(f, object_pairs_hook=OrderedDict)
    #         return config
    #
    # def save_config(self, config):
    #     with open(self.configfilepath, 'w') as f:
    #         json.dump(config, f)
    #     return
    #
    # def get_url_file_path(self):
    #     config = self.load_config()
    #     url_file_path = config[0]["urlpathlist"][0]["path"]
    #     if url_file_path == '' :
    #         if not os.path.exists(self.url_file) :
    #             if not os.path.exists(resource_dir):
    #                 os.makedirs(resource_dir)
    #             shutil.copyfile(self.url_file_init, self.url_file)
    #         url_file_path = self.url_file
    #     return url_file_path
    #
    # def set_url_file_path(self, file_path):
    #     config = self.load_config()
    #     config[0]["urlpathlist"][0]["path"] = file_path
    #     Config().save_config(config)
    #     return
    #
    #
    # def load_url_info(self, file_path):
    #     try:
    #         all_url_info = open(file_path).readlines()
    #         return all_url_info
    #     except Exception:
    #         return ""
    #
    # def get_download_dir(self):
    #     config = self.load_config()
    #     download = config[1]["downloaddirlist"][0]["dir"]
    #     if download=="":
    #         download = download_dir
    #     return download
    #
    # def set_download_dir(self, dir):
    #     config = self.load_config()
    #     config[1]["downloaddirlist"][0]["dir"] = dir
    #     Config().save_config(config)
    #     return
    #
    # def get_thread_number(self):
    #     config = self.load_config()
    #     download_dir = config[2]["threadnumberlist"][0]["number"]
    #     return download_dir
    #
    # def set_thread_number(self, number):
    #     config = self.load_config()
    #     config[2]["threadnumberlist"][0]["number"] = number
    #     Config().save_config(config)
    #     return
    #
    #
    # def get_failed_retry_times(self):
    #     config = self.load_config()
    #     download_dir = config[3]["failedretrytimeslist"][0]["time"]
    #     return download_dir
    #
    #
    # def set_failed_retry_times(self, time):
    #     config = self.load_config()
    #     config[3]["failedretrytimeslist"][0]["time"] = time
    #     Config().save_config(config)
    #     return
    #
    #
    # def get_connect_timeout(self):
    #     config = self.load_config()
    #     download_dir = config[4]["connecttimeoutlist"][0]["time"]
    #     return download_dir
    #
    #
    # def set_connect_timeout(self, time):
    #     config = self.load_config()
    #     config[4]["connecttimeoutlist"][0]["time"] = time
    #     Config().save_config(config)
    #     return
    #
    # def get_headertext(self):
    #     config = self.load_config()
    #     headertext = config[5]["headertextlist"][0]["text"]
    #     if isinstance(headertext, str):
    #         headertext = ''.join(headertext).replace('\',', '\',\n')
    #     if isinstance(headertext, list):
    #         headertext = ','.join(headertext).replace('\',','\',\n')
    #     return headertext
    #
    #
    # def set_headertext(self, headertext):
    #     config = self.load_config()
    #     config[5]["headertextlist"][0]["text"] = headertext
    #     Config().save_config(config)
    #     return



