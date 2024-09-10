# İngilizce sözlükten veri çekme

Bu uygulamada ister terminalden kelime yazarak anlamını çekebilirsiniz ister API yi çalıştırır istek atarsınız tercih sizin ben ikisinide açıklyacağim

## Kurulum

ilk önce paketi klonluyoruz [git](https://github.com/SADOx00/tureng-sozluk-api.git)

```bash
git clone https://github.com/SADOx00/tureng-sozluk-api.git
```

## 1.Kullanımı

```bash
cd app # uygulamanın içine giriyoruz 
```
```bash
pip install -r requirements.txt # gerekli paketleri yüklüyoruz
```
```bash
python main.py #uygulammızı çalıştıyoruz
```
Sonra bilmek istediğimiz Kelimeyi Yazıyoruz

Ve biraz bekledikten sonra sonuçlarımız geliyor:
![Ekran görüntüsü 2024-09-10 151246](https://github.com/user-attachments/assets/f2a3d780-a500-43c6-96bd-90377f017b47)
![unknown_2024 09 10-15 22-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/35c0e802-f11b-4c1c-984d-ad0e83ff5c01)

## 2.Kullanımı
```bash
cd app # uygulamanın içine giriyoruz 
```
```bash
pip install -r requirements.txt # gerekli paketleri yüklüyoruz
```
```bash
python API.py #APİ mizi çalıştıyoruz
```
Bundan sonra Local host'ta :

http://127.0.0.1:5000

 adresimize istek atabilecek duruma geliyoruz 
**PEKİ AMA NASIL İSTEK ATACAĞIZ**

### 1.Yöntem Direkt URL  üzerinden
```url
http://localhost:5000/api/word?word=example 
```
Burda example yerine istediğiniz kelimeyi yazabilirsiniz.

sonuçlar şöyle olacaktır:

### Örnek Yanıt

```json
{
    "word": "example",
    "meanings": [
        "örnek",
        "misal",
        "numune",
        "model",
        "emsal",
        "misal",
        "temsilci",
        "temsil",
        "örnek olay",
        "örnek"
    ],
    "sentences": [
        "This is an example sentence.",
        "Here's another example sentence.",
        "Finally, a third example sentence."
    ]
}
```
- **`word`**: API'ye gönderdiğiniz kelime.
- **`meanings`**: Kelimenin anlamlarını içeren liste.
- **`sentences`**: Kelimenin kullanıldığı cümleleri içeren liste.


### 2.Yöntem Python ile
```python
import requests

response = requests.get("http://localhost:5000/api/word", params={"word": "example"})
data = response.json()

print(data)
```
### 3.Yöntem  JavaScript  ile
```javascript
fetch('http://localhost:5000/api/word?word=example')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));

```





## License
[MIT](https://choosealicense.com/licenses/mit/)
