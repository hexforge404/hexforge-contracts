const fs = require("fs");
const path = require("path");

function schemaPath(name) {
  return path.resolve(__dirname, "..", "..", "schemas", "common", name);
}

function loadSchema(name) {
  return JSON.parse(fs.readFileSync(schemaPath(name), "utf8"));
}

module.exports = { schemaPath, loadSchema };
