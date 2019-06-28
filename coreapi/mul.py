""" to  segment video ffmpeg -loglevel panic -i "/Users/amit/Desktop/Give.mp4"  -c copy -map 0 -segment_time 5 -reset_timestamps 1 -f segment -segment_list_type csv -segment_list '/Users/amit/Desktop/test/seg/seg.csv' '/Users/amit/Desktop/test/seg/%d.mp4' """

"""to extract frames   ffmpeg -i "/Users/amit/Desktop/Give.mp4"  "/Users/amit/Desktop/test/seg/img/%d.jpg" """

import os
import subprocess as sp
import concurrent.futures
import shlex
import logging
import glob
from PIL import Image
from .tasks import testmulti

def segment():
	command = "ffmpeg -loglevel panic -i '/Users/amit/Downloads/Elon Musk Smokes Weed  - Joe Rogan Podcast.mp4'  -c copy -map 0 -segment_time 5 -reset_timestamps 1 -f segment -segment_list_type csv -segment_list '/Users/amit/Desktop/multi/seg/seg.csv' '/Users/amit/Desktop/multi/seg/vid/%d.mp4'"
	logging.info(command)
	segmentor = sp.Popen(shlex.split(command))
	segmentor.wait()
	if segmentor.returncode != 0:
		raise ValueError
	print("Done Segmenting")

def getfileinfo(file):

	command = 'ffprobe -show_streams -i {}  '.format(file)
	segment_json = sp.check_output(shlex.split(command))
	return segment_json

def propara():
	with concurrent.futures.ProcessPoolExecutor() as executor:
		video_files = glob.glob("/Users/amit/Desktop/multi/seg/vid/*.mp4")
		result = executor.map(testmulti.delay, video_files)

		for res in result:
			print(res)


# if __name__ == "__main__":
segment()
propara()

