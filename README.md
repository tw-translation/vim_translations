# VIM 正體中文翻譯計畫
## 計畫概述
原本的 VIM 翻譯已年久失修且有部份糟糕翻譯，
藉翻譯 VIM 的機會來修正 VIM 的翻譯。

## 如何參與
- 發 Pull Request
- 發 Issues 表示想長期加入此翻譯計畫，直接加入此 Repo 的貢獻者之一。

## 翻譯原則
**翻譯時請翻譯 zh_TW.UTF-8.po 檔案，翻譯完後再使用 iconv.py 生成
zh_TW.po (Big5) 檔案！**

每次翻譯完之後，請輸入下述的指令，以保證 
zh_TW.UTF-8.po 的翻譯與 zh_TW.po 的翻譯相同。

```
$ python3 iconv.py
```

## 貢獻者
歡迎自行修改此 README.md，增加自己的名稱。

早期 vim 翻譯貢獻者：
- Hung-Te Lin <piaip@csie.ntu.edu.tw> (可追溯的第一個翻譯者).
- Cecil Sheng "<b7506022@csie.ntu.edu.tw>.

tw-translation/vim_translations 貢獻者名單： 
- pan93412 <pan93412@gmail.com>, 2018. 
