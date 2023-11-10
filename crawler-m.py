import settings
settings.VERBOSE=True
from crawler import Crawler
import attributes




if __name__ == '__main__':
    
    crawler = Crawler('https://www.amazon.com/Richeer-Hubcentric-ChevyTahoe-Avalanche-6x139-7mm/dp/B07XF3J1QZ')
    
    #print(crawler.browser.requestAttribute(attributes.getSelections(year=2007,makeId=68,modelId=885,submodelId=20)))
    for year in [2005,2012,2017,2014]:
        for makeId in [47]:
            for modelId in [491]:
                for submodelId in [430,478,523,444]:
                    crawler.getMoreAttrViaSubmodelId(year=year,makeId=makeId,modelId=modelId,submodelId=submodelId)

