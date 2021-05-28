# GT Crawler

GT crawler is an application for crawling course information in Georgia Tech. </p>

## Description

Following app used "Fiddler Everywhere" application and tracked how the variables are named and sent to Georgia Tech web server.\
Crawled data is saved in form of ".csv" extension, but if error occurs, feel free to edit the extension and change it on your own.\
Refer to tools.py/writeToExcel function for more information. </p>


## Installation

clone the repository and use package manager pip to install libraries

```bash
git clone https://github.com/GT-Time/crawler.git
pip install beautifulsoup4
pip install regex
```

## Output

parsed data will be saved as "data/term.txt". User will need to manually convert it to csv file by using excel. </p>
* Open Microsoft Excel
* Go to Data -> From Text/CSV
* Navigate to parsed data text file
* Set delimiter as '|'
* Complete import
