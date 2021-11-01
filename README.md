Raphaël Doursenaud Experiences
==============================

[My blog](https://raphael.doursenaud.fr) sources.


Usage
-----

Install Pelican and required modules in a virtualenv:
```
virtualenv venv
venv/Scripts/activate
python -m pip install -r requirements.txt
```

Clone in the directory directly above here:
- [ ] https://github.com/getpelican/pelican-plugins
- [ ] https://github.com/rdoursenaud/materialistic-pelican
- [ ] https://github.com/rdoursenaud/pelican-materialize

### Serve & debug
```
pelican --settings pelicanconf.py --listen --autoreload
```

### Generate
```
pelican --settings pelicanconf.py
```
