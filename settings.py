from fake_useragent import UserAgent

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
# headers["user-agent"] = UserAgent(path=r'ua.json').random


# copy from request header: https://www.amazon.com/Forenner-Headlight-Conversion-Installation-Replacement/dp/B096812T9V
headerstr='''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,id;q=0.5,gl;q=0.4
cache-control: max-age=0
cookie: aws-ubid-main=468-0066304-8374066; aws-session-id=839-6066719-5968543; aws-analysis-id=839-6066719-5968543; remember-account=false; aws-session-id-time=1646721876l; noflush_locale=en; sp-cdn="L5Z9:HK"; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1649383029520-768214.32_0; awsc-color-theme=light; regStatus=pre-register; session-id=144-1013221-5780831; ubid-main=130-6365689-3306938; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Asts%3A%3A252285218316%3Aassumed-role%2FADFS-ADMIN%2Ftony_su%22%2C%22alias%22%3A%22sandstorm-dev%22%2C%22username%22%3A%22assumed-role%252FADFS-ADMIN%252Ftony_su%22%2C%22keybase%22%3A%22j4vrW%2Bu3X303s7ql8lTBlsheivFx6qA4m5ib370mqfw%5Cu003d%22%2C%22issuer%22%3A%22%22%2C%22signinType%22%3A%22PUBLIC%22%7D; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6IjNhYWFiODU3LTRlZjItNGRjNi1iOTEwLTI4Y2IwYmZiNDM3ZSJ9.eyJzdWIiOiJzYW5kc3Rvcm0tZGV2Iiwic2lnbmluVHlwZSI6IlBVQkxJQyIsImlzcyI6IiIsImtleWJhc2UiOiJqNHZyVyt1M1gzMDNzN3FsOGxUQmxzaGVpdkZ4NnFBNG01aWIzNzBtcWZ3PSIsImFybiI6ImFybjphd3M6c3RzOjoyNTIyODUyMTgzMTY6YXNzdW1lZC1yb2xlXC9BREZTLUFETUlOXC90b255X3N1IiwidXNlcm5hbWUiOiJhc3N1bWVkLXJvbGUlMkZBREZTLUFETUlOJTJGdG9ueV9zdSJ9.zZBlKgzHdS2hYxHsEYBRrvGJlEdNdTkbKeXsmTrI9XM7LMmyTQxq6Nm2QtPrdMXNfOKF1Y0XulnT5lWPcUcbwVufGhMs9cAropoCqjZgNf5FvQ-42e2wSf2mz-pn7F7i; awsc-uh-opt-in=; noflush_awsccs_sid=496bff63f2e097b213acae817d6beac11d6fb013f98219ed55555db72f994696; aws-signer-token_us-west-2=eyJrZXlWZXJzaW9uIjoiQzg2V3NIQmZLRTRqSkRTa29iWm1ZejhXTjBOMVFoaFMiLCJ2YWx1ZSI6IkZHSGRWdmRuZkRoS3BhemQycEx0R0VyZkFPa25WWG40RGFIMEwvbDdIY009IiwidmVyc2lvbiI6MX0=; aws-signer-token_us-east-1=eyJrZXlWZXJzaW9uIjoiRmlOYUV5a0tzSXViXzFyUTE1N2kuNjRsblZjVkxpR0oiLCJ2YWx1ZSI6ImNEOENvK25URU5DN1hERXAydzNScElFdFh1emtleUVjS2FCS0Z3OTl1c289IiwidmVyc2lvbiI6MX0=; session-id-time=2082787201l; i18n-prefs=USD; session-token="HCTwLx10xsDIAKr2PqAzcj5NhChaJqIjnHlxJyKMfgqgfaTwfC1p5RKIn3OP0zuxPjBp8xlEb+iUKXIoT88xPOMfrVLoU1y+qNohgG+4Xbp1e3Bz5d1EVtYBmxauULZJ3vzyYqq8PxoOT2E8EDsgBrbtYkMe1NfG4Um2LYiP1/QNzD/sTJ7fpr3OzTlQWQqT560MGtyZQhAUp8RZI2RQEA=="; csm-hit=tb:s-2F49WPKNSEMTVBS53HEX|1659003449170&t:1659003450294&adb:adblk_yes
device-memory: 8
downlink: 1.45
dpr: 1
ect: 4g
rtt: 150
sec-ch-device-memory: 8
sec-ch-dpr: 1
sec-ch-ua: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-ch-viewport-width: 1920
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
viewport-width: 1920
'''

for i in headerstr.splitlines():
    d =i.split(':')
    d = [i.strip() for i in d]
    if len(d) == 2 and d[0] != 'cookie':
        headers[d[0]]=d[1].strip()