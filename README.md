# D.O.G. image server

 A simple remote camera server. Client can connect to a remote camera
 and take a snapshot.
 
## Usage
 
 It's pretty simple. You connect to it from your browser and press "get 
 snapshot" button. You will be redirected to a page with a new photo on it, 
 and photo's id will be stored in your cookies in case you'll come back.
 
## Deployment
 
 Both server, client and tests are compatible with python 2 and python 3 now
  (tested in 2.7.13 and 3.6.0).
  
 First, install all of the requirements either by pip or manually. The only
 actual dependency is `bottlepy` module.
 
    pip install -r pip_requirements.txt
    
 You will need a terminal-based camera app which can receive a filepath 
 argument. I've used `imagesnap` for this purpose on OS X. Install it using 
 homebrew or any other package manager.
  
 Review `camera_access.sh` and add your app into it. The only argument passed
 to the script should be a filepath to an image to be created.
  
 Ensure that `server.py` and `camera_access.sh` are both `chmod +x` and you
 have permissions to write into the server + child directories.
   
 You may want to check server config in `config.py` for such vars as 
 host/port, secret key, camera "dead time", etc.
   
 Finally, run the server:
 
    server.py
 
 All should work now. Default log record will be stored in `server.log`. If 
 you want you can run unit tests executing: `python tests.py` (they require 
 your server to be running).
 
## Problems
 
 The execution of the script is pretty secure. A client obviously 
 doesn't have access to it, because it's not served in any way, plus in most 
 cases one won't need to exec it with su or sudo, and if you do, then 
 something is wrong with you! Also cookies protection is pretty lame.
 
 Though concurrent connections have been tested, I cannot guarantee high 
 load support.
 
 File names are 7 letter randomly generated strings and, considering that no 
 additional name checks being performed, they may become overwritten 
 eventually (in a couple of centuries).