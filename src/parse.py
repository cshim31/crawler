import pandas as pd 
import json

#  append output parsed data to source
# :param list of Course object
# :param course term
def writeCSV(courseList, term):
    df = pd.DataFrame([course.__dict__ for course in courseList])
    df.to_csv('./data/' + term + '.csv', sep=',', index=False, encoding='utf-8')
    return

#  append output parsed data to source
# :param list of Course object
# :param course term
def writeJson(courseList, term):
    
    f = open('./data/'+term+'.json','w', encoding='UTF-8')
    
    data = {"course": []}

    data["course"].extend([course.__dict__ for course in courseList])

    
    parsed = json.dumps(data, separators=(',', ":"))
    f.write(parsed)
    f.close()
    return

def removeSpaces(Str):
    return ' '.join(Str.split())
