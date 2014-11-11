from snapchat import *
from time import sleep
import getpass
import os
import sys

username = ""
path = ""

def run(password, init_post_count):
	post_count = init_post_count
	s = Snapchat()
	s.login(username, password)
	if not s.logged_in:
		print "Invalid login credentials"
		return
	while True:
		snaps = s.get_snaps()
		for snap in snaps:
			download(s, snap)
		s.clear_feed()
		for filename in os.listdir(path):
			print "Processing: ", filename
			media_type = 0
			extension = filename.split('.')[-1]
			if extension == "mp4":
				media_type = s.MEDIA_VIDEO
			elif extension == "jpg" or extension == "jpeg":
				media_type = s.MEDIA_IMAGE
			else:
				continue
			media_id = s.upload(media_type, path + filename)
			time = 10
			try:
				time = int(filename.split('+')[0])
			except ValueError:
				time = 10
			s.add_story(media_id, media_type, "Post #" + str(post_count), time)
			os.remove(path + filename)
			post_count += 1
		sleep(300)
		s.login(username, password)
	
def download(s, snap):
    """Download a specific snap"""

    id = snap['id']
    name = snap['sender']
    time = str(snap['time'])

    result = s.get_media(id)

    if not result:
        return False

    ext = s.is_media(result)
    filename = '{}+{}+{}.{}'.format(time, name, id, ext)
    full_path = path + filename
    with open(full_path, 'wb') as fout:
        fout.write(result)
    return True

if __name__ == '__main__':
	username = raw_input("Username: ")
	path = "../" + username + "/"
	password = getpass.getpass('Password: ')
	post_count = 0
	if len(sys.argv) > 1:
		try:
			post_count = int(sys.argv[1])
		except ValueError:
			post_count = 1
	run(password, post_count)
