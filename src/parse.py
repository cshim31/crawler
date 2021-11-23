import pandas as pd 
import json

#  append output parsed data to source
# :param list of Course object
# :param course term
def writeCSV(elemList, term):
    df = pd.DataFrame([elem.__dict__ for elem in elemList])
    df.to_csv('./data/' + term + '.csv', sep=',', index=False, encoding='utf-8')
    return

#  append output parsed data to source
# :param list of Course object
# :param course term
def writeJson(elemList, term):
    
    f = open('./data/'+term+'.json','w', encoding='UTF-8')
    
    data = {"seat": []}

    data["seat"].extend([elem.__dict__ for elem in elemList])

    
    parsed = json.dumps(data, separators=(',', ":"))
    f.write(parsed)
    f.close()
    return

def removeSpaces(Str):
    return ' '.join(Str.split())
