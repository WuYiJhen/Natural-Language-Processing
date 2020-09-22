class WordSearch:
    def __init__(self):
        self.trie = {}
        self.res = {}
        self.keywords = set()
        
    def load_keywords(self, keywords, add=False):
        for word in keywords:
            cur = self.trie
            for s in word:
                if s not in cur: cur[s] = {}
                cur = cur[s]
            cur['*'] = True
        if not add: self.keywords = set(keywords)
            
    def add_keywords(self, words):
        for word in words:
            if word not in self.keywords:
                self.keywords.update([word])
                self.load_keywords([word], True)
            else: print('Word "%s" is already in keywords.'%(word))
        
    def del_keywords(self, words):
        for word in words:
            if word in self.keywords:
                self.keywords.remove(word)
                cur = self.trie
                for s in word:
                    cur = cur[s]
                cur.pop('*', None)
            else: print('Word "%s" is not in keywords.'%(word))
        
    def return_keywords(self):
        return (self.keywords, self.trie)
    
    def rebuild_trie(self):
        self.trie = {}
        self.load_keywords(self.keywords, True)
        
    def search(self, x):
        res = {}
        i, bloc, word, cur = 0, -1, '', self.trie
        while i < len(x):
            if x[i] in cur:
                if bloc < 0: bloc = i
                word += x[i]
                if '*' in cur[x[i]]:
                    if word not in res:     
                            res[word] = {'index': [[bloc, i]], 'count': 1}
                    else:
                        res[word]['index'].append([bloc, i])
                        res[word]['count'] += 1
                cur = cur[x[i]]
                i += 1
            else:
                if bloc >= 0: i, bloc, word, cur = bloc, -1, '', self.trie 
                i += 1    
        return res


if __name__ == '__main__':
    keywords = ['台股', '三大法人', '外資', '面板雙虎', '台積電', '金融股', '晶電', '期貨', '群創', '國泰金', '富邦', '台達']
    wordsearch = WordSearch()
    wordsearch.load_keywords(keywords)
    wordsearch.add_keywords(['中環', '合計', '外資', '台達化', '華航', '長榮', '達邁', '台表科', '賣超', '中信金', '台新金'])
    wordsearch.del_keywords(['面板雙虎', '三大法人', '1000'])
    wordsearch.add_keywords(['三大法人'])
    wordsearch.del_keywords(['合計'])
    # wordsearch.rebuild_trie()
    # wordsearch.return_keywords()

    x = '''台股今 (21) 日在權值股普遍走弱下，摜破 12800 點關卡，終場下跌 80.5 點或 0.63%，收在 12795.12 點，三大法人同步站在賣方，合計 130.35 億元，其中內外資再度聯手調節台積電逾 1.7 萬張，其中，外資反手調節多檔金融股，不過內外資對面板雙虎不同調，外資減碼近 4 萬張、投信則買超近 2 萬張。
        台股今日成交量縮至 1706 億元，外資連 3 賣，賣超 64.78 億元，期貨淨多單也減少 6019 口，降至 13158 口；投信賣超 6.13 億元、自營商同步賣超 59.42，三大法人合計賣超 130.35 億元。
        觀察外資今日買超，大舉回補元大台灣 50 反 1 逾 22 萬張，躍居冠軍，傳產股台塑 8331 張、東和鋼鐵 4582 張，聯家軍的聯電及欣興也分別買超 5878、6215 張。
        外資賣超方面，前兩名分別為面板雙虎友達逾 2 萬張、群創 1.9 萬張，持續調節台積電 1.4 萬張，其他則鎖定金融股，包括兆豐金 1.6 萬張、新光金 1.6 萬張、中信金 1.5 萬張、國泰金 9051 張，其餘則為晶電 1.1 萬張、富邦 VIX 8487 張。
        投信買超前 10 名分別為群創 1.1 萬張、友達 6234 張、頎邦、佳凌、創惟、南亞科、奇鋐、聯電、華夏及臻鼎 - KY；賣超標的前 10 名分別為晶電、華航、長榮、達邁、台積電、廣明、台表科、華通、台泥、亞泥。
        自營商買超前 10 名包括晨訊科 - DR、創惟、中壽、華城、興富發、台新金、美德醫療 - DR、榮成、中鋼及遠雄港；賣超前 10 名包括聯電、台積電、鴻海、金寶、友達、台達化、晶電、京元電、旺宏、中環'''

    res = wordsearch.search(x)
    print(res)