from crawler import Crawler
from db import DataBase
import traceback

loop = True
db = DataBase()
while loop:
    loop = False
    for parts in db.getPartUnkown():
        loop = True
        try:
            crawler = Crawler(parts['url'])
            crawler.updateFit(parts)
        except Exception as e:
            crawler.browser.logger.error(f'fail to {e}. {traceback.format_exc()}')
            crawler.browser.sleep()

# print(crawler.getMakeId(year=year))
# print(crawler.getModelId(year=year,makeId=45))