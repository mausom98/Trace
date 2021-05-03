"use strict";

const m = require("mithril");

const Dashboard = {
  view(vnode) {
    return [
      m(".header.text-center.mb-4", m("h4", "Welcome To Trace")),
      m(
        ".blurb",
        m(
          "p",
          m("em", "Trace"),
          " is a simple, supply chain application built",
          " using the Hyperledger Sawtooth blockchain platform. It maintains",
          " a distributed ledger that records the provenance and location",
          " of assets as they are transferred among various agents in a",
          " supply chain."
        ),
        m(
          "p",
          "To use ",
          m("em", "Trace"),
          ", create a new agent using the Log in/Sign up link on the navbar",
          " above. Once logged in, you will be able to register your",
          " produce on the blockchain, update its location, and transfer",
          " ownership of the work of produce to other registered agents."
        )
      ),
    ];
  },
};

module.exports = Dashboard;
