# GT Crawler

<p> Georgia Tech course information crawler using Python </p>

### Description

<a href="https://www.telerik.com/download/fiddler-everywhere"> Fiddler Everywhere </a> is used for analyzing packet sent to Georgia Tech web server.
<p> Data is saved in form of ".csv" extension but feel free to edit the extension and change it on your own. </p>

## Getting Started
### Building and installing
#### Prereqs:
- A Python compiler (Python 3.9.5+)
- A Package management system (pip 20.0.2+)

<p> Clone the repository</p>
    
    git clone https://github.com/GT-Time/crawler.git
    
<p> Install requirements and build project </p>

    pip install -r requirements.txt
    
    
<p> Navigate to repository and run </p>    

    python crawler.py

## Configuration
<p> Navigate to config.py and change setting. </p>

[![config.py](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/cshim31/crawler/blob/master/src/constant/config.py)

### SEMESTER

<p> Navigate to config.py and change "SEMESTER" value. </p>
<p> Value represents number of recent semester to crawl course data. </p>

### TIMEOUT

<p> Navigate to config.py and change "TIMEOUT" value. </p>
<p> Value represents threads timeout in second</p>

### THREAD_COUNT

<p> Navigate to config.py and change "THREAD_COUNT" value. </p>
<p> Value represents number of thread to be generated for crawling course data for each semester</p>

<strong> Overall, SEMESTER X THREAD_COUNT + SEMESTER is the total number of thread generated </strong>


## Output

<p> Fetched data will be parsed and saved in "data" branch with following file name structure </p>
<div style="text-align: right; margin-right: 10%;"> &lt;semesterID&gt;.&lt;fileExtension&gt; </div>

&nbsp;
<p> Supported files extensions: </p>

- JSON (.json)
- Excel (.csv)
