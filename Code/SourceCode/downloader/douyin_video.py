# -*- coding: utf-8 -*-
import os, platform, re, time, json, hashlib, copy, codecs
import urllib
import pathlib
from threading import Thread
import js2py
import requests
from six.moves import queue as Queue
from SourceCode.pub_func import utils_md5
from SourceCode.pub_func import utils_public

class Resolver_Douyin(object):
    def __init__(self, config, videoconfig):
        self.config = config
        self.videoconfig = videoconfig
        self.videoconfigs = self.videoconfig.load_vconfig()

    # def download_douyin(self, medium_type, uri, medium_url, target_folder):
    def download_douyin(self, medium_type, filename, medium_url, target_folder, user_id, desc):
        headers = copy.copy(self.config.get_headerdict())
        target_folder_md5 = (str(target_folder)).strip() + "_md5"
        # update :
        # support two types of file name
        #   0 : 视频标识_视频名称
        #   1 : 视频编号_主播ID_主播名称_视频标识_视频名称
        namingruleoptionid = self.config.get_namingruleoptionid()
        file_name = filename




        # desc = utils_public.clean_zh_text(desc)
        if medium_type == 'video':
            file_name += '.mp4'
            headers['user-agent'] = 'Aweme/27014 CFNetwork/974.2.1 Darwin/18.0.0'
        elif medium_type == 'image':
            file_name += '.jpg'
            file_name = file_name.replace("/", "-")
        else:
            return

        if namingruleoptionid == '1' :
            if self.videoconfig.get_video_savedfilename_by_identifykey(filename) is not None :
                savedfilename = self.videoconfig.get_video_savedfilename_by_identifykey(filename)
                newfilename = self.videoconfig.get_video_number_by_identifykey(filename) + "_" + \
                                self.videoconfig.get_video_bloggerID_by_identifykey(filename) + "_" + \
                                self.videoconfig.get_video_blogger_by_identifykey(filename) + "_" + file_name
        else :
            savedfilename = file_name
            newfilename = file_name

        file_path = os.path.join(target_folder, file_name)

        if not self.videoconfig.is_empty_config():
            if self.videoconfig.is_video_downloaded_success(filename) is not None and self.videoconfig.is_video_downloaded_success(filename):
                self.rename_downloadfile(savedfilename, newfilename, target_folder, target_folder_md5)
                self.videoconfig.update_one_video_savedfilename(filename, file_name)
                    # newconfig = self.videoconfig.construct_one_vconfig(number, blogger, bloggerid, vtitle, vsize,
                    #                                                    status,
                    #                                                    downtime, filetype, identifykey, savedfilename)
                    # self.videoconfig.update_one_vconfig(newconfig)
                print(file_name + " 已经爬取过了，放弃爬取")
                return
        # if os.path.isfile(file_path):
        #     print(file_name + " 已经爬取过了，文件保存在 " + file_path + " 放弃爬取")
        #     return
        # Windows Terminal 执行会有乱码，导致运行失败
        #print("Downloading %s from %s.\n" % (file_name, medium_url))
        print("Downloading %s from %s.\n" % (file_name.encode("gbk", "ignore").decode("gbk", "ignore"), medium_url))
        # VIDEOID_DICT[VIDEO_ID] = 1  # 记录已经下载的视频
        retry_times = 0
        download_status = "success"

        while retry_times < self.config.getRetryTimes():
            try:
                resp = requests.get(medium_url, headers=headers, stream=True, timeout=self.config.getTimeOut())
                if resp.status_code == 403:
                    retry_times = self.config.getRetryTimes()
                    print("Access Denied when retrieve %s.\n" % medium_url)
                    raise Exception("Access Denied")
                with open(file_path, 'wb') as fh:
                    for chunk in resp.iter_content(chunk_size=1024):
                        fh.write(chunk)
                # check md5 option and auto change if necessary
                md5_optionid = self.config.get_MD5optionid()
                file_path_md5 = os.path.join(target_folder_md5, file_name)
                if not int(md5_optionid) == 0:
                    if not os.path.isdir(target_folder_md5):
                        os.mkdir(target_folder_md5)

                if int(md5_optionid) == 1:
                    # 复制
                    utils_md5.changemd5_by_append_uuid4(file_path_md5, file_path)
                elif int(md5_optionid) == 2:
                    image = self.config.get_trailerpicture_dir()
                    if not image == "":
                        mergevideo = image + ".mp4"
                        cmd = utils_md5.generate_cmd_img2video(mergevideo, image)
                        print(cmd)
                        res = utils_md5.run_ffmpeg_cmd(cmd)
                elif int(md5_optionid) == 3:
                    mergevideo = self.config.get_trailervideo_dir()

                if int(md5_optionid) == 2 or int(md5_optionid) == 3:
                    if not mergevideo == "":
                        if (platform.system() == 'Windows'):
                            file_path = file_path.replace("\\", "/")
                            mergevideo = mergevideo.replace("\\", "/")
                        cmd, tempfilename = utils_md5.generate_cmd_merge_videos(file_path_md5, file_path, mergevideo)
                        print(cmd)
                        res = utils_md5.run_ffmpeg_cmd(cmd)
                        if os.path.isfile(tempfilename):
                            os.remove(tempfilename)

                mtime = os.stat(file_path).st_mtime
                file_modify_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                #  file_size Unit is MB
                file_size = os.path.getsize(file_path)
                file_size = file_size / float(1024 * 1024)
                file_size = round(file_size, 2)
                # medium_type, user_id, desc, status, filesize, file_modify_time, identifykey
                video_nums = self.videoconfig.get_video_numbers()
                number = video_nums+1
                blogger = "未知"
                bloggerid = user_id
                vtitle = desc
                status = download_status
                vsize = str(file_size) + "MB"
                downtime = str(file_modify_time)
                filetype = ""
                if medium_type == 'video':
                    filetype = 'mp4'
                elif medium_type == 'image':
                    filetype = '.jpg'
                identifykey = filename
                savedfilename = filename
                isReDownload = False
                # 判断是否下载过，但是没成功
                if not self.videoconfig.is_empty_config():
                    if self.videoconfig.is_video_downloaded_success(identifykey) is not None and not self.videoconfig.is_video_downloaded_success(identifykey):
                        if self.videoconfig.get_video_number_by_identifykey(identifykey) is not None:
                            isReDownload = True
                if (isReDownload):
                    number = self.videoconfig.get_video_number_by_identifykey(identifykey)
                if namingruleoptionid == '1':
                    savedfilename = str(number) + "_" + bloggerid + "_" + blogger + "_" + identifykey
                outputsavedfilename = savedfilename+file_name[file_name.rfind('.'):]
                newconfig = self.videoconfig.construct_one_vconfig(number, blogger, bloggerid, vtitle, vsize, status,
                                                                   downtime, filetype, identifykey, savedfilename)
                if(isReDownload):
                    newconfig = self.videoconfig.construct_one_vconfig(number, blogger, bloggerid, vtitle, vsize, status,
                                                           downtime, filetype, identifykey, savedfilename)
                    self.videoconfig.update_one_vconfig(newconfig)
                    self.rename_downloadfile(file_name, outputsavedfilename, target_folder, target_folder_md5)
                    break
                self.videoconfig.add_one_vconfig(newconfig)
                self.rename_downloadfile(file_name, outputsavedfilename, target_folder, target_folder_md5)
                # print("Dummy: "
                #       "         medium_type = " + medium_type +
                #       # "         filename = " + uri +
                #       # "         target_folder = " + target_folder +
                #       "         user_id = " + user_id,
                #       "         desc = " + desc,
                #       "         status = " + download_status,
                #       "         filesize = " + str(file_size) + "MB"
                #       "         modifytime = " + str(file_modify_time))

                break
            except:
                pass
            retry_times += 1
        else:
            try:
                os.remove(file_path)
            except OSError:
                pass
            download_status = "failed"
            video_nums = self.videoconfig.get_video_numbers()
            number = video_nums + 1
            blogger = "未知"
            bloggerid = user_id
            vtitle = desc
            status = download_status
            vsize = str("0") + "MB"
            downtime = str("")
            filetype = ""
            if medium_type == 'video':
                filetype = 'mp4'
            elif medium_type == 'image':
                filetype = '.jpg'
            identifykey = filename
            savedfilename = filename
            if namingruleoptionid == '1':
                savedfilename = str(number) + "_" + bloggerid + "_" + blogger + "_" + identifykey
            newconfig = self.videoconfig.construct_one_vconfig(number, blogger, bloggerid, vtitle, vsize, status,
                                                               downtime, filetype, identifykey, savedfilename)
            # 加入已下载库
            self.videoconfig.add_one_vconfig(newconfig)
            # print("Dummy: "
            #       "         medium_type = " + medium_type +
            #       # "         filename = " + uri +
            #       # "         target_folder = " + target_folder +
            #       "         user_id = " + user_id,
            #       "         desc = " + desc,
            #       "         status = " + download_status)
            print("Failed to retrieve %s from %s.\n" % (filename, medium_url))
            time.sleep(1)

    def rename_downloadfile(self, ori_file_name, new_file_name, target_folder, target_folder_md5):
        try:
            if ori_file_name != new_file_name:
                file_path = os.path.join(target_folder, ori_file_name)
                saved_file_path = file_path.replace(ori_file_name, new_file_name)
                os.rename(file_path, saved_file_path)
                file_path_md5 = os.path.join(target_folder_md5, ori_file_name)
                saved_file_path_md5 = file_path_md5.replace(ori_file_name, new_file_name)
                os.rename(file_path_md5, saved_file_path_md5)
        except Exception as e:
            return

    def get_real_address_douyin(self, url):
        if url.find('v.douyin.com') < 0:
            return url
        # res = requests.get(url, headers=self.config.get_headerdict(), allow_redirects=False)
        res = requests.get(url, headers=self.config.get_headerdict(), allow_redirects=False)
        return res.headers['Location'] if res.status_code == 302 else None

    def get_real_address_by_id_douyin(self, id):
        url = "https://www.iesdouyin.com/share/user/" + id
        res = requests.get(url, headers=self.config.get_headerdict(), allow_redirects=False)
        return res.headers['Location'] if res.status_code == 302 else None

    def get_dytk_douyin(self, url):
        res = requests.get(url, headers=self.config.get_headerdict())
        if not res:
            return None
        dytk = re.findall("dytk: ['\"](.*)['\"]", res.content.decode('utf-8'))
        if len(dytk):
            return dytk[0]
        return None


