import request
import inputs
import attributes
from db import DataBase
import json

class Crawler():
    def __init__(self,product_url) -> None:
        self.browser = request.AmazonVehicleParts(product_url)
        self.browser.requestTokenFromHome().requestFirstSelect()
        self.db = DataBase()
        self.db.test()

    def updateFit(self,i):
        self.browser.logger.info(f'check fit: parts={json.dumps(i)}')
        fit,note=self.browser.requestPartfinder(attributes.getSelections(
            year=i['year'],makeId=i['makeId'],
            modelId=i['modelId'],submodelId=i['submodelId'],
            engine=i['engine'],bodyStyle=i['bodyStyle']))
        self.db.updateFit(fit,note,i['rowid'])
    
    def getYear(self):
        return self.browser.requestAttribute(attributes.getSelections())
    
    def getMakeIdMaxYear(self):
        return self.db.getMakeIdMaxYear(self.browser.asin)[0].get('maxyear')
        
    def getMakeId(self,year='2003'):
        self.browser.logger.info(f'get makeId via year=: {year}')
        ids = [ i['makeId'] for i in self.db.getMakeId(self.browser.asin,year=year) if i['makeId']]
        if len(ids) != 0:
            return ids
        ids, idskey, _ = self.browser.requestAttribute(attributes.getSelections(year=year))
        assert idskey == 'makeId'
        self.db.insertMakeId(self.browser.asin,year,ids,self.browser.product_url)
        return [i[0] for i in ids]
    
    def getModelId(self,year='2003',makeId=73):
        self.browser.logger.info(f'get modelId via makeId= {makeId}')
        ids = [i['modelId'] for i in self.db.getModelId(self.browser.asin,year,makeId) if i['modelId']]
        if len(ids) !=0:
            return ids
        ids, idskey, _ = self.browser.requestAttribute(attributes.getSelections(year=year,makeId=makeId))
        assert idskey == 'modelId'
        self.db.insertUpdateModelId(self.browser.asin,year,makeId,ids)
        return [i[0] for i in ids]
    
    def getSubmodelId(self,year='2003',makeId=73,modelId=986):
        self.browser.logger.info(f'get submodelId via modelId=: {modelId}')
        ids = [ i['submodelId'] for i in self.db.getSubmodelId(self.browser.asin,year,makeId,modelId) if i['submodelId'] is not None ]
        if len(ids) !=0:
            return ids
        ids = self.browser.requestAttribute(attributes.getSelections(year=year,makeId=makeId,modelId=modelId))[0]
        ids = [(0,None)] if len(ids) == 0 else ids
        self.db.insertUpdateSubmodelId(self.browser.asin,year,makeId,modelId,ids)

        return [i[0] for i in ids]
    
    def getMoreAttrViaSubmodelId(self,year,makeId,modelId,submodelId):
       # engine or bodyStyle or end
        self.browser.logger.info(f'update more attr via submodelId=: {submodelId}')
        _submodelId=[ 
            i['submodelId']
            for i in self.db.getMoreAttrViaSubmodelId(self.browser.asin,year,makeId,modelId,submodelId)
            if i['engine'] is None or i['bodyStyle'] is None
        ]
        if len(_submodelId) == 0 or _submodelId[0] ==0:
            return
        ids, idskey, _ = self.browser.requestAttribute(attributes.getSelections(year,makeId,modelId,submodelId),couldMoreThen=True)
        if idskey is None:
            ids = [(0,0,0,0)]
        elif idskey == 'engine':
            '''2016/Land Rover/Range Rover/Base/3.0L V6 Diesel
            https://www.amazon.com/Puroma-Filter-Activated-Replacement-CF10285/dp/B07VHMX2NT
            '''
            ids = [(engine[0],engine[1],0,0) for engine in ids]
        elif idskey == 'bodyStyle':
            '''2009/Honda/Accord/EX/4 Door Sedan
            https://www.amazon.com/SEALIGHT-360-degree-Illumination-Brightness-Installation/dp/B07Q24LVDM
            '''
            ids = [(0,0,bodyStyle[0],bodyStyle[1]) for bodyStyle in ids]
        elif idskey == attributes.CouldMoreThen_BE:
            '''2007/INFINITI/G35/Base/<bodyStyle>/<engine>
            https://www.amazon.com/CA4309-Extra-Flexible-Rectangular-Filter/dp/B0009H51MG
            '''
            pass
        else:
            self.browser.logger.error(f'[TODO]unspported type: {idskey} --> {ids}')
            return
        self.db.insertUpdateMoreAttr(self.browser.asin,year,makeId,modelId,submodelId,ids)


if __name__ == '__main__':
    
    crawler = Crawler(inputs.product_url)
    min_year = crawler.getMakeIdMaxYear() if crawler.getMakeIdMaxYear() else min(inputs.year)
    for year in range(min_year,max(inputs.year)+1):
        for makeId in crawler.getMakeId(year):
            for modelId in crawler.getModelId(year,makeId=makeId):
                for submodelId in crawler.getSubmodelId(year,makeId=makeId,modelId=modelId):
                    crawler.getMoreAttrViaSubmodelId(year,makeId,modelId,submodelId)