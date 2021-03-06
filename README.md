GroupSnap (for Python!)
======================

This project is a variation of my original GroupSnap project in Java. In short, this program will allow you to create groups in Snapchat. Any snaps received by the GroupSnap account will be automatically reposted onto the account's story.

Prerequisites:
--------------
1. This program should preferably be run on an always-on computer. 
2. Use 'pip' to install the 'requests' module.
3. Also, install the 'pycrypto' module.

How to Set Up a GroupSnap Account:
----------------------------------
1. Create a new Snapchat account for your group with a memorable username.
2. Set the permissions for this 'group' account to 'Everyone', or manually add the friends you want in your group.
3. Run groupsnap.py and enter the username and password for your group.

Usage for 'groupsnap.py':
-------------------------
python groupsnap.py [initial post count]
If you'd like, you can include the optional, integer "initial post count" argument. This will initialize the post counter to a number other than zero (which is the default). For new groups, this argument should be excluded, but if you are restarting a previously run groupsnap account, then you may want to begin the post counter at a higher number.

Credits:
--------
Much of the library code is the work of 'niothiel'. All other code is my own, and inspired by my earlier Java project.
