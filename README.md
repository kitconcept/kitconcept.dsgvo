<div align="center">
    <img alt="kitconcept.dsgvo" width="200px" src="./docs/icon.png">
</div>

<h1 align="center">kitconcept.dsgvo</h1>

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)
[![PyPI - License](https://img.shields.io/pypi/l/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)
[![PyPI - Status](https://img.shields.io/pypi/status/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)


[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/kitconcept.dsgvo)](https://pypi.org/project/kitconcept.dsgvo/)

[![Code analysis checks](https://github.com/kitconcept/kitconcept.dsgvo/actions/workflows/code-analysis.yml/badge.svg)](https://github.com/kitconcept/kitconcept.dsgvo/actions/workflows/code-analysis.yml)
[![Tests](https://github.com/kitconcept/kitconcept.dsgvo/actions/workflows/tests.yml/badge.svg)](https://github.com/kitconcept/kitconcept.dsgvo/actions/workflows/tests.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/kitconcept/kitconcept.dsgvo)](https://github.com/kitconcept/kitconcept.dsgvo)
[![GitHub Repo stars](https://img.shields.io/github/stars/kitconcept/kitconcept.dsgvo?style=social)](https://github.com/kitconcept/kitconcept.dsgvo)


</div>

The General Data Protection Regulation ("GDPR" or "DSGVO" in German) is a regulation in EU law on data protection and privacy for all individuals within the European Union.

kitconcept.dsgvo implements the technical requirements that are necessary to be compliant with this regulation.

We strongly suggest to consult a Plone solution provider for the technical implications and a laywer for the legal implications of the DSGVO/GDPR.

Don't hesitate to contact us under info@kitconcept.com if you need assistance with implementing the DSGVO/GDPR.

## Features

- ✅ Opt-out banner for storing cookies
- ✅ Extensible registration form with user confirmation
- ✅ Contact form with information text
- ✅ Store username, date, time and IP address of the user on registration
- ✅ Export user data

### Registration Form

Default text (German):

    "Ich habe die [Link] Datenschutzerklärung und Widerrufhinweise[/Link] gelesen und akzeptiere diese."

### Contact Form

Default text (German):

    "Ihre Anfrage wird verschlüsselt per https an unseren Server geschickt. Sie erklären sich damit einverstanden, dass wir die Angaben zur Beantwortung Ihrer Anfrage verwenden dürfen. Hier finden Sie unsere [Link]Datenschutzerklärung und Widerrufhinweise[/Link]."

### User Export

As administrator you can call http://localhost:8080/Plone/export-users. This will return a CSV-File with the full name and username of all users of the portal.

## Examples

This add-on can be seen in action at the following sites:

- VHS-Ehrenamtsportal.de (https://vhs-ehrenamtsportal.de)
- Zeelandia Website (https://www.zeelandia.de)
- HU Berlin Excellence Initiative (https://www.alles-beginnt-mit-einer-frage.de)
- Talke Career Website (https://karriere.talke.com)


## Translations

This product has been translated into

- German


## Installation

Add `kitconcept.dsgvo` as a requirement of your package (in setup.py or setup.cfg).


## Compatibility

| Version | Plone 6.0 |  Plone 5.2 | Plone 5.1 | Plone 5.0 | Plone 4.3 |
| --- | --- | --- | --- | --- | --- |
| 2.x | ✅ | ✅ | | | |
| 1.x | | ✅ | ✅ | ✅ | ✅ |

## Contribute

- Issue Tracker: https://github.com/kitconcept/kitconcept.dsgvo/issues
- Source Code: https://github.com/kitconcept/kitconcept.dsgvo


## Support

If you are having issues, or you need assistance implementing the DSGVO / GDPR for your website, don't hesitate to contact us at info@kitconcept.com.


## Credits

Developed by:

[![kitconcept GmbH](https://kitconcept.com/logo.svg)](https://kitconcept.com/)

## License

The project is licensed under the GPLv2.
