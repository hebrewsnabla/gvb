gvb module for PySCF
=========================

2022-01-09

* Version 0.1

Install
-------
* Install to python site-packages folder
```
pip install git+https://github.com/hebrewsnabla/gvb
```

* Install in a custom folder for development
```
git clone https://github.com/hebrewsnabla/gvb /home/abc/local/path

# Set pyscf extended module path
echo 'export PYSCF_EXT_PATH=/home/abc/local/path:$PYSCF_EXT_PATH' >> ~/.bashrc
```

You can find more details of extended modules in the document
[extension modules](http://pyscf.org/pyscf/install.html#extension-modules)
