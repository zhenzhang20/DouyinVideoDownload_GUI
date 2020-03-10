

import subprocess, ffmpeg, uuid, os

def generate_cmd_insertimg2video(input_video_file, imput_image_file, out_video_file):
    v_time_by_second = float(ffmpeg.probe(input_video_file)['format']['duration'])
    enable_flag = "\'if(gt(t,%f),lt(t,%f))\'" % (v_time_by_second, v_time_by_second+1)
    cmd = 'ffmpeg -i %s -i %s -filter_complex "overlay=x=0:y=0:enable=%s" -y %s' % (input_video_file, imput_image_file, enable_flag, out_video_file)
    return cmd

def generate_cmd_img2video(imput_image_file, out_video_file):
    v_time_by_second = "00:00:03"
    cmd = 'ffmpeg -y -f image2 -loop 1 -t %s -i %s %s' % (v_time_by_second, imput_image_file, out_video_file)
    return cmd

def generate_cmd_merge_videos(out_video_file, *input_video_file):
    tempfilename = uuid.uuid4().hex + ".txt"
    with open(tempfilename, 'w') as f:
        for line in input_video_file:
            f.write('file ' + line + '\n')
    cmd = 'ffmpeg -y -f concat -i %s -c copy %s' % (tempfilename, out_video_file)
    return cmd, tempfilename


def run_ffmpeg_cmd(cmd):
    try:
        res = subprocess.call(cmd, shell=True)
        if res != 0:
            return False
        return True

    except Exception:
        return False

if __name__ == "__main__":
    # 输入视频
    input_file = "test.mp4"

    # 输出视频
    out_file = "test_out.mp4"

    # 添加的图片
    img = "demo1.jpg"

    img2video = "demo1.mp4"

    # cmd = generate_cmd_img2video(img, img2video)
    #
    # res = run_ffmpeg_cmd(cmd)
    #
    # cmd, tempfilename = generate_cmd_merge_videos(out_file, input_file, img2video )
    #
    # res = run_ffmpeg_cmd(cmd)
    # if os.path.isfile(tempfilename) :
    #     os.remove(tempfilename)
