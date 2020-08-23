import subprocess
import os
from IPython import embed
import argparse
parser = argparse.ArgumentParser(description='get info')
parser.add_argument('-d', type=str, help='music directory')
parser.add_argument('-l', type=str, help='youtube playlist link')
args = parser.parse_args()
playlistLink = 'https://www.youtube.com/playlist?list=PLEAzH5sDwKT1rV-UMfIGCrhp-PjNlAycj' if args.l is None else args.l
directory = '../' if args.d is None else args.d
folderName = 'youtubeMusic/'
folder = directory+folderName
if not os.path.exists(folder):
    os.makedirs(folder)
cmd = 'youtube-dl --download-archive downloaded.txt --no-post-overwrites -ciwx --audio-format mp3 -o "%(title)s.%(ext)s" {}'.format(playlistLink)
cmd = cmd.split()
cmd[cmd.index('--download-archive')+1] = folder + cmd[cmd.index('--download-archive')+1] 
cmd[cmd.index('-o')+1] = folder + cmd[cmd.index('-o')+1] 
subprocess.run(cmd)