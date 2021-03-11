import subprocess
import os
import argparse
from IPython import embed
parser = argparse.ArgumentParser(description='get info')
parser.add_argument('link', type=str, help='youtube playlist link')
parser.add_argument('-d', type=str, help='music directory')
args = parser.parse_args()
directory = '../' if args.d is None else args.d
folderName = 'youtubeMusic/'
folder = directory+folderName
if not os.path.exists(folder):
    os.makedirs(folder)
#cmd = 'youtube-dl --download-archive {0}downloaded.txt --no-post-overwrites -ciwx --audio-format mp3 -o {0}"%(title)s.%(ext)s" {1}'.format(folder,args.link)
cmd = 'youtube-dl --download-archive {0}downloaded.txt --add-metadata --xattrs --no-post-overwrites --audio-quality 0 --embed-thumbnail -ciwx --audio-format mp3 -o {0}"%(title)s.%(ext)s" {1}'.format(folder,args.link)
cmd = cmd.split()
subprocess.run(cmd)