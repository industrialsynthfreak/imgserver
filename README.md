# D.O.G. image server

 A simple remote snapshot server. Client can connect to a remote camera
 and take a snapshot.
 
 ## Usage
 
 It's pretty simple. You connect with it from your browser and press "get 
 snapshot". You will be redirected to a page with a shot on it, and its name
  will be stored in your cookies in case you'll come back.
 
 ## Deployment
 
 Tested in python2.7. Should also work in python3.
 First install all requirements (the only one is bottle) either with pip or 
 manually.
 
    `pip install -r pip_requirements.txt`
    
 You will need a terminal-based image capturing app which can receive a save
  path argument. I've used `imagesnap` for this on OS X. Install it with 
  homebrew or manually.
  
  Check `camera_access.sh` and add your system type and your image capturing 
  app to it. The only argument that is passed to the script is a relative 
  filepath (you may make it absolute in `config.py`, I guess).
  
  Ensure that `server.py` and `camera_access.sh` are both `chmod +x` and you
   have rights to write into the server and its child directories.
   
 You may want to check server config in `config.py` for such vars as 
 host/port, secret key, etc.
   
 Finally, run the server:
 
    `server.py`
 
 All should work then. The default location is at `localhost:8080`. Default 
 log record is stored in `server.log`.
 
 ## Problems
 
 The execution of the script is pretty secure, because a client obviously 
 doesn't have access to it - it's not served in any way, plus in most cases 
 one won't need to exec it with su or sudo, and if you do then something 
 is wrong with you!
 
 However, cookies protection is pretty lame. You may want to patch that.
 
 File names are 7 letter randomly generated strings and may overlap 
 eventually.
 