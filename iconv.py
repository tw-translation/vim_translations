#!/usr/bin/env python3
'''
@name       自動轉換編碼工具
@author     pan93412
@date       2018.07.30 3:08PM
@system     Linux / macOS (?) / Windows (cygwin) (?)
'''
import os, sys

# 檢查系統
if sys.platform == "win32":
    print("這個程式不支援 Windows 環境 QQ")
    print("請使用 cygwin (未知支援) 或是")
    print("Linux 唷！")
    exit(1)
else:
    pass # 除了 Win32 以外的系統都允許使用。

# 來源檔案設定
source = "zh_TW.UTF-8.po"
source_encoding = "UTF-8"

# 目標檔案設定
target = "zh_TW.po"
target_encoding = "Big5"

# 主程式
print("開始從 {0} ({1}) 產生 {2} ({3}) ……".format(source, source_encoding, target, target_encoding))
os.system("iconv -f {1} -t {3} -o {2} {0}".format(source, source_encoding, target, target_encoding))
os.system('sed -i \'s/charset={0}\\\\n/charset={1}\\\\n/g\' {2}'.format(source_encoding, target_encoding, target))
print("成功產生 {0}！".format(target))
exit()
