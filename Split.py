import pydub
import sys

#command line args contain any number of txt files, each for an album
#lines in text file are in order: mp3filename, artist, album, year, tracks(ordered)
#starttime 12:21 trackname
files = sys.argv[1:]
print(files)
def split(txt):
    mp3filepath = "/home/alannair/Music/" + txt[0]
    musicfile = pydub.AudioSegment.from_mp3(mp3filepath)
    artist = txt[1]
    album = txt[2]
    year = txt[3]

    tracks = txt[4:]
    no_of_tracks = len(tracks)
    tracknumber = no_of_tracks

    for song in reversed(tracks):
        songdata = song.split(' ')
        title = ' '.join(songdata[1:])
        starttime = 1000*(int((songdata[0].split(':'))[0])*60 + int((songdata[0].split(':'))[1]))
        meta = {'artist':artist, 'album':album, 'title':title, 'year':year, 'track':tracknumber}
        print("a\n")
        currtrack = musicfile[starttime:]
        musicfile = musicfile[:starttime]

        currtrack.export("/home/alannair/Music/"+title+".mp3", format="mp3", tags=meta)
        tracknumber -= 1

for txtfile in files:
    with open(txtfile,'r') as currfile:
        data = currfile.read().splitlines()
        print("a\n")
    split(data)
