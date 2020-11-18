# Covid19 Virus data compiled from https://covid19.saglik.gov.tr/
## Access API here: https://covid19reqapi.herokuapp.com/
### Data updated everyday at night.
The data is created with my insanely complicated (if you don't know regex) regular expression from pdf files. Using `mutool` I convert them to txt and parse the text with my regular expression. After that we have a json file which is currently `753kb`. I am planning to add a few functions to query the data in node.js but currently the node.js server only servers the json file. I added github workflows to auto update the data everyday.
Here is an example of one day:
```json
[
  {
    "summary": [
      "Bir önceki güne göre COVID-19 test sayısında ve hastaneden taburcu edilen yeni hasta sayısında artış (sırasıyla %6,5 ve %2,8), hastaneye yatırılan yeni hasta sayısında ise azalma (-%0,3) görülmüştür.",
      "Bir önceki güne göre bölgelerdeki yeni hasta değişim yüzdesine bakıldığında; en fazla azalış Batı Marmara Bölgesinde gerçekleşmiştir (-%13,5). En fazla artış ise Doğu Karadeniz Bölgesinde olup hasta sayısı açısından incelendiğinde bu fark 23 hastadır.",
      "25-49 yaş grubunda 1.000.000 kişiye düşen yeni COVID-19 hasta sayısı kadınlarda 54,3, erkeklerde ise 55,8’dir.",
      "Bir önceki güne göre hastaneye yatırılan yeni hasta sayısındaki en fazla azalış Kuzeydoğu Anadolu Bölgesindedir (-%33,3). Bunun yanı sıra hastaneden taburcu edilen yeni hasta sayısındaki en fazla artış Ortadoğu Anadolu Bölgesindedir (%16,7). COVID-19 Günlük Durum Raporu, 16/11/2020, Türkiye"
    ],
    "age_data": {
      "men": {
        "< 2": 5,
        "2-4": 6,
        "5-14": 41,
        "15-24": 229,
        "25-49": 869,
        "50-64": 317,
        "65-79": 145,
        "80+": 30
      },
      "women": {
        "< 2": 4,
        "2-4": 6,
        "5-14": 44,
        "15-24": 258,
        "25-49": 828,
        "50-64": 335,
        "65-79": 160,
        "80+": 39
      },
      "all": {
        "< 2": 9,
        "2-4": 12,
        "5-14": 85,
        "15-24": 487,
        "25-49": 1697,
        "50-64": 652,
        "65-79": 305,
        "80+": 69
      }
    },
    "region_data": {
      "i̇stanbul": {
        "new_cases": 868,
        "compared_yesterday": -42,
        "compared_yesterday_percentage": -4.6
      },
      "bati_marmara": {
        "new_cases": 109,
        "compared_yesterday": -17,
        "compared_yesterday_percentage": -13.5
      },
      "ege": {
        "new_cases": 448,
        "compared_yesterday": -38,
        "compared_yesterday_percentage": -7.8
      },
      "dogu_marmara": {
        "new_cases": 504,
        "compared_yesterday": 7,
        "compared_yesterday_percentage": 1.4
      },
      "bati_anadolu": {
        "new_cases": 264,
        "compared_yesterday": 44,
        "compared_yesterday_percentage": 20
      },
      "akdeniz": {
        "new_cases": 280,
        "compared_yesterday": 28,
        "compared_yesterday_percentage": 11.1
      },
      "orta_anadolu": {
        "new_cases": 133,
        "compared_yesterday": 31,
        "compared_yesterday_percentage": 30.4
      },
      "bati_karadeniz": {
        "new_cases": 243,
        "compared_yesterday": 56,
        "compared_yesterday_percentage": 29.9
      },
      "dogu_karadeniz": {
        "new_cases": 91,
        "compared_yesterday": 23,
        "compared_yesterday_percentage": 33.8
      },
      "kuzeydogu_anadolu": {
        "new_cases": 62,
        "compared_yesterday": 0,
        "compared_yesterday_percentage": 0
      },
      "ortadogu_anadolu": {
        "new_cases": 96,
        "compared_yesterday": 11,
        "compared_yesterday_percentage": 12.9
      },
      "guneydogu_anadolu": {
        "new_cases": 218,
        "compared_yesterday": -11,
        "compared_yesterday_percentage": -4.8
      },
      "turkiye": {
        "new_cases": 3316,
        "compared_yesterday": 92,
        "compared_yesterday_percentage": 2.9
      }
    },
    "hospital_data": {
      "i̇stanbul": {
        "hospitalized_count": 158,
        "hospitalized_compared_yesterday_percentage": 4.6,
        "healed_count": 134,
        "healed_compared_yesterday_percentage": 7.2
      },
      "bati_marmara": {
        "hospitalized_count": 29,
        "hospitalized_compared_yesterday_percentage": -19.4,
        "healed_count": 17,
        "healed_compared_yesterday_percentage": -15
      },
      "ege": {
        "hospitalized_count": 89,
        "hospitalized_compared_yesterday_percentage": 14.1,
        "healed_count": 56,
        "healed_compared_yesterday_percentage": -8.2
      },
      "dogu_marmara": {
        "hospitalized_count": 117,
        "hospitalized_compared_yesterday_percentage": 17,
        "healed_count": 91,
        "healed_compared_yesterday_percentage": 2.2
      },
      "bati_anadolu": {
        "hospitalized_count": 72,
        "hospitalized_compared_yesterday_percentage": 2.9,
        "healed_count": 60,
        "healed_compared_yesterday_percentage": -4.8
      },
      "akdeniz": {
        "hospitalized_count": 66,
        "hospitalized_compared_yesterday_percentage": 0,
        "healed_count": 54,
        "healed_compared_yesterday_percentage": 10.2
      },
      "orta_anadolu": {
        "hospitalized_count": 31,
        "hospitalized_compared_yesterday_percentage": -29.5,
        "healed_count": 25,
        "healed_compared_yesterday_percentage": -7.4
      },
      "bati_karadeniz": {
        "hospitalized_count": 49,
        "hospitalized_compared_yesterday_percentage": 2.1,
        "healed_count": 35,
        "healed_compared_yesterday_percentage": 12.9
      },
      "dogu_karadeniz": {
        "hospitalized_count": 15,
        "hospitalized_compared_yesterday_percentage": 0,
        "healed_count": 12,
        "healed_compared_yesterday_percentage": -7.7
      },
      "kuzeydogu_anadolu": {
        "hospitalized_count": 22,
        "hospitalized_compared_yesterday_percentage": -33.3,
        "healed_count": 19,
        "healed_compared_yesterday_percentage": 5.6
      },
      "ortadogu_anadolu": {
        "hospitalized_count": 21,
        "hospitalized_compared_yesterday_percentage": -8.7,
        "healed_count": 28,
        "healed_compared_yesterday_percentage": 16.7
      },
      "guneydogu_anadolu": {
        "hospitalized_count": 58,
        "hospitalized_compared_yesterday_percentage": -10.8,
        "healed_count": 60,
        "healed_compared_yesterday_percentage": 9.1
      },
      "turkiye": {
        "hospitalized_count": 727,
        "hospitalized_compared_yesterday_percentage": -0.3,
        "healed_count": 591,
        "healed_compared_yesterday_percentage": 2.8
      }
    },
    "tests": 151741,
    "tests_compared_yesterday": 9263,
    "healed": 591,
    "healed_compared_yesterday": 16,
    "hospitalized": 727,
    "hospitalized_compared_yesterday": -2,
    "intubated": 115,
    "intubated_compared_yesterday": 17,
    "cases": 3316,
    "cases_compared_yesterday": 92,
    "tests_compared_percentage": 6.5,
    "healed_compared_percentage": 2.8,
    "hospitalized_compared_percentage": -0.3,
    "intubated_compared_percentage": 17.3,
    "cases_compared_percentage": 2.9,
    "date": 1605484800
  },
  .
  .
  .
]
```

# Türkçe Açıklama
Buradaki veri yazdığım korkunç regular expression ile pdf dosyalarından oluşturulmaktadır. Pdf dosyaları `mutool` ile text dosyalarına çevirilip, benim regular expression'ım uygulandıktan sonra birkaç düzenleme ile şu anda boyutu `753kb` olan bir json dosyası elde edilmektedir. İleride bu veriden sorgu yapma sistemi de eklemeyi planlıyom ancak şu anlık node.js üzerinden sadece o oluşturulan json dosyası sunulmaktadır.