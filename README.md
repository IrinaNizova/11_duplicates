# Anti-Duplicator
Script that takes an input folder, looks through all the files in it (and all subfolders and sub-folders ...)
and reports if it finds duplicates.

# How to run
```python
python duplicates.py [folder]
```
Example:
```python
python3 duplicates.py /var/log
```

# Example of output
```
This files have duplicates:
test/my/java_error_in_PYCHARM_2742.log
test/my/less/java_error_in_PYCHARM_2742.log
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
