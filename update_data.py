import requests, re, json, os, shutil, locale
from datetime import datetime
from bs4 import BeautifulSoup as BS
from pprint import pprint
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

if not shutil.which("mutool"):
    print("[Uyari] Ayni klasore 'mutool'u atin ya da PATH degiskenine ekleyin.")
    exit(1)

if not os.path.exists("data_raw"):
    os.mkdir("data_raw")
if not os.path.exists("data_txt"):
    os.mkdir("data_txt")

BASE_URL = "https://covid19.saglik.gov.tr"
data = requests.get(BASE_URL)

REPORT_PAGE = BASE_URL + BS(data.content, "lxml").find("a", {"title": "COVID-19 Durum Raporu"}).get("href")
data = requests.get(REPORT_PAGE)

REPORT_LIST_PAGE = BASE_URL + BS(data.content, "lxml").select("div#ada_AltSayfaSolLink > a")[0].get("href")
data = requests.get(REPORT_LIST_PAGE)
data = [i.get("href") for i in BS(data.content, "lxml").select(".page-content-body > div > div > table tr > td > a[href*='tr.html']")]

files = map(lambda x: (str(x), re.match(r"^.*?(\d+-tr)", str(x)).groups()[0] + ".pdf"), data)
for report in files:
    dataPath = os.path.join("data_raw", report[1])
    txtPath = os.path.join("data_txt", report[1].replace("pdf", "txt"))
    if not os.path.exists(dataPath):
        with open(dataPath, "wb") as f:
            f.write(requests.get(BASE_URL + report[0]).content)
    if not os.path.exists(txtPath):
        os.system("cmd /C \"{} convert -o {}.txt {}\"".format(
            shutil.which("mutool"),
            txtPath.split(".")[0],
            dataPath
        ))

ageMap = [
    "< 2", 
    "2-4", 
    "5-14", 
    "15-24", 
    "25-49", 
    "50-64", 
    "65-79", 
    "80+", 
]

fieldMap = {
    "Erkek": "men",
    "Kadın": "women",
    "Toplam": "all",
}

regionMap = [
    "new_cases",
    "compared_yesterday",
    "compared_yesterday_percentage",
]

hospitalMap1 = [
    "hospitalized_count",
    "hospitalized_compared_yesterday_percentage",
    "healed_count",
    "healed_compared_yesterday_percentage",
]

hospitalMap2 = [
    "hospitalized_count",
    "healed_count",
]

def removeTurkish(text):
    t = text.replace("ı", "i")
    t = t.replace("ü", "u")
    t = t.replace("ö", "o")
    t = t.replace("ç", "c")
    t = t.replace("ğ", "g")
    t = t.replace("ş", "s")
    return t

# \uf0b7
# datetime.strptime("01/07/2020", "%d/%m/%Y")

blacklisted = {

}

