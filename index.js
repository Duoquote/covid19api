const express = require("express"),
      fs = require("fs"),
      Sentry = require("@sentry/node"),
      app = express()

if (process.env.SENT_DSN) {
  Sentry.init({
    dsn: process.env.SENT_DSN
  });
}

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.requestHandler());
}


app.get("/", (req, res)=>{
  if (fs.existsSync("data.json")) {
    let data = fs.readFileSync("data.json");
    res.json(JSON.parse(data));
  } else {
    res.send("Loading data, please send request later...");
  }

})

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.errorHandler());
}


app.listen(3000, "localhost", ()=>{
  console.log(`Listening on 'localhost:3000'`);
})
