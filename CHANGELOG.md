## 2.0.1 (2022-08-09)

### Features

- Implement pip-based installations @ericof
  (#26)


# Changelog

<!--
   You should *NOT* be adding new change log entries to this file.
   You should create a file in the news directory instead.
   For helpful instructions, please see:
   https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
-->

## 2.0.1 (unreleased)

- Nothing changed yet.


## 2.0.0 (2021-09-24)

- Add support for Python 3.8 and 3.9. @tisto

- Drop support for Python 2.7 @tisto

- Drop support for Plone 4.3, 5.0, and 5.1 @tisto


## 1.3.0 (2020-06-03)

- Fixed deprecation warning on cgi.escape @ajung

- Add norwegian translation @espenmn


## 1.2.0 (2020-04-27)

- Add user export functionality. @rodfersou


## 1.1.1 (2020-04-02)

- Add bundle for Plone 5.2.x. @thomasmassmann


## 1.1.0 (2020-02-20)

- Make p.a.controlpanel dependency optional @rodfersou

- Plone 5.2 compatibility @rodfersou

- Python 3 compatibility @pbauer

- Add french translation @tiazma


## 1.0.0 (2018-11-17)

- Fix event subscriber fired by "adduser" command [#2](https://github.com/kitconcept/kitconcept.dsgvo/issues/2) @ajung


## 1.0.0a13 (2018-06-07)

- Fix broken msgstr @csenger


## 1.0.0a12 (2018-06-07)

- Fix translation in mailchimp form @csenger


## 1.0.0a11 (2018-05-28)

- Add zest.pocompile to the build and add the .mo files to the release. @sneridagh


## 1.0.0a10 (2018-05-28)

- Add missing CSS registry for Plone 5 from last fix @sneridagh


## 1.0.0a9 (2018-05-25)

- Fix the path on @@close-dsgvo-info view. @sneridagh


## 1.0.0a8 (2018-05-25)

- Fix weird profile behavior on reinstall (it wasn't uninstall/reinstalling at all). Transfer condition of the cookie banner showing to JS. @sneridagh


## 1.0.0a7 (2018-05-24)

- Fix CSS for non box-sizing: border-box; themes. @sneridagh


## 1.0.0a6 (2018-05-24)

- Add development status "alpha" to list classifiers. @timo

- Fix P4 registration form to correctly translate messages with that use ${portal_url} @csenger


## 1.0.0a5 (2018-05-24)

- Always open links to privacy policy in a new window. @sneridagh


## 1.0.0a4 (2018-05-24)

- Add plone.app.controlpanel to requirements to ensure permissions are configured @csenger

## 1.0.0a3 (2018-05-24)

- Add jbot override for contact-info.cpt @csenger

- Banner styling changes @csenger


## 1.0.0a2 (2018-05-23)

- Switch checkbox widget to use z3c.form.browser.checkbox to be compatible with Plone 5.0.x @csenger

- Add Plone4 support for banner and registration form @csenger


## 1.0.0a1 (2018-05-21)

- Initial release. @kitconcept
