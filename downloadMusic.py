import subprocess
import os
from IPython import embed
playlistLink = 'https://www.youtube.com/playlist?list=PLEAzH5sDwKT1rV-UMfIGCrhp-PjNlAycj'
directory = '/Users/atillasaadat/Music/iTunes/iTunes Media/Music/'
folderName = 'youtube/'
folder = directory+folderName
if not os.path.exists(folder):
    os.makedirs(folder)
cmd = 'youtube-dl --embed-thumbnail --download-archive downloaded.txt --no-post-overwrites -ciwx --audio-format mp3 -o "%(title)s.%(ext)s" {}'.format(playlistLink)
cmd = cmd.split()
cmd[cmd.index('--download-archive')+1] = folder + cmd[cmd.index('--download-archive')+1] 
cmd[cmd.index('-o')+1] = folder + cmd[cmd.index('-o')+1] 
subprocess.run(cmd)