from unittest import TestCase
from ..model.ffmpeg.ffmpeg_execute import ffmpegexecute
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


class Test(TestCase):
    def test_ffmpegexecute(self):
        filepath = str(BASE_DIR) + '/resources_test/video_test/testvideo.mp4'
        print(filepath)
        current = ffmpegexecute(filepath)
        expected = f'ffmpeg -i "{filepath}"  -r 1/1  "images/%04d.jpg"'
        self.assertEqual(current, expected)
