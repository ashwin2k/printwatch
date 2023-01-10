# Printwatch
Tired of running long tasks, but want to monitor from your phone? Try ***PRINTwatch***!

![PyPI](https://img.shields.io/pypi/v/printwatch) ![PyPI - License](https://img.shields.io/pypi/l/printwatch)
## Alpha version is now live on pip! 

Head to https://pypi.org/project/printwatch/ to install!

## Usage
Import the Redirector class using:

`from printwatch.redirection import Redirector`

Create a new method of `Redirector` and initialize it using:

`redirector=Redirector(identifier="Randomfd")
redirector.initialize()`

To redirect the output of a cell:

```
with redirector:
    print("Redirected output")
```

Redirected outputs will be placed in `logs/` folder. 