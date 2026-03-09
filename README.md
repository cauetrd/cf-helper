# Codeforces Helper

A small toolkit to help with Codeforces Div contests.
It automatically extracts sample tests from the downloaded contest page, generates input/output files, creates a file for each problem, and provides a script to compile and test solutions quickly.

## Features

- Parse downloaded Codeforces contest HTML and extract sample tests
- If wanted, creates a X.cpp file for each problem
- Can also run based on a single solution file if prefered
- Configurable paths and compiler options
- Runs solutions on sample cases and gives veredict

---

# How to Use

- Clone this repository to a folder of your preference
- Adjust paths and other configurations on the config.txt file
- When the contest starts:
  - Download the complete problem page e.g. (https://codeforces.com/contest/2205/problems) to the location you defined in config
  - Run `setup.py`
  - If the mode is set to `MULTIFILE`, a copy of your template will be created for each problem should be created in the dir you defined in config
  - If the mode is set to `SINGLEFILE`, it is expected that all solutions will be written on a single file specified in config
  - When testing samples, run `runsamples.sh X` to test problem X
  - Depending on the mode, X.cpp or singlefile.cpp will be compiled with the flags set on config to `/run`

---

# Sugested Aliases

- `alias gen='python Your/Absolute/Path/cf.py'`
- `alias rs='Your/Absolute/Path/runsamples.sh'`

Or something like that. These are recommended for even praticity

# Requirements

- Python 3
- `beautifulsoup4`

Install dependencies:

```
pip install beautifulsoup4
```

---

# License

This project is intended for personal competitive programming use. Feel free to modify and adapt it to your workflow.
