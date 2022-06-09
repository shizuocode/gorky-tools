# Gorky Tools
----
![Gorky Tools](https://user-images.githubusercontent.com/107080348/172741325-7cac9b49-9552-402c-b4f0-4cf7692fddbc.jpg)
Gorky Tools is a simple google search result grabber using google dork. With Gorky Tools you can use google dork lists to search faster dan automatically grab website in google search result. This tools will automatically grab website in the next pages. The maximum page is page number 10.

Installation
----
You can download this tools as zip and exctact the file, or you can instanly download using this command:
```
  git clone https://github.com/shizuocode/gorky-tools/
```
This tools requires BeautifulSoup4 Modules, install bs4 module using this command:
```
  pip install beautifulsoup4
```

Usage
----
Before you start using this tools, make sure to copy cookies from google search. Just randomly search in google.com and copy the cookies, easiest way to grab cookies is by paste this command in your address bar:
```
  javascript:document.cookie
```
After you grab the cookies copy and paste it to the cookies.txt files. Don't forget to save your google dork lists file at the same directory as Gorky Tools.
Finally you can start this tools by the basic command in python: ```python main.py``` and input your google dork lists filename.

Blank and reCAPTCHA
----
This tools can detect google recaptcha and sometimes you may face blank process. To fix it, redo the copy and past cookies step and save it to cookies.txt file. You can do this step without closing the main.py program.
