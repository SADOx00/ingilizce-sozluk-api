from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options




class Manage:

    """
    kullanımı değişken = Manage(word=str) => word = ingilizce kelime
    """
    def __init__(self, word):
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Tarayıcıyı görünmez modda başlatır
        self.driver = webdriver.Firefox(options=firefox_options)

        self.word = word
        self.connect()
        sleep(0.5)




    def connect(self):
        """
        kullanımı
        verilen word'e göre bir bağlantı oluşturur.


        """


        url = f"https://tureng.com/tr/turkce-ingilizce/{self.word}"
        self.driver.get(url)

    def rslt(self):
        try:
            table = self.driver.find_element(By.XPATH, "//*[@id='englishResultsTable']")
        except:
            return False
        else:
            return True

    def get_10_meanings(self):
        """
        kullanımı: değişken = get_10_meanings(self)
        ve değişkene kelimenin on anlamını içeren bir dize atanır.

        """
        num = 0
        table = self.driver.find_element(By.XPATH,"//*[@id='englishResultsTable']")
        meanings = []
        tr_s = table.find_elements(By.TAG_NAME, "tr")

        for i in tr_s:
            if num == 10:
                break
            i_c = i.get_attribute("class")
            if i_c == "tureng-manual-stripe-odd" or i_c == "tureng-manual-stripe-even":
                td_s = i.find_elements(By.TAG_NAME,"td")
                for j in td_s:
                    j_lang =j.get_attribute("lang")
                    if j_lang=="tr":
                        meanings.append(j.text.strip())
                        num += 1
        return meanings

    def get_sentences(self):
        """
        kullanımı:
        değişken=get_sentence(self)
        ve değişkene en fazla 3 adet cümle atanır.

        """
        table = self.driver.find_element(By.XPATH, "//*[@id='englishResultsTable']")
        num = 0
        sentences = []
        tr_s = table.find_elements(By.TAG_NAME, "tr")
        for i in tr_s:
            if num == 3:
                break
            i_c = i.get_attribute("class")
            if i_c=="tureng-manual-stripe-even example-sentences-row" or i_c == "tureng-manual-stripe-odd example-sentences-row":
                sentences.append(i.text)
                num+=1
        sentencess=[]
        for i in sentences:
            i= i.split("\n\n")
            sentencess.append(i[0])
        return sentencess

    def close(self):
        """
        Kullanımı: Bağlantıyı koparır.
        """
        self.driver.close()


"""
𝓢4𝓓0 𝓟4𝓢𝓗4
FULLSTACK DEVELOPER
DATE: SEPTEMBER 10 2024
GİTHUB: https://github.com/SADOx00
"""









