const functions = require("firebase-functions");
const {spawn} = require("child_process");
const path = require("path");

exports.api = functions.https.onRequest((req, res) => {
  const scriptPath = path.join(__dirname, "./app.py");
  const process = spawn("python", [scriptPath]);
  process.stdout.on("data", (data) => {
    res.status(200).send(data.toString());
  });
  process.stderr.on("data", (data) => {
    res.status(500).send(data.toString());
  });
});
