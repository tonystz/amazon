import json
import re
import requests
from bs4 import BeautifulSoup

import time
import random
import logger
import settings
import attributes
import html

# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1
class AmazonVehicleParts():
    def __init__(self, product_url) -> None:
        self.product_url = product_url
        self.logger = logger.logger
        self.save_body = logger.save_body
        self.session = requests.Session()
        self.session.cookies['lc-main']='en-US'
        self.asin=product_url.split('/dp/')[1].strip('/')
        self.logger.info(f'product url {product_url} and id {self.asin}')
        self.http_code={}
    
    def checkHttpCode(self,status_code):
        if status_code == 200: return
        if status_code not in self.http_code:
            self.http_code[status_code] = 0
        self.http_code[status_code] +=1
        for status_code in [403]:
            assert self.http_code.get(status_code,0) < 4

    def sleep(self,timeout=None):
        if timeout:
            time.sleep(timeout)
            return
        time.sleep(random.randint(0,1))
    
    def __getAutomotiveId(self):
        _idrandom=str(int(round(time.time() * 1000)))[-3:] + str(random.random())[-3:]
        idrandom = f'automotive-pf-partfinder-secondary-view-id-{_idrandom}'
        self.logger.debug(f'id:{idrandom}')
        return idrandom

    def get_token(self):
        if settings.HOME_FROM == 2:
            import home
            # page = home.asyncio.get_event_loop().run_until_complete(home.main())
            self.logger.info('via browser')
            return BeautifulSoup(
            re.search(r"<!--CardsClient-->(.*)", home.get(self.product_url)).group(1),
            "lxml",
            ).find_all("div")
        else:
            rsp = self.session.get(self.product_url, headers=settings.headers,timeout=(60,60))
            self.save_body('homepage',rsp)
            self.logger.info('via http request')
            return BeautifulSoup(
            re.search(r"<!--CardsClient-->(.*)<input", rsp.text).group(1),
            "lxml",
            ).find_all("div")
        
    def requestTokenFromHome(self):
        initial_soup= self.get_token()
        # page = open('log/home.html').read()        
        
        for div in initial_soup:
            id = div.get('id')
            self.dapparams = div.get('data-acp-params')
            self.dappath= div.get('data-acp-path')
            self.logger.info(f'find info from homepage: data-acp-params={self.dapparams} data-acp-path={self.dappath}')
            break
        if self.dapparams and self.dappath:
            self.logger.info('find token sucessfully')
        else:
            self.logger.error('fail to find token')
        return self
    
    def __postRequest(self,step,url,payload):
        self.sleep()
        for i in range(3):
            response = self.session.post(url, json=payload, headers=settings.headers,timeout=(60,60))
            if response.status_code == 200:
                break
            self.sleep()
        self.logger.info(f'{step}: {response} {response.url}')
        self.save_body(f'{step}',response)
        return response

    def requestFirstSelect(self):
        first_select_url=f'https://www.amazon.com/{self.dappath}getPartfinderGarageEntitySelection?ref_=pf_dsk_pu&hitType=pageTouch&pageAssemblyType=main'
        
        payload = {
            "asin":self.asin,
            "attributesSelectionFlow":"vehicle-by-attributes",
            "attributesSelectionType":"variant","currentSelections":[],
            "garageVehicleSelectionType":"vehicles-view",
            "id":self.__getAutomotiveId(),
            "requiredSelection":[]}

        settings.headers.update(
            {
                "x-amz-acp-params": self.dapparams,
                "x-requested-with": "XMLHttpRequest",
                "referer":self.product_url,
            }
        )
        return self.__postRequest('select1',first_select_url,payload=payload)

    def requestAttribute(self,selections=None):
        '''
        selection = [{"id": "year", "value": "2022"}]
        '''
        attrURL=f'https://www.amazon.com/{self.dappath}getAttributesSelectionView'

        payload={	
            "asin":self.asin,	
            "attributesBlockIndex":"1",	
            "id":f"{self.__getAutomotiveId()}-garage-vehicle-selection-vehicle-attributes-selection",
            "isLayoutHorizontal":'false',	
            "requiredSelection":[],	
            "selectionType":"variant",	
            }
        payload["selections"] = selections if selections else attributes.Selections().get()
        
        self.logger.info(f'attrURL: sendselection: {json.dumps(payload["selections"])}')
        response =  self.__postRequest('attrURL',attrURL,payload=payload)
        return attributes.parserActive(response.text)

    def requestPartfinder(self, selections=None):
        findUrl=f'https://www.amazon.com/{self.dappath}getPartfinderView?ref_=pf_dsk_ftr&hitType=pageTouch&pageAssemblyType=main'

        payload={
            "asin":self.asin,
            "id":"automotive-pf-primary-view",
            "inputSelections":[],
            "selectionType":"VehicleAttribute",
        }
        payload["selections"] = selections if selections else attributes.Selections(year=2018,makeId=45,modelId=25218).get()
        self.logger.info(f'findUrl: sendselection: {payload["selections"]}')
        response =  self.__postRequest('findUrl',findUrl,payload=payload)
        if response.status_code == 400 and len(response.text) == 0:
            self.logger.error('fit error: delete and try  again later')
            return 'err','error,400'
        self.checkHttpCode(response.status_code)
        return self.checkPartfinderView(response.text)

    def checkPartfinderView(self,body):
        '''
        2008 Saab 9-3 fit: id=automotive-pf-primary-view-yes-fitment-note-with-popover
        not fit: id=automotive-pf-primary-view-no-this-does-not-fit-message
        '''
        fit='unknown'
        if body.find('automotive-pf-primary-view-no-this-does-not-fit-message') != -1 or body.find('This does not fit') !=-1:
            fit = 'not'
        elif body.find('automotive-pf-primary-view-yes-fitment-note-with-popover') != -1 or body.find('This fits') != -1:
            fit = 'yes'
        d=[]
        bsobject=BeautifulSoup(body,'lxml')
        for div in bsobject.find_all('span'):
            if len(str(div.getText()).strip()) in [0,1]: continue
            d.append(str(div.getText()).strip())
        bsnote=bsobject.select('#'+'a-popover-automotive-pf-primary-view-yes-fitment-note-with-popover-popover')
        note = html.unescape(bsnote[0].text).encode('utf-8') if bsnote else None

        self.logger.info(f"fit info: {fit}. note={note} {','.join(list(set(d))).encode('utf-8')}")
        return fit,note

if __name__ == '__main__':
    AmazonVehicleParts('https://www.amazon.com/SEALIGHT-360-degree-Illumination-Brightness-Installation/dp/B098DWSXT2').requestTokenFromHome()

