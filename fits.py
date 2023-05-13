from crawler import Crawler
from db import DataBase
import traceback

loop = True
db = DataBase()
while loop:
    loop = False
    cache={}
    for parts in db.getPartUnkown():
        url = parts['url']
        loop = True
        try:
            crawler = cache.get(url,None)
            if crawler is None:
                crawler = Crawler(url)
                cache[url] = crawler
            crawler.updateFit(parts)
        except Exception as e:
            cache[url]=None
            crawler.browser.logger.error(f'fail to {e}. {traceback.format_exc()}')
            crawler.browser.sleep(5)
            loop = True

# print(crawler.getMakeId(year=year))
# print(crawler.getModelId(year=year,makeId=45))