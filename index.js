const axios = require("axios"),
      express = require("express"),
      CronJob = require("cron").CronJob,
      JSDOM = require("jsdom").JSDOM,
      Sentry = require("@sentry/node"),
      app = express()

if (process.env.SENT_DSN) {
  Sentry.init({
    dsn: process.env.SENT_DSN
  });
}


var dateDict = {
  "OCAK": 1,
  "ŞUBAT": 2,
  "MART": 3,
  "NİSAN": 4,
  "MAYIS": 5,
  "HAZİRAN": 6,
  "TEMMUZ": 7,
  "AĞUSTOS": 8,
  "EYLÜL": 9,
  "EKİM": 10,
  "KASIM": 11,
  "ARALIK": 12
}

var varDict = {
  "TOPLAM TEST SAYISI": "total_tests",
  "TOPLAM VAKA SAYISI": "total_cases",
  "TOPLAM VEFAT SAYISI": "total_deaths",
  "TOPLAM YOĞUN BAKIM HASTA SAYISI": "total_intense_care",
  "TOPLAM ENTUBE HASTA SAYISI": "total_incubated",
  "TOPLAM İYİLEŞEN HASTA SAYISI": "total_head"
}

var data;

function updateData() {
  axios.get("https://covid19.saglik.gov.tr/")
    .then(resp=>{
      var tmpData = {};
      eval([...resp.data.matchAll(/(?<data>var config = [\s\S]*? data: {[\s\S]*?}),\r\n.*options/gm)][0].groups.data + "}");
      let dailyData = config.data.labelsTooltip.reduce((obj, iter, i)=>{
        let tarih = dateDict[iter.match(/\d+ ([A-ZİÜĞÇŞÖ]+)/)[1]].toString() + "-" + config.data.labels[i].toString() + "-" + iter.match(/.* (\d+)/)[1];

        if (config.data.datasets[0].data[i]) {
          obj[tarih] = {
            date: new Date(tarih).getTime(),
            cases: config.data.datasets[0].data[i],
            deaths: config.data.datasets[1].data[i]
          }
        }
        return obj;
      }, {})
      tmpData.dailyData = dailyData;
      var dom = new JSDOM(resp.data).window.document;
      tmpData.detail = {};
      [...dom.querySelector("div[class='baslik-tablo']").nextElementSibling.querySelector("ul").children].forEach((elem)=>{
        let label = elem.textContent.match(/(?!\d)([A-ZİÜĞÇŞÖ]+)/g).join(" ");
        tmpData.detail[varDict[label]] = parseInt(elem.textContent.match(/(\d+\.?\d+|\d+)/g)[0].replace(".", ""));
      })
      data = tmpData;
    })
}

updateData();

var job = new CronJob("0 * * * *", updateData, null, true);

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.requestHandler());
}


app.get("/", (req, res)=>{
  res.json(data);
})

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.errorHandler());
}


app.listen(3000, "localhost", ()=>{
  console.log(`Listening on 'localhost:3000'`);
})
