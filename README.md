# CensysAssessment
This is an assessment given by Censys for the role of  Censys Summer 2023 Intern

script for getting validity dates and the SHA256 fingerprint of certificates with the query- parsed.names: censys.io and tags: trusted.

## Install

```bash
pip install -r requirements.txt
```

## Run
Create a file name `.env`
Add the Censys API ID and secret found under [My Account](https://censys.io/account/api) to `.env` as follows:
```bash
export CENSYS_ID="<Your apid id>"
export CENSYS_SECRET="<your api secret>"
```
Run the main script (with your python version):
```bash
python main.py
```
