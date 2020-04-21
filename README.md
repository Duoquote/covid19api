# Covid19 Virus data compiled from https://covid19.saglik.gov.tr/
## Access API here: https://covid19reqapi.herokuapp.com/
### Data updated every hour but the origin data is updated daily, so don't expect many changes as the actual data is going to be updated daily.
In this project, I parse the Covid19 Virus data from saglik.gov.tr, and compile it into REST API kind of data. The structure is as follows:
```json
{
  "dailyData": {
    "3-10-2020": {
      "date": 1583787600000,
      "cases": "1",
      "deaths": "0"
    },
    .
    .
    .
    "4-19-2020": {
      "date": 1587243600000,
      "cases": "86306",
      "deaths": "2017"
    },
    "4-20-2020": {
      "date": 1587330000000,
      "cases": "90980",
      "deaths": "2140"
    }
  },
  "detail": {
    "total_tests": 673980,
    "total_cases": 90980,
    "total_deaths": 2140,
    "total_intense_care": 1909,
    "total_incubated": 1033,
    "total_head": 13430
  }
}
```
The date is in `MM-DD-YYYY` format.

Assuming you assign the data to `data` object, the data as follows:
| Location | Type | Data |
| --- | --- | --- |
| data.detail.dailyData | Dictionary | Indices are dates in format of `MM-DD-YYYY`. Has daily data about cases, deaths and unix timestamp of that day. |
| data.detail.dailyData[*].date | Integer | Date in unix timestamp format. |
| data.detail.dailyData[*].cases | Integer | Cases recorded on that day. |
| data.detail.dailyData[*].deaths | Integer | Deaths recorded on that day. |
| data.detail.total_tests | Integer | Total tests made. |
| data.detail.total_cases | Integer | Total cases. |
| data.detail.total_deaths | Integer | Total deaths. |
| data.detail.total_intense_care | Integer | Total people in intense care. |
| data.detail.total_cases | Integer | Total people incubated |
| data.detail.total_healed | Integer | Total people healed. |



# Türkçe Açıklama
Bu projede, saglik.gov.tr'den corona virüsünün verisi alınıp, REST API için hazır hale getirilip sunulmaktadır. https://covid19reqapi.herokuapp.com/ adresine `GET` isteği göndererek, JSON formatında veriyi alabilirsiniz. Verinin yapısı oldukça basit, yukarıda örnek bir JSON verisi var. Verinin detaylı açıklaması aşağıdaki tablodadır.

Aşağıdaki tablo, alınan veriyi `data` değişkenine atadığınızı varsayaraktan açıklanmıştır.
| Konum | Veri Tipi | Veri |
| --- | --- | --- |
| data.detail.dailyData | Dictionary | Anahtarları `AY-GÜN-YIL` biçiminde olan girdiler vardır. Girdilerde unix timestamp olarak tarih, gün içi vaka ve gün içi ölüm sayısı vardır. |
| data.detail.dailyData[*].date | Integer | Unix timestamp formatında tarih içerir. |
| data.detail.dailyData[*].cases | Integer | O gün kaydedilen vaka sayısını içerir. |
| data.detail.dailyData[*].deaths | Integer | O gün kaydedilen ölüm sayısını içerir. |
| data.detail.total_tests | Integer | Toplam yapılan test sayısını içerir. |
| data.detail.total_cases | Integer | Toplam vaka sayısını içerir. |
| data.detail.total_deaths | Integer | Toplam ölüm sayısını içerir |
| data.detail.total_intense_care | Integer | Toplam yoğun bakımda olan kişi sayısını içerir. |
| data.detail.total_cases | Integer | Toplam entübe olan kişi sayısını içerir. |
| data.detail.total_healed | Integer | Toplam iyileşen kişi sayısnı içerir. |
