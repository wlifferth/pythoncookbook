# Problem: You want to process data iteratively in the style of a data processing pipeline (similar to Unix pipes). For instancce, you have a huge amount of data that needs to be processed, but it can't fit entirely into memory.

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    for path, distlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


