
import json
from bs4 import BeautifulSoup
from logger import logger

CouldMoreThen_BE='bodyStyle-engine'
def parserActive(body,couldMoreThen=False):
    '''
    first, next,next
    '''
    bsparser= BeautifulSoup(body,'lxml')
    r=[]
    selections = None
    idskey = None
    ids = []
    for select in bsparser.find_all('select'):
        r.append([
            (str(el.get('value')).strip(),str(el.getText()).strip()) 
            for el in select.find_all('option')
            ])
    if bsparser.select_one('div[data-selections-json]') and bsparser.select_one('div[data-active-attribute-ids-json]'):
        selections = json.loads(bsparser.select_one('div[data-selections-json]').get('data-selections-json'))
        _idskey= json.loads(bsparser.select_one('div[data-selections-json]').get('data-active-attribute-ids-json'))
        if len(_idskey) == 1:
            idskey = _idskey[0]
        elif len(_idskey) == 0:
            pass
        else:
            if couldMoreThen:
                if '-'.join(_idskey) == CouldMoreThen_BE:
                    logger.info(f'find bodyStyle, and engine {_idskey} and r=:{r}')
                    bodyStyle=[i for i in r[0] if len(i[0]) != 0 ]
                    engine=[i for i in r[1] if len(i[0]) != 0 ]
                    for e in engine:
                        for b in bodyStyle:
                            ids.append((e[0],e[1],b[0],b[1]))
                return ids,CouldMoreThen_BE,selections
            logger.error(f'more than one idskey {_idskey}')
    logger.debug(f'attribute: {r}')

    if len(r) !=0 :
        ids = [i for i in r[0] if len(i[0]) != 0 ]
    logger.info(f'attribute ids: {ids}')
    logger.info(f'attribute idskey: {idskey}')
    logger.info(f'attribute selections: {selections}')
    
    return ids, idskey, selections

def getSelections(year=None,makeId=None,modelId=None,submodelId=None,engine=None,bodyStyle=None):
    s = [
        {"id":"version","value":"1"},
        {"id":"flow","value":"vehicle-by-attributes"},
        {"id":"vehicleType","value":"automotive"},
    ]
    if year:
        s.append({"id": "year", "value": year})
        if makeId:
            s.append({"id": "makeId", "value": makeId})
            if modelId:
                s.append({"id": "modelId", "value": modelId})
                if submodelId and submodelId !=0 :
                    s.append({"id": "submodelId", "value": submodelId})
                    if engine and engine !=0 :
                        s.append({"id": "engine", "value": engine})
                    if bodyStyle and bodyStyle !=0 :
                        s.append({"id": "bodyStyle", "value": bodyStyle})
    return s