class DownloadWorker_Douyin(Thread):
    def __init__(self, queue, config, videoconfig):
        Thread.__init__(self)
        self.queue = queue
        self.config = config
        self.videoconfig = videoconfig
        self.videoconfigs = self.videoconfig.load_vconfig()

    def run(self):
        resolver = Resolver_Douyin(self.config, self.videoconfig)

        while True:
            medium_type, uri, download_url, target_folder, user_id, desc = self.queue.get()
            resolver.download_douyin(medium_type, uri, download_url, target_folder, user_id, desc)
            self.queue.task_done()



#   download_status:
#       RUNNING
#       FAILED
#       FINISH
#       INVALIDURL

class Time_Consume(object):
    def __init__(self):
        self.STATUS_FAILED = 'FAILED'
        self.STATUS_FINISH = 'FINISH'

class CrawlerScheduler_Douyin(object):
    STATUS_RUNNING = 'RUNNING'
    STATUS_FAILED = 'FAILED'
    STATUS_FINISH = 'FINISH'
    STATUS_INVALIDURL = 'INVALIDURL'
    def __init__(self, urls, config, videoconfig):
        self.config = config
        self.configs = config.load_config()
        self.videoconfig = videoconfig
        self.videoconfigs = videoconfig.load_vconfig()
        # videoconfig.get_key_value(videoconfig,"number")
        # videoconfig.get_key_value(videoconfig,"number")
        # config.load_config()
        self.numbers = []
        self.challenges = []
        self.musics = []
        self.resolver = Resolver_Douyin(self.config, self.videoconfig)
        self.download_status = self.STATUS_RUNNING


        self.url_file_path = self.config.get_url_file_path()
        self.config.load_url_info(self.url_file_path)

        for i in range(len(urls)):
            url = self.resolver.get_real_address_douyin(urls[i])
            if not url:
                continue
            if url.find('/share/video/') > 0:
                url = self._get_user_link_from_video(url)
            if re.search('share/user', url):
                self.numbers.append(url)
            if re.search('share/challenge', url):
                self.challenges.append(url)
            if re.search('share/music', url):
                self.musics.append(url)

        with open(str(self.config.js_file), encoding='UTF-8') as f:
            self.js = f.read()

        self.queue = Queue.Queue()
        self.scheduling()


    def generateSignature(self, value):
        js = self.js.replace('__INPUT__', str(value))
        return js2py.eval_js(js)

    @staticmethod
    def calculateFileMd5(filename):
        hmd5 = hashlib.md5()
        fp = open(filename, "rb")
        hmd5.update(fp.read())
        return hmd5.hexdigest()

    def scheduling(self):
        for x in range(self.config.getThreadNum()):
            worker = DownloadWorker_Douyin(self.queue, self.config, self.videoconfig)
            worker.daemon = True
            worker.start()
        if len(self.numbers) == 0:
            self.download_status = self.STATUS_INVALIDURL
            return
        for url in self.numbers:
            self.download_user_videos(url)
        for url in self.challenges:
            # self.download_challenge_videos(url)
            print("convert 2 finish ........... !!!!")
        for url in self.musics:
            # self.download_music_videos(url)
            print("convert 3 finish ........... !!!!")
        self.download_status = 'FINISH'

    def download_user_videos(self, url):
        number = re.findall(r'share/user/(\d+)', url)
        if not len(number):
            return
        dytk = self.resolver.get_dytk_douyin(url)
        hostname = urllib.parse.urlparse(url).hostname
        if hostname != 't.tiktok.com' and not dytk:
            return
        user_id = number[0]
        params = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        sec_uid = params['sec_uid'][0]
        # video_count = self._download_user_media(user_id, dytk, url)
        video_count = self._download_user_media(user_id, dytk, url, sec_uid)
        self.queue.join()
        print("\nAweme number %s, video number %s\n\n" %
              (user_id, str(video_count)))
        print("\nFinish Downloading All the videos from %s\n\n" % user_id)

    def download_challenge_videos(self, url):
        challenge = re.findall('share/challenge/(\d+)', url)
        if not len(challenge):
            return
        challenges_id = challenge[0]
        video_count = self._download_challenge_media(challenges_id, url)
        self.queue.join()
        print("\nAweme challenge #%s, video number %d\n\n" %
              (challenges_id, video_count))
        print("\nFinish Downloading All the videos from #%s\n\n" % challenges_id)

    def download_music_videos(self, url):
        music = re.findall('share/music/(\d+)', url)
        if not len(music):
            return
        musics_id = music[0]
        video_count = self._download_music_media(musics_id, url)
        self.queue.join()
        print("\nAweme music @%s, video number %d\n\n" %
              (musics_id, video_count))
        print("\nFinish Downloading All the videos from @%s\n\n" % musics_id)

    def _join_download_queue(self, user_id, aweme, target_folder):
        try:
            if aweme.get('video', None):
                uri = aweme['video']['play_addr']['uri']
                download_url = "https://aweme.snssdk.com/aweme/v1/play/?{0}"
                download_params = {
                    'video_id': uri,
                    'line': '0',
                    'ratio': '720p',
                    'media_type': '4',
                    'vr_type': '0',
                    'test_cdn': 'None',
                    'improve_bitrate': '0',
                    'iid': '35628056608',
                    # 'device_id': '46166618999',
                    'device_id': '46166618998',
                    'os_api': '18',
                    'app_name': 'aweme',
                    'channel': 'App%20Store',
                    'idfa': '00000000-0000-0000-0000-000000000000',
                    'device_platform': 'iphone',
                    'build_number': '27014',
                    'vid': '2ED380A7-F09C-6C9E-90F5-862D58F3129C',
                    'openudid': '21dae85eeac1da35a69e2a0ffeaeef61c78a2e98',
                    'device_type': 'iPhone8%2C2',
                    'app_version': '2.7.0',
                    'version_code': '2.7.0',
                    'os_version': '12.0',
                    'screen_width': '1242',
                    'aid': '1128',
                    'ac': 'WIFI',
                    'is_play_url': '1'
                }
                if aweme.get('hostname') == 't.tiktok.com':
                    download_url = 'http://api.tiktokv.com/aweme/v1/play/?{0}'
                    download_params = {
                        'video_id': uri,
                        'line': '0',
                        'ratio': '720p',
                        'media_type': '4',
                        'vr_type': '0',
                        'test_cdn': 'None',
                        'improve_bitrate': '0',
                        'version_code': '1.7.2',
                        'language': 'en',
                        'app_name': 'trill',
                        'vid': 'D7B3981F-DD46-45A1-A97E-428B90096C3E',
                        'app_version': '1.7.2',
                        'device_id': '6619780206485964289',
                        'channel': 'App Store',
                        'mcc_mnc': '',
                        'tz_offset': '28800'
                    }
                url = download_url.format('&'.join([key + '=' + download_params[key] for key in download_params]))
                desc = aweme.get('desc', uri)

                filename = utils_public.clean_zh_text(uri) + "_" + utils_public.clean_zh_text(desc)

                self.queue.put(('video', filename, url, target_folder, user_id, desc))

            else:
                if aweme.get('image_infos', None):
                    image = aweme['image_infos']['label_large']
                    self.queue.put(
                        ('image', image['uri'], image['url_list'][0], target_folder))

        except KeyError:
            return
        except UnicodeDecodeError:
            print("Cannot decode response data from DESC %s" % aweme['desc'])
            return

    # def __download_favorite_media(self, user_id, dytk, hostname, signature, favorite_folder, video_count):
    #     if not os.path.exists(favorite_folder):
    #         os.makedirs(favorite_folder)
    #     # favorite_video_url = "https://%s/aweme/v1/aweme/favorite/" % hostname
    #     favorite_video_url = "https://%s/web/api/v2/aweme/like/" % hostname
    #     favorite_video_params = {
    #         'user_id': str(user_id),
    #         'count': '21',
    #         'max_cursor': '0',
    #         'aid': '1128',
    #         '_signature': signature,
    #         'dytk': in DownloadWorkerdytk
    #     }
    #     max_cursor = None
    #     while True:
    #         if max_cursor:
    #             favorite_video_params['max_cursor'] = str(max_cursor)
    #         res = requests.get(favorite_video_url,
    #                            headers=HEADERS, params=favorite_video_params)
    #         contentJson = json.loads(res.content.decode('utf-8'))
    #         favorite_list = contentJson.get('aweme_list', [])
    #         for aweme in favorite_list:
    #             video_count += 1
    #             aweme['hostname'] = hostname
    #             self._join_download_queue(aweme, favorite_folder)
    #         if contentJson.get('has_more'):
    #             max_cursor = contentJson.get('max_cursor')
    #         else:
    #             break
    #     return video_count

    def _download_user_media(self, user_id, dytk, url, sec_uid):
        requests.packages.urllib3.disable_warnings()
        # current_folder = os.getcwd()
        base_folder = self.config.get_download_dir()
        target_folder = os.path.join(base_folder, '%s' % user_id)
        if not os.path.isdir(target_folder):
            os.mkdir(target_folder)

        if not user_id:
            print("Number %s does not exist" % user_id)
            return
        hostname = urllib.parse.urlparse(url).hostname
        signature = self.generateSignature(str(user_id))
        user_video_url = "https://%s/web/api/v2/aweme/post/" % hostname
        user_video_params = {
            # 'user_id': str(user_id),
            'sec_uid': str(sec_uid),
            'count': '21',
            'max_cursor': '0',
            'aid': '1128',
            '_signature': signature,
            'dytk': dytk
        }
        if hostname == 't.tiktok.com':
            user_video_params.pop('dytk')
            user_video_params['aid'] = '1180'

        max_cursor, video_count = None, 0
        while True:
            if max_cursor:
                user_video_params['max_cursor'] = str(max_cursor)
            res = requests.get(user_video_url, headers=self.config.get_headerdict(),
                               params=user_video_params, verify=False)
            contentJson = json.loads(res.content.decode('utf-8'))
            aweme_list = contentJson.get('aweme_list', [])
            for aweme in aweme_list:
                video_count += 1
                aweme['hostname'] = hostname
                self._join_download_queue(user_id, aweme, target_folder)
            if contentJson.get('has_more'):
                max_cursor = contentJson.get('max_cursor')
            else:
                break
        # if True:
        #     favorite_folder = target_folder + '/favorite'
        #     video_count = self.__download_favorite_media(
        #         user_id, dytk, hostname, signature, favorite_folder, video_count)

        if video_count == 0:
            print("There's no video in number %s." % user_id)

        return video_count

    def _download_challenge_media(self, challenge_id, url):
        requests.packages.urllib3.disable_warnings()
        if not challenge_id:
            print("Challenge #%s does not exist" % challenge_id)
            return
        # current_folder = os.getcwd()
        base_folder = self.config.get_download_dir()
        target_folder = os.path.join(base_folder, '#%s' % challenge_id)

        if not os.path.isdir(target_folder):
            os.mkdir(target_folder)

        hostname = urllib.parse.urlparse(url).hostname
        signature = self.generateSignature(str(challenge_id) + '9' + '0')

        challenge_video_url = "https://%s/aweme/v1/challenge/aweme/" % hostname
        challenge_video_params = {
            'ch_id': str(challenge_id),
            'count': '9',
            'cursor': '0',
            'aid': '1128',
            'screen_limit': '3',
            'download_click_limit': '0',
            '_signature': signature
        }

        cursor, video_count = None, 0
        while True:
            if cursor:
                challenge_video_params['cursor'] = str(cursor)
                challenge_video_params['_signature'] = self.generateSignature(
                    str(challenge_id) + '9' + str(cursor))
            res = requests.get(challenge_video_url,
                               headers=self.config.get_headerdict(), params=challenge_video_params)
            try:
                contentJson = json.loads(res.content.decode('utf-8'))
            except:
                print(res.content)
            aweme_list = contentJson.get('aweme_list', [])
            if not aweme_list:
                break
            for aweme in aweme_list:
                aweme['hostname'] = hostname
                video_count += 1
                self._join_download_queue(aweme, target_folder)
                print("number: ", video_count)
            if contentJson.get('has_more'):
                cursor = contentJson.get('cursor')
            else:
                break
        if video_count == 0:
            print("There's no video in challenge %s." % challenge_id)
        return video_count

    def _download_music_media(self, music_id, url):
        requests.packages.urllib3.disable_warnings()
        if not music_id:
            print("Challenge #%s does not exist" % music_id)
            return
        # current_folder = os.getcwd()
        base_folder = self.config.get_download_dir()
        target_folder = os.path.join(base_folder, '@%s' % music_id)
        if not os.path.isdir(target_folder):
            os.mkdir(target_folder)

        hostname = urllib.parse.urlparse(url).hostname
        signature = self.generateSignature(str(music_id))
        music_video_url = "https://%s/aweme/v1/music/aweme/?{0}" % hostname
        music_video_params = {
            'music_id': str(music_id),
            'count': '9',
            'cursor': '0',
            'aid': '1128',
            'screen_limit': '3',
            'download_click_limit': '0',
            '_signature': signature
        }
        if hostname == 't.tiktok.com':
            for key in ['screen_limit', 'download_click_limit', '_signature']:
                music_video_params.pop(key)
            music_video_params['aid'] = '1180'

        cursor, video_count = None, 0
        while True:
            if cursor:
                music_video_params['cursor'] = str(cursor)
                music_video_params['_signature'] = self.generateSignature(
                    str(music_id) + '9' + str(cursor))

            url = music_video_url.format(
                '&'.join([key + '=' + music_video_params[key] for key in music_video_params]))
            res = requests.get(url, headers=self.config.get_headerdict())
            contentJson = json.loads(res.content.decode('utf-8'))
            aweme_list = contentJson.get('aweme_list', [])
            if not aweme_list:
                break
            for aweme in aweme_list:
                aweme['hostname'] = hostname
                video_count += 1
                self._join_download_queue(aweme, target_folder)
            if contentJson.get('has_more'):
                cursor = contentJson.get('cursor')
            else:
                break
        if video_count == 0:
            print("There's no video in music %s." % music_id)
        return video_count

    def _get_user_link_from_video(self, url):
        """从分享的单个视频链接获取用户信息
        @param: url 抖音单个视频链接
        @return: url 真实的用户首页链接
        """
        if url.find('/share/video/') < 0:
            return url
        # session = HTMLSession()
        # video_res = session.get(url, headers=MOBIE_HEADERS)
        video_res = requests.get(url, headers=self.config.get_headerdict())
        uid = re.findall("uid: ['\"](.*)['\"]", video_res.content.decode('utf-8'))
        # uid = video_res.content.search('uid: "{uid}"')['uid']
        USER_HOME_URL='https://www.iesdouyin.com/share/user/'
        return USER_HOME_URL + str(uid[0])

    def update_videoconfig(self):
        return self.videoconfigs

