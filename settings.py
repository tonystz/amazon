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


# copy from https://www.amazon.com/Forenner-Headlight-Conversion-Installation-Replacement/dp/B096812T9V
headerstr='''
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,id;q=0.5,gl;q=0.4
cache-control: max-age=0
cookie: aws-ubid-main=468-0066304-8374066; aws-session-id=839-6066719-5968543; aws-analysis-id=839-6066719-5968543; session-id=139-7170060-6722130; remember-account=false; ubid-main=134-7999112-0304468; aws-session-id-time=1646721876l; awsc-color-theme=light; aws-target-data=%7B%22support%22%3A%221%22%7D; aws-target-visitor-id=1647673369382-469574.32_0; noflush_locale=en; awsc-uh-opt-in=optedIn; aws-userInfo=%7B%22arn%22%3A%22arn%3Aaws%3Asts%3A%3A711171116841%3Aassumed-role%2FADFS-READONLY%2Ftony_su%22%2C%22alias%22%3A%22ddcloud-aws-devops%22%2C%22username%22%3A%22assumed-role%252FADFS-READONLY%252Ftony_su%22%2C%22keybase%22%3A%22SSquF6meIF7h6r05KDlu5A1gmjHilYirKHB%2BqzOH%2FFY%5Cu003d%22%2C%22issuer%22%3A%22%22%2C%22signinType%22%3A%22PUBLIC%22%7D; aws-userInfo-signed=eyJ0eXAiOiJKV1MiLCJrZXlSZWdpb24iOiJ1cy1lYXN0LTEiLCJhbGciOiJFUzM4NCIsImtpZCI6ImFhNDFkZjRjLTMxMzgtNGVkOC04YmU5LWYyMzUzYzNkOTEzYiJ9.eyJzdWIiOiJkZGNsb3VkLWF3cy1kZXZvcHMiLCJzaWduaW5UeXBlIjoiUFVCTElDIiwiaXNzIjoiIiwia2V5YmFzZSI6IlNTcXVGNm1lSUY3aDZyMDVLRGx1NUExZ21qSGlsWWlyS0hCK3F6T0hcL0ZZPSIsImFybiI6ImFybjphd3M6c3RzOjo3MTExNzExMTY4NDE6YXNzdW1lZC1yb2xlXC9BREZTLVJFQURPTkxZXC90b255X3N1IiwidXNlcm5hbWUiOiJhc3N1bWVkLXJvbGUlMkZBREZTLVJFQURPTkxZJTJGdG9ueV9zdSJ9.OGj1dY4pNcoknz35Xxt1pulpiPTHuS3v55D_NDReUuO4N_EmIY8Gix9KeSgXCZyAWDZgdR8LiBVbY9dZHNBStfBcItO4toOxpoRiM7AzJl5u2kl6YVeJ6UM41G34-n79; noflush_awsccs_sid=10a519ef4d4c866bf5c84be3b13ca64934d09feb46e6e81d63488a9308200bde; session-id-time=2082787201l; i18n-prefs=USD; UM_distinctid=17fbba7c756471-05acb51122dc1c-3a67410c-e1000-17fbba7c7578c9; session-token=ej6pkSb5zDUNdR+vZHx9yfQ2u8cPftpeaWFRr5yf0Dx244NBuUo66TGMVbrPp0Ufogm9v1Wi9bRNxg21q1sl5lHnTZoURyixiXUczV2E1M2PmrC1iJh6ZDEqFRnkrw/nr9uh9BzFBZzEChx6p/c0xXlWdw3eb1TyrJcXbBLPpDzVcwwaxUW3dFr71GtQZKhf; csm-hit=tb:s-J94N57F0QGPRR06VPTX2|1648208380119&t:1648208382974&adb:adblk_yes; CNZZDATA1256793290=317762228-1648119644-%7C1648201410
device-memory: 8
downlink: 3.35
dpr: 1.5
ect: 4g
rtt: 100
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"
sec-ch-ua-mobile: ?0
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
viewport-width: 853
'''

for i in headerstr.splitlines():
    d =i.split(':')
    d = [i.strip() for i in d]
    if len(d) == 2 and d[0] != 'cookie':
        headers[d[0]]=d[1].strip()