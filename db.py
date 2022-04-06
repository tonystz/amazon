import sqlite3
from logger import logger

class DataBase():
    def __init__(self) -> None:
        self.con = sqlite3.connect('data.db')
    
    def create(self):
        cur = self.con.cursor()
        # Create table
        if True:
            cur.execute('''CREATE TABLE parts("asin" text,
                "year" integer,
                "makeId" integer,
                "makeIdtxt" TEXT,
                "modelId" integer,
                "modelIdtxt" TEXT,
                "submodelId" integer,
                "submodelIdtxt" TEXT,
                "fit" text,
                "engine" integer,
                "enginetxt" TEXT,
                "bodyStyle" integer
                "bodyStyletxt" TEXT,
                "note" TEXT,
                "url" text
                )''')
        else:
            cur.executescript('''
            ALTER TABLE parts ADD COLUMN bodyStyletxt TEXT;
            ''')
        self.con.commit()
        cur.close()
        
    def execute(self,sql,parameters):
        logger.debug(f'sql={sql},p={parameters}')
        cur = self.con.cursor()
        cur.execute(sql,parameters)
        self.con.commit()
        cur.close()
    
    def executeBatch(self,sql,batchParametersh, deleteSql=None,deleteParameters=None):
        logger.debug(f'sql={sql},p={batchParametersh}')
        cur = self.con.cursor()
        cur.execute("begin")
        try:
            if deleteSql:
                logger.debug(f'sql delete={deleteSql} {deleteParameters}')
                cur.execute(deleteSql,deleteParameters)
            for parameters in batchParametersh:
                cur.execute(sql,parameters)
                cur.execute("commit")
        except Exception as e:
            logger.error(f"sql failed! {e}")
            cur.execute("rollback")
        cur.close()
    
    def fetch(self,sql,parameters=None):
        logger.debug(f'sql={sql},p={parameters}')
        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.con.row_factory = dict_factory
        cur = self.con.cursor()
        if parameters:
            cur.execute(sql,parameters)
        else:
            cur.execute(sql)
        rows = cur.fetchall()
        logger.debug(f'{rows}')
        self.con.commit()
        cur.close()
        return rows
    
    def executeInsertUpdate(self,rs:dict,updateCol:list,ids:list):
        assert 'rowid' in rs.keys()

        sqlk=[k for k,v in rs.items() if v and k not in ['rowid']+updateCol]
        sqlv=[v for k,v in rs.items() if v and k not in ['rowid']+updateCol]
        sqlk.extend(updateCol)

        self.executeBatch(f'''INSERT INTO parts({','.join(sqlk)})VALUES({','.join(['?']*len(sqlk))})''',
        [sqlv+list(ids) for ids in ids ],
        deleteSql='delete from parts where rowid=?',
        deleteParameters=(rs['rowid'],))

    def getMakeId(self,asin,year):
        return self.fetch('select makeId from parts where asin=? and year=?',(asin,year,))

    def getModelId(self,asin,year,makeId):
        return self.fetch('select modelId from parts where asin=? and year=? and makeId=?',(asin,year,makeId))

    def getSubmodelId(self,asin,year,makeId,modelId):
        return self.fetch('select submodelId from parts where asin=? and year=? and makeId=? and modelId=?',(asin,year,makeId,modelId))
    
    def getMoreAttrViaSubmodelId(self,asin,year,makeId,modelId,submodelId):
        return self.fetch('select submodelId,engine,bodyStyle from parts where asin=? and year=? and makeId=? and modelId=? and submodelId=?',(asin,year,makeId,modelId,submodelId))
    
    def insertUpdateModelId(self,asin,year,makeId,ids):
        rs = self.fetch('select rowid,* from parts where asin=? and year=? and makeId=? and modelId is NULL',(asin,year,makeId))
        assert len(rs) == 1
        self.executeInsertUpdate(rs[0],['modelId','modelIdtxt'],ids)
    
    def insertUpdateSubmodelId(self,asin,year,makeId,modelId,ids):
        rs = self.fetch('select rowid,* from parts where asin=? and year=? and makeId=? and modelId=? and submodelId is NULL',(asin,year,makeId,modelId))
        assert len(rs) == 1

        self.executeInsertUpdate(rs[0],['submodelId','submodelIdtxt'],ids)

    
    def insertUpdateMoreAttr(self,asin,year,makeId,modelId,submodelId,ids):
        rs = self.fetch('select rowid,* from parts where asin=? and year=? and makeId=? and modelId=? and submodelId =?',(asin,year,makeId,modelId,submodelId))
        assert len(rs) == 1
        
        self.executeInsertUpdate(rs[0],['engine','enginetxt','bodyStyle','bodyStyletxt'],ids)
    
    def checkFit(self,asin,year,makeId,modelId,submodelId):
        sql='select fit from parts where asin=? and year=? and makeId=? and modelId=? and submodelId=?'
        return self.fetch(sql,(asin,year,makeId,modelId,submodelId))

    def updateFit(self,fit,note,rowid):
        sql='update parts set fit=?, note=? where rowid=?'
        self.execute(sql,(fit,note,rowid))
    
    def getPartUnkown(self):
        return self.fetch('select rowid,* from parts where fit is NULL or fit == "unknown" limit 100')

    def close(self):
        self.con.close()
    
    def insertMakeId(self,asin,year,ids,url):
        sql='''INSERT INTO parts(asin,year,makeId,makeIdtxt,url)VALUES(?,?,?,?,?)'''
        self.executeBatch(sql,[(asin,year,makeId[0],makeId[1],url) for makeId in ids])


if __name__ == '__main__':
    DataBase().create()
    # print(DataBase().getPartUnkown('B07VHMX2NT',2003))
    # DataBase().updateFit(157)
    # print(DataBase().fetch('select * from parts where id=?',(25,)))
    # DataBase().insertUpdateModelId('B07Q24LVDM',2009,58,[(23,'moduleidxx'),(24,'23sxx')])