# Printwatch
Tired of running long tasks? Try ***PRINTwatch***!

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

Redirected outputs will be placed in `logs/` folder. You can also use the webserver at `http://127.0.0.1:5001` to monitor the logs locally (will add support for hosted webservers soon).

## Changelogs
### `0.0.7-alpha`
- Added chunk/lazy reading to big log files!
- Improved UI