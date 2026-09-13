# Contributing

Read the Vistoda family [contribution guide](https://github.com/luigibarretta/vistoda-home-assistant/blob/main/CONTRIBUTING.md)
before changing provider or discovery contracts.

This repository owns the Home Assistant app catalog, app options, translations,
installation guides and tested release matrix. Provider implementations belong
in their Ring, Blink or EZVIZ repositories.

Run `python scripts/check.py` and `python -m unittest discover -s tests -p
'test_*.py'`. A version change must update app configuration, changelog and
[COMPATIBILITY.md](COMPATIBILITY.md) together.