allJson = []
for reportTxt in filter(lambda x: x != "29062020-tr.txt", os.listdir("data_txt")):
    f = open(os.path.join("data_txt", reportTxt), "r", encoding="utf-8")
    data = f.read()
    match = re.match(r"[\s\S]*?(?P<date>\d\d\/\d\d\/\d{4})[\s\S]*?Tablo 1:[\s\S]*?Test Sayısı \n(?P<tests>.*?) ?\n(?P<tests_compared_yesterday>.*?) ?\n(?P<tests_compared_percentage>.*?) ?\n[\s\S]*?(Vaka|Hasta) Sayısı \n(?P<cases>.*?) ?\n(?P<cases_compared_yesterday>.*?) ?\n(?P<cases_compared_percentage>.*?) ?\n[\s\S]*?Hasta Sayısı \n(?P<hospitalized>.*?) ?\n(?P<hospitalized_compared_yesterday>.*?) ?\n(?P<hospitalized_compared_percentage>.*?) ?\n[\s\S]*?Hasta Sayısı \n(?P<intubated>.*?) ?\n(?P<intubated_compared_yesterday>.*?) ?\n(?P<intubated_compared_percentage>.*?) ?\n[\s\S]*?Hasta Sayısı \n\n(?P<healed>.*?) ?\n(?P<healed_compared_yesterday>.*?) ?\n(?P<healed_compared_percentage>.*?) ?\n[\s\S]*?Günün Özeti.*?$(?P<summary>[\s\S]*?)Tablo 2:[\s\S]*?Göre Değişim.*?$(?P<region_data>[\s\S]*?)Şekil 1:[\s\S]*?Tablo 3:.*?$[\s\S]*?Yaş Grubu[\s\S]*?(?=Erkek|Kadın)(?P<age_data>[\s\S]*?)Şekil 2:[\s\S]*?Tablo 4:[\s\S]*İBBS-1(?P<hospital_data>[\s\S]*?Notlar:)", data, re.MULTILINE)
    matchData = match.groupdict()
    exportData = {
        "summary": [],
        "age_data": {},
        "region_data": {},
        "hospital_data": {},
    }
    for info in matchData["summary"].strip("\r\n 123456789").split("\uf0b7"):
        if info:
            val = "".join([i for i in info.split("\n") if i])
            val = re.sub(r"\s{2,}", " ", val).strip()
            exportData["summary"].append(val)
    for info in matchData["age_data"].strip().split("\n\n"):
        val = {}
        for i, item in enumerate(info.strip().split(" \n")[1:]):
            val[ageMap[i]] = int(item.replace(".", ""))
        exportData["age_data"][fieldMap[info.strip().split(" \n")[0]]] = val
    for info in re.findall(r"(^.* \n(.* \n){3})", matchData["region_data"], re.MULTILINE):
        val = {}
        for i, text in enumerate(info[0].strip().split(" \n")[1:]):
            if i < 2:
                val[regionMap[i]] = int(text.replace(".", ""))
            else:
                val[regionMap[i]] = float(text.replace(",", "."))
        exportData["region_data"][re.sub(r"\s", "_", removeTurkish(info[0].strip().split(" \n")[0].lower()))] = val
    hospital_data = re.findall(r"(^.* \n\d* \n(.* \n){1,3})", matchData["hospital_data"], re.MULTILINE)
    for info in hospital_data:
        val = {}
        if len(hospital_data) > 2:
            for i, text in enumerate(info[0].split(" \n")[1:-1]):
                if i % 2 == 0:
                    val[hospitalMap1[i]] = int(text.replace(".", ""))
                else:
                    val[hospitalMap1[i]] = float(text.replace(",", "."))
        else:
            for i, text in enumerate(info[0].split(" \n")[1:-1]):
                val[hospitalMap2[i]] = int(text.replace(".", ""))
        exportData["hospital_data"][re.sub(r"\s", "_", removeTurkish(info[0].split(" \n")[0].lower()))] = val
    for field in [
            "tests",
            "tests_compared_yesterday",
            "healed",
            "healed_compared_yesterday",
            "hospitalized",
            "hospitalized_compared_yesterday",
            "intubated",
            "intubated_compared_yesterday",
            "cases",
            "cases_compared_yesterday",
        ]:
        exportData[field] = int(matchData[field].replace(".", "")) if matchData[field] else 0
    for field in [
            "tests_compared_percentage",
            "healed_compared_percentage",
            "hospitalized_compared_percentage",
            "intubated_compared_percentage",
            "cases_compared_percentage",
        ]:
        exportData[field] = float(matchData[field].replace(",", "."))
    exportData["date"] = datetime.strptime(matchData["date"], "%d/%m/%Y").timestamp()
    allJson.append(exportData)

with open("29062020.json", "r", encoding="utf-8") as f:
    allJson.append(json.loads(f.read()))

allJson = sorted(allJson, key=lambda x: x["date"], reverse=True)

with open("export.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(allJson))