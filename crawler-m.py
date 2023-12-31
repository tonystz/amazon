import settings
settings.VERBOSE=True
from crawler import Crawler
import attributes




if __name__ == '__main__':
    
    crawler = Crawler('https://www.amazon.com/CA9482-Extra-Guard-Flexible-Filter/dp/B000A0CANA')
    
    #print(crawler.browser.requestAttribute(attributes.getSelections(year=2007,makeId=68,modelId=885,submodelId=20)))
    # for year in [2017]:
    #     for makeId in [13,76]:
    #         for modelId in [21598]:
    #             for submodelId in [13,268,5702,20,282]:
    #                 crawler.getMoreAttrViaSubmodelId(year=year,makeId=makeId,modelId=modelId,submodelId=submodelId)
    for row in crawler.db.repeatUpdate():
        crawler.db.repeatDelete(row['rowid'])
        crawler.getMoreAttrViaSubmodelId(year=row['year'],makeId=row['makeId'],modelId=row['modelId'],submodelId=row['submodelId'])

