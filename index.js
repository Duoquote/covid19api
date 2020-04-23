const express = require("express"),
      fs = require("fs"),
      Sentry = require("@sentry/node"),
      path = require("path"),
      app = express()

const port = process.env.PORT || 3000;

if (process.env.SENT_DSN) {
  Sentry.init({
    dsn: process.env.SENT_DSN
  });
}

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.requestHandler());
}


app.get("/", (req, res)=>{
  res.sendFile(path.join(__dirname, "data.json"))
})

if (process.env.SENT_DSN) {
  app.use(Sentry.Handlers.errorHandler());
}


app.listen(port, ()=>{
  console.log(`Listening on '${port}'`);
})
