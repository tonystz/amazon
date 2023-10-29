import settings
settings.VERBOSE=True
from crawler import Crawler
import attributes




if __name__ == '__main__':
    
    crawler = Crawler('https://www.amazon.com/Richeer-Hubcentric-ChevyTahoe-Avalanche-6x139-7mm/dp/B07XF3J1QZ')
    
    #print(crawler.browser.requestAttribute(attributes.getSelections(year=2007,makeId=68,modelId=885,submodelId=20)))
    for year in [1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,
                 2010,2011,2012,2013,2013,2015,2016,2017,2018]:
        for makeId in [47]:
            for modelId in [491,499]:
                for submodelId in [20,96,125,430,434,444,478,523,912,3584,11005]:
                    crawler.getMoreAttrViaSubmodelId(year=year,makeId=makeId,modelId=modelId,submodelId=submodelId)

