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

## Usage
<p> Navigate to constant.py and change setting. </p>

[![Constant.py](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/cshim31/crawler/blob/master/src/constant.py)

### Set number of semester 
<p> Navigate to constant.py and change SEMESTER value. </p>
<p> Value represents recent number of recent semester to crawl data. </p>

### Change Timeout and Delay 
<p> Navigate to constant.py and change TIMEOUT and DELAY value. </p>


## Output

parsed data will be saved as "data/term.txt". User will need to manually convert it to csv file by using excel. </p>
* Open Microsoft Excel
* Go to Data -> From Text/CSV
* Navigate to parsed data text file
* Set delimiter as '|'
* Complete import
