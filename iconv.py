#!/usr/bin/env python3
import os
source = "zh_TW.po"
target = "zh_TW.UTF-8.po"
print("Started.")
os.system("iconv -f Big5 -t UTF-8 -o {target} {source}".format(source=source, target=target))
print("Done.")
exit()
