# PyHotKey

### Install
```
git clone https://github.com/marcelTau/PyHotKey.git && cd PyHotKey

pip3 install virtualenv
virtualenv .
source bin/activate
sudo pip3 install -r requirements.txt
```

### Run
```
sudo python3 main.py --help
```

### Config file
```
Default path: ~/shortcut.cfg

Pattern:
key=replacement
```
It is important, that the file follows this pattern. Multiline replacements are currently not supported.

