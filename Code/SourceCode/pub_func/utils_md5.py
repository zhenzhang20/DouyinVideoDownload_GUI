import subprocess, ffmpeg, uuid

def generate_cmd_insertimg2video(out_video_file, input_video_file, imput_image_file):
    v_time_by_second = float(ffmpeg.probe(input_video_file)['format']['duration'])
    enable_flag = "\'if(gt(t,%f),lt(t,%f))\'" % (v_time_by_second, v_time_by_second+1)
    cmd = 'ffmpeg -i %s -i %s -filter_complex "overlay=x=0:y=0:enable=%s" -y %s' % (input_video_file, imput_image_file, enable_flag, out_video_file)
    return cmd

def generate_cmd_img2video(out_video_file, imput_image_file):
    v_time_by_second = "00:00:05"
    cmd = 'ffmpeg -y -f image2 -loop 1 -t %s -i %s %s' % (v_time_by_second, imput_image_file, out_video_file)
    return cmd

# ffmpeg -f concat -i <path_to_text_file> ...
# The path_to_text_file must use forward slashes, not backslashes, even in Windows. This rule doesn't seem to apply for the video file paths on the command line though -- only for the text file path on the command line.
# The paths listed within your text file are interpreted by ffmpeg as being relative to the location of your text file. (In particular, the paths listed are not relative to the current working directory.)
# add "-safe 0 " to solve  "Operation not permitted" issue
def generate_cmd_merge_videos(out_video_file, *input_video_file):
    tempfilename = uuid.uuid4().hex + ".txt"
    with open(tempfilename, 'w', encoding='UTF-8') as f:
        for line in input_video_file:
            f.write('file ' + line + '\n')
    cmd = 'ffmpeg -y -f concat -safe 0  -i %s -c copy %s' % (tempfilename, out_video_file)
    return cmd, tempfilename

import shutil
def changemd5_by_append_uuid4(out_video_file, input_video_file):
    uuidstr = uuid.uuid4().hex
    shutil.copy2(input_video_file, out_video_file)
    video_file = open(out_video_file, 'a')
    video_file.write(uuidstr)
    video_file.close()

def run_ffmpeg_cmd(cmd):
    try:
        res = subprocess.call(cmd, shell=True)
        if res != 0:
            return False
        return True

    except Exception:
        return False

# import platform
# def debug05():
#
#     file_path = 'D:\\zz\\study\\py_prj\\VideoDownload_GUI-douyin\\gui\\src\\download\\96038051045\\v0200f0e0000bk7kspceae1ftkts8rd0-我只看花，不敢看你。我怕我看着你，一切心事不能掩饰。.mp4'
#     if (platform.system() == 'Windows'):
#         file_path = file_path.replace("\\", "/")
#     mergevideo = 'D:/zz/study/py_prj/VideoDownload_GUI-douyin/gui/src/Resource/def_tailervideo.mp4'
#
#     cmd, tempfilename = generate_cmd_merge_videos("out.mp4", file_path, mergevideo)
#     print(cmd)
#     res = run_ffmpeg_cmd(cmd)




#
# if __name__ == "__main__":
#     # 输入视频
#     input_file = "test.mp4"
#
#     # 输出视频
#     out_file = "test_out.mp4"
#
#     # 添加的图片
#     img = "tailerpicture.jpg"
#     # img = "demo1.jpg"
#
#     img2video = "tailerpicture.mp4"
#
#     cmd = generate_cmd_img2video(img2video, img)
#     #
#     res = run_ffmpeg_cmd(cmd)
#     #
#     # cmd, tempfilename = generate_cmd_merge_videos(out_file, input_file, img2video )
#     #
#     # res = run_ffmpeg_cmd(cmd)
#     # if os.path.isfile(tempfilename) :
#     #     os.remove(tempfilename)
#     # debug05()