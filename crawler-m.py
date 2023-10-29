import settings
settings.VERBOSE=True
from crawler import Crawler
import attributes




if __name__ == '__main__':
    
    crawler = Crawler('https://www.amazon.com/Richeer-Hubcentric-ChevyTahoe-Avalanche-6x139-7mm/dp/B07XF3J1QZ')
    
    #print(crawler.browser.requestAttribute(attributes.getSelections(year=2007,makeId=68,modelId=885,submodelId=20)))
    crawler.getMoreAttrViaSubmodelId(year=1995,makeId=47,modelId=499,submodelId=96)