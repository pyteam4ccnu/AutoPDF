# AutoPDF

## Project Information

AutoPDF is a Automatic Python Documents Downloader. Based on [Python 官网](https://docs.python.org/zh-cn/3/tutorial/index.html). AutoPDF means to make a All Documents Downloader for each Website like BeautifulSoup or Flask, but now we can just download and make PythonBook fluently.

## Developer Information

This is a group work, we have 4 developers: **Song Ruyang(@ShiinaOrez)**, **Wang Pengyu(@messi-wpy)**, **Huang Zhiying(@liususususus)** and **Shen Yixin(@shenyixin)**.

And the work for each one:

| Name | The Part of Work |
|------|------------------|
| @ShiinaOrez | Main architectural design, Debug, and the Document Tree Coding Block. |
| @messi-wpy | The View Coding Block. |
| @liususususus | The Network Request Coding Block. |
| @shenyixin | The PDFs Merger Coding Block. |

## Dev Env & Test Env

### Dev Env

The **Dev Env** is `Windows 10 & Python3.7` and `Linux Ubuntu 18.04 & Python 3.7`.

### Test Env

The **Test Env** is `Linux Ubuntu 18.04 & Python 3.7`

## The Architecture & Technology Stack

### The Architecture

```
├── app                      // The app dir means to analyze the doc tree of page and download the PDFs.
│   ├── chromedriver
│   ├── decorator
│   │   └── timer.py
│   ├── doc_tree.py          // The script of doc tree.
│   ├── download.py          // The script of download.
│   ├── driver
│   │   └── __init__.py
│   ├── __init__.py
│   └── _internal.py
├── download                 // The download PDFs will be saved at here.
├── mergePDF                 // The script of merge PDFs.
│   ├── __init__.py
│   └── merge.py         
├── README.md
├── run.py
├── start.sh                 // The script to run this application.
└── view                     // The script of view.
    ├── form.py
    └── __init__.py

```

### The Technology Stack

+ PyQt5
+ PyPDF2
+ BeautifulSoup
+ requests

## Env

+ PATH
+ AutoPDF_PDFdir
+ AutoPDF_NewPDFname
+ AutoBaseUrl
+ AutoPDF_Base

## Quick Start

If you already have a right and safe running environment, you can just open your terminal and input next line:

> ```sh start.sh```

And then please enjoy it.

## Status:

[2019/5/5] Base function Over.

[2019/6/9] Add new view.

[2019/6/9] Fixed the logic of View.

## License

```
AutoPDF is a Automatic Python Documents Downloader.
Copyright (C) 2019 ShiinaOrez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```