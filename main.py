from censys.search import CensysCertificates
import csv
from os import getenv
from dotenv import load_dotenv

def call_censys(id, secret):
    c = CensysCertificates(api_id=id, api_secret=secret)
    fields = ["parsed.fingerprint_sha256", "parsed.validity.start", "parsed.validity.end"]
    certs = c.search("parsed.names: censys.io and tags: trusted", fields)
    with open("censys_sha256_records.csv", "w") as csvfile:
        csv_fields = ["fingerprintSha256",
                      "validityStart", "validityEnd"]
        writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
        writer.writeheader()

        for certificate in certs:
            writer.writerow({
                "fingerprintSha256": certificate["parsed.fingerprint_sha256"],
                "validityStart": certificate["parsed.validity.start"],
                "validityEnd": certificate["parsed.validity.end"]
            })
    print("Successfully generated censys_sha256_records.csv")


if __name__ == '__main__':
    load_dotenv()
    ID = getenv("CENSYS_ID")
    SECRET = getenv("CENSYS_SECRET")
    if not (ID and SECRET):
        raise KeyError(
            "Please add your Censys account Api_ID and Secret in the .env file (Can be found at: "
            "https://search.censys.io/account/api)")
    call_censys(ID, SECRET)

