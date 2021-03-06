"use strict";

const m = require("mithril");

const api = require("../services/api");
const forms = require("../components/forms");

/**
 * The Form for authorizing an existing agent.
 */
const LoginForm = {
  view(vnode) {
    const setter = forms.stateSetter(vnode.state);

    return m(".login-form", [
      m("img.mb-4", {
        src: "https://firebasestorage.googleapis.com/v0/b/genesis-d3c48.appspot.com/o/undraw_Login_re_4vu2.png?alt=media&token=6ec1560b-b018-4f68-bd6b-a8ac5b6b723f",
        height: "100px",
        width: "200px",
      }),
      m(
        "form",
        {
          onsubmit: (e) => {
            e.preventDefault();
            const credentials = {
              public_key: vnode.state.publicKey,
              password: vnode.state.password,
            };
            api
              .post("authentication", credentials)
              .then((res) => {
                api.setAuth(res.authorization);
                m.route.set("/");
              })
              .catch(api.alertError);
          },
        },
        m("legend", "Login Agent"),
        forms.textInput(setter("publicKey"), "Public Key"),
        forms.passwordInput(setter("password"), "Password"),
        m(
          "container.text-center",
          "Or you can ",
          m(
            'a[href="/signup"]',
            { oncreate: m.route.link },
            "create a new agent"
          )
        ),
        m(
          ".form-group",
          m(
            ".row.justify-content-end.align-items-end",
            m(
              "col-2",
              m(
                "button.btn.btn-primary",
                { "data-toggle": "modal", "data-target": "#modal" },
                "Login"
              )
            )
          )
        )
      ),
    ]);
  },
};

module.exports = LoginForm;
