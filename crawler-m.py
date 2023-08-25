import settings
settings.VERBOSE=True
from crawler import Crawler
import attributes




if __name__ == '__main__':
    
    crawler = Crawler('https://www.amazon.com/CA4309-Extra-Flexible-Rectangular-Filter/dp/B0009H51MG')
    
    #print(crawler.browser.requestAttribute(attributes.getSelections(year=2007,makeId=68,modelId=885,submodelId=20)))
    crawler.getMoreAttrViaSubmodelId(year=2007,makeId=68,modelId=885,submodelId=20)