# test url:
1. https://www.amazon.com/Headlight-SEALIGHT-Design-Upgraded-Warranty/dp/B07HCZ7RZ6
 - 2003 audi A4
1. https://www.amazon.com/Forenner-Headlight-Conversion-Installation-Replacement/dp/B096812T9V
1. output csv/fit or not
# install
```
pip3 install scrapy

scrapy runspider vehicle.py
```
# docs
https://www.jianshu.com/p/a44da11c9e79
https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html

```shell
pip3 install scrapy
pip3 install scrapyjs
pip3 install scrapy-splash
scrapy startproject car
scrapy genspider veh veh.com
#run
cd car
scrapy crawl veh
# try debug
scrapy shell https://www.amazon.com/Forenner-Headlight-Conversion-Installation-Replacement/dp/B096812T9V
```
# docs Scrapy-Splash solution
```shell
docker run -p 8050:8050 scrapinghub/splash --max-timeout 3600
```
1. https://www.cnblogs.com/Summer-skr--blog/articles/11477117.html
1. https://www.cnblogs.com/kongzhagen/articles/6549053.html
1. https://stackoverflow.com/questions/30345623/scraping-dynamic-content-using-python-scrapy
1. https://pypi.org/project/scrapyjs/
1. https://github.com/scrapy-plugins/scrapy-splash
1. jquery with splash: https://stackoverflow.com/questions/41614472/use-scrapy-splash-return-html


# Selenium solution with Firefox

1. wget  https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux32.tar.gz
1. https://github.com/sundowndev/PhoneInfoga/issues/84
1. https://selenium-python.readthedocs.io/installation.html#drivers
1. https://selenium-python.readthedocs.io/getting-started.html


# request solution
1. https://stackoverflow.com/questions/67311882/trouble-scraping-all-the-books-from-a-section-without-hardcoding-payload
1. https://beautiful-soup-4.readthedocs.io/en/latest/

```
pip3 install beautifulsoup4
pip3 install fake-useragent
#for windows
pip install lxml
```