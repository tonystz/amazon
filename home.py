from playwright.sync_api import sync_playwright
'''
pip install pytest-playwright
playwright install
'''
def get(url):
    with sync_playwright() as p:
        context = p.request.new_context()
        response = context.get(url)
        content=response.body().decode('utf-8')
        open('log/home.html','w',encoding='utf-8').write(content)
        return content
        # # assert response.ok
        # # # assert response.status == 200
        # # # assert response.headers["content-type"] == "application/json; charset=utf-8"
        # # # assert response.json()["name"] == "foobar"
        # # open('a.html','w',encoding='utf-8').write(response.body().decode('utf-8'))
        # browser=[p.chromium, p.firefox, p.webkit]
        # for browser_type in [browser[0]]:
        #     browser = browser_type.launch()
        #     context = browser.new_context()
        #     response = context.get("https://www.amazon.com/SEALIGHT-360-degree-Illumination-Brightness-Installation/dp/B098DWSXT2")
        #     # page.goto(url)
        #     # page.screenshot(path='log/home.png')
        #     print(response.body())
        #     browser.close()
        #     return c

# import asyncio
# from pyppeteer import launch

# async def main():
#     # launch chromium browser in the background
#     browser = await launch()
#     # open a new tab in the browser
#     page = await browser.newPage()
#     # add URL to a new page and then open it
#     await page.goto("https://www.amazon.com/SEALIGHT-360-degree-Illumination-Brightness-Installation/dp/B098DWSXT2")
#     # create a screenshot of the page and save it
#     await page.screenshot({"path": "test.png"})
#     conttent = await page.content()
#     # close the browser
#     await browser.close()
#     return conttent

# if __name__ == '__main__':
#     '''
#     https://www.scrapingbee.com/blog/pyppeteer/#what-is-pyppeteer-
#     https://medium.com/@ssmak/how-to-fix-puppetteer-error-while-loading-shared-libraries-libx11-xcb-so-1-c1918b75acc3
#     '''
#     print("Starting...")
#     conttent = asyncio.get_event_loop().run_until_complete(main())
#     print("Screenshot has been taken")
#     print(conttent)
if __name__ == '__main__':
    get('https://www.amazon.com/SEALIGHT-360-degree-Illumination-Brightness-Installation/dp/B098DWSXT2')