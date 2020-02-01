<div align="center">

# Linguist

View the language breakdown of your entire GitHub account.

[![Build Status](https://travis-ci.org/Justintime50/linguist.svg?branch=master)](https://travis-ci.org/Justintime50/linguist)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

<img src="assets/showcase.png">

</div>

GitHub displays beautiful language breakdowns on each repo on their platform; however, they do not show your entire language breakdown anywhere.

Linguist can return the language breakdown of your personal repos or all repos you have access to individually via the command line, then Linguist will build a customized pie chart breakdown of your overall language usage across all repos. Configure some settings and quickly find out what languages you use the most!

## Install

```bash
pip install -r requirements.txt
```

## Usage

Add your GitHub token to the `G` variable in the `linguist.py` file and run the following command:

```bash
python linguist.py
```

The repos you'd like to include can be configured by changing the `REPO_TYPE` variable in the `linguist.py` file.
