const Ajv = require("ajv");

function validateJson(data, schema) {
  const ajv = new Ajv({ allErrors: true, strict: false });
  const ok = ajv.validate(schema, data);
  if (!ok) {
    const err = new Error("Schema validation failed");
    err.details = ajv.errors;
    throw err;
  }
}

module.exports = { validateJson };
