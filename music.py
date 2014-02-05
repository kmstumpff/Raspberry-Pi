import os
import eyeD3

go_on = 1

while go_on == 1:

    os.system('clear')

    filename = raw_input('Enter path to mp3 file: ')

    audiofile = eyeD3.Mp3AudioFile(filename)
    tag = audiofile.getTag()
    tag.link(filename)
    print ("\nTitle:  " + tag.getTitle())
    print ("Artist: " + tag.getArtist())
    print ("Album:  " + tag.getAlbum())
    length = audiofile.getPlayTimeString()
    print ("Length: " + length)
    cmd = "mpg321 -q " + filename
    os.system(cmd)
    
    go_on_string = raw_input('Would you like to play another song? (y/n): ')
    if go_on_string == "y":
        go_on = 1
    else:
        print "quitting..."
        break
