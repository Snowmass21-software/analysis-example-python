# Pure-Python Analysis Example

This repository provides an example analysis script for processing the Delphes outputs produced by the Snowmass MC Prod task force.

## Installation

Using a python3 installation in a virtual environment, e.g.

```
python3 -m venv myenv
source myenv/bin/activate
```

you can install the requirements via

```
python -m pip install -r requirements.txt
```

## Running

Simply run

```
python analysis.py
```

which outputs a histogram using `histoprint`. For one Delphes file, one sees

```
 0.00e+00 _                             4.68e+04 ╷
 2.50e+01 _███████████████████████████████████████
 5.00e+01 _█
 7.50e+01 _
 1.00e+02 _
 1.25e+02 _
 1.50e+02 _
 1.75e+02 _
 2.00e+02 _
 2.25e+02 _
 2.50e+02 _
 2.75e+02 _
 3.00e+02 _
 3.25e+02 _
 3.50e+02 _
 3.75e+02 _
 4.00e+02 _
 4.25e+02 _
 4.50e+02 _
 4.75e+02 _
 5.00e+02 _
 5.25e+02 _
 5.50e+02 _
 5.75e+02 _
 6.00e+02 _
 6.25e+02 _
 6.50e+02 _
 6.75e+02 _
 7.00e+02 _
 7.25e+02 _
 7.50e+02 _
 7.75e+02 _
 8.00e+02 _
 8.25e+02 _
 8.50e+02 _
 8.75e+02 _
 9.00e+02 _
 9.25e+02 _
 9.50e+02 _
 9.75e+02 _
 1.00e+03 _
```

which takes about 2 seconds to run.
