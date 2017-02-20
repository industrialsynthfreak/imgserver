# D.O.G. image server

 A simple remote camera server. Client can connect to a remote camera
 and take a snapshot.
 
## Usage
 
 It's pretty simple. You connect to it from your browser and press "get 
 snapshot" button. You will be redirected to a page with a new photo on it, 
 and photo's id will be stored in your cookies in case you'll come back.
 
## Deployment
 
 Tested in python 2.7. Should work in python 3 as well (haven't tested it).
 First install all of the requirements either with pip or manually. The only
 actual dependency is `bottlepy` module.
 
    pip install -r pip_requirements.txt
    
 You will need a terminal-based image capturing app which can receive a file
 path argument. I've used `imagesnap` for this on OS X. Install it with 
 homebrew or any other package manager.
  
 Check `camera_access.sh` and add your image capturing app to it. The only 
 argument that is shipped to the script is a filepath to an image to be 
 created.
  
 Ensure that `server.py` and `camera_access.sh` are both `chmod +x` and you
 have permissions to write into the server dir and child directories.
   
 You may want to check server config in `config.py` for such vars as 
 host/port, secret key, camera "dead time", etc.
   
 Finally, run the server:
 
    server.py
 
 All should work now. Default log record will be stored in `server.log`. If 
 you want you can run unit tests: `python2 tests.py` (they require the 
 server to be running).
 
## Problems
 
 The execution of the script is pretty secure. A client obviously 
 doesn't have access to it, because it's not served in any way, plus in most 
 cases one won't need to exec it with su or sudo, and if you do then something 
 is wrong with you! However, cookies protection is pretty lame. File names are 
 7 letter randomly generated strings and, considering that no additional name 
 checks being performed, they may be automatically overwritten eventually.
 