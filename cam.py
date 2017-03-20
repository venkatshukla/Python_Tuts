from urllib import request

sap_url = "https://spc40-emea.byd.sap.corp/sap/a1s/cam"


def downld_from_url (url):

    response = request.urlopen(url)
    csv = response.read()
    csv_text = str(csv)
    print(csv_text)

downld_from_url(sap_url)