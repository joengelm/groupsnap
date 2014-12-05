from snapchat import *
import argparse
from time import sleep
import getpass, os, sys
import logging

username = ""
path = ""

def run(password, init_post_count):
	post_count = init_post_count
	s = Snapchat()
	s.login(username, password)
	if not s.logged_in:
		print "Invalid login credentials"
		return
	logging.basicConfig(filename='../gs.log', level=logging.DEBUG, format='%(asctime)s - ' + username + ': %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	logging.info("initializing")
	while True:
		logging.info("fetching snaps")
		snaps = s.get_snaps()
		for snap in snaps:
			logging.info("downloaded snap")
			download(s, snap)
		logging.info("clearing feed")
		s.clear_feed()
		for filename in os.listdir(path):
			logging.info("processing snap " + str(post_count))
			media_type = 0
			extension = filename.split('.')[-1]
			if extension == "mp4":
				media_type = s.MEDIA_VIDEO
			elif extension == "jpg" or extension == "jpeg":
				media_type = s.MEDIA_IMAGE
			else:
				continue
			logging.info("uploading snap " + str(post_count) + " as a " + extension)
			media_id = s.upload(media_type, path + filename)
			time = 10
			try:
				time = int(filename.split('+')[0])
			except ValueError:
				time = 10
			logging.info("adding snap " + str(post_count) + " to story")
			s.add_story(media_id, media_type, "Post #" + str(post_count), time)
			logging.info("removing snap " + str(post_count) + " from directory")
			os.remove(path + filename)
			post_count += 1
		logging.info("sleeping")
		sleep(300)
		logging.info("logging in")
		s.login(username, password)
		logging.info("logged in")
	
def download(s, snap):
    """Download a specific snap"""

    snap_id = snap['id']
    name = snap['sender']
    time = str(snap['time'])

    result = s.get_media(snap_id)

    if not result:
        return False

    ext = s.is_media(result)
    filename = '{}+{}.{}'.format(time, snap_id, ext)
    full_path = path + filename
    with open(full_path, 'wb') as fout:
        fout.write(result)
    return True

if __name__ == '__main__':
        print("GroupSnap Running")
        parser = argparse.ArgumentParser()
        parser.add_argument("-l")
        args = parser.parse_args()
        if args.l is not None and os.path.exists(args.l):
            creds = open(args.l)
            username = creds.readline().strip()
            password = creds.readline().strip()
        else:
            username = raw_input("Username: ")
            password = getpass.getpass('Password: ')
	path = "../" + username + "/"
        if not os.path.exists(path):
            os.makedirs(path)
	post_count = 0
        # Allow reading credentials from a file.
	# if len(sys.argv) > 1:
	# 	try:
	# 		post_count = int(sys.argv[1])
	# 	except ValueError:
	# 		post_count = 1
	run(password, post_count)
