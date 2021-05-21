"use strict";

const m = require("mithril");
const _ = require("lodash");

const stateSetter = (state) => (key) => (value) => {
  state[key] = value;
};
const group = (label, ...contents) => {
  return m(".form-group", [m("label", label), contents]);
};

const field = (onValue, attrs = null) => {
  const defaults = {
    required: true,
    oninput: m.withAttr("value", onValue),
  };

  return m("input.form-control.mb-1", _.assign(defaults, attrs));
};

const input = (type, onValue, label, required = true) => {
  return group(label, field(onValue, { type, required }));
};

const textInput = _.partial(input, "text");
const passwordInput = _.partial(input, "password");

module.exports = {
  group,
  field,
  stateSetter,
  textInput,
  passwordInput,
};
