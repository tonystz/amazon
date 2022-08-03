from fake_useragent import UserAgent

'''
get home from:
1: requests
2: playwright browser
'''
HOME_FROM=1

'''
#navigator.connection
https://developer.mozilla.org/en-US/docs/Web/API/Navigator/connection
'downlink': '1.4',
'ect': '3g',
'rtt': '1000',
'''

''' china location
L5Z9:CN
'''
headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cache-control': 'max-age=0',
            'downlink': '2.6',
            'ect': '4g',
            'rtt': '100',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': "macOS",
            'sec-fetch-dest': "document",
            'sec-fetch-mode': "navigate",
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        }



# copy from request header: https://www.amazon.com/Forenner-Headlight-Conversion-Installation-Replacement/dp/B096812T9V
headerstr='''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7
cache-control: max-age=0
cookie: session-id-time=2082787201l; session-id=133-9424710-3846764; ubid-main=131-4430385-2075638; i18n-prefs=USD; sp-cdn="L5Z9:CN"; lc-main=en_US; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1649340053142-768021.32_0; regStatus=pre-register; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19203%7CMCMID%7C26726776119005477131231249625536253419%7CMCAAMLH-1659708410%7C11%7CMCAAMB-1659708410%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1659110810s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; session-token=qs27jqtlPaw4I8jN0JhjceaGFKj5BiS6tlAc2iZBx41PiXuONheQjopTuQQ8NoN0+ZK340xIyb4CSAV8As2m0a/uzEcfLBWNQhz2xlq8x64F6OKOWBcHqfU/bx0qRPw1EELXhu4uftwxVz4f5UkyhI9wjVshT73yDu85NF/TQBu73NVx8lY/cLDhdz0Wjs2kCfp5qcfPTRncLRqwQB3KBLT8iVKi6r7Y; csm-hit=tb:s-MRVM4SDQ88RQT0JC0YXZ|1659428713463&t:1659428715182&adb:adblk_no
device-memory: 8
downlink: 1.25
dpr: 1
ect: 3g
rtt: 250
sec-ch-device-memory: 8
sec-ch-dpr: 1
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-ch-viewport-width: 1280
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
viewport-width: 1280
'''

for i in headerstr.splitlines():
    d =i.split(':')
    d = [i.strip() for i in d]
    if len(d) == 2 and d[0] != 'cookie':
        headers[d[0]]=d[1].strip()

# headers["user-agent"] = UserAgent(path=r'ua.json').random

# save response body
SAVE_BODY=False