class ParseWebSiteURL():
    def parse_sites(self, fileName):
        with open(fileName, "rb") as f:
            txt = f.read().rstrip().lstrip()
            txt = codecs.decode(txt, 'utf-8')
            txt = txt.replace("\t", ",").replace(
                "\r", ",").replace("\n", ",").replace(" ", ",")
            txt = txt.split(",")
        numbers = list()
        for raw_site in txt:
            site = raw_site.lstrip().rstrip()
            if site:
                numbers.append(site)
        return numbers


#
# class CrawlerScheduler_Douyin_bak(object):
#     def __init__(self, config):
#         self.config = config
#         self.numbers = []
#         self.challenges = []
#         self.musics = []
#
#         print("convert dummy finish ........... !!!!")
#
# class CrawlerScheduler_Douyin_working(object):
#     def __init__(self):
#         self.msg = self.genMsg()
#
#     def __init1__(self, urls, config):
#         self.config = config
#         self.numbers = []
#         self.challenges = []
#         self.musics = []
#         # self.resolver = Resolver_Douyin(self.config)
#         # print("in douyin_video, debug in here")
#         return('ErrorMessage: ' , '打开失败', '无法打开，请手动打开下载目录')
#
#     def genMsg(self):
#         return('ErrorMessage: '+'打开失败'+'无法打开，请手动打开下载目录')
#
#
#
# class CrawlerScheduler_Douyin_debug(object):
#
#     def __init__(self, urls, config):
#         self.msg = self.genMsg()
#
#         self.config = config
#         self.numbers = []
#         self.challenges = []
#         self.musics = []
#         self.resolver = Resolver_Douyin(self.config)
#         #
#         #
#         # self.url_file_path = self.config.get_url_file_path()
#         # self.config.load_url_info(self.url_file_path)
#
#         print("in douyin_video, debug in here")
#         for i in range(len(urls)):
#             print(urls[i])
#
#
#     def genMsg(self):
#         return ('ErrorMessage: ' + '打开失败' + '无法打开，请手动打开下载目录')
