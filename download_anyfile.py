from urllib import request

sap_url = "https://spc40-emea.byd.sap.corp/sap/a1s/cam"


def downld_from_url (url):
    count = 1
    response = request.urlopen(url)
    csv = response.read()
    csv_text = str(csv)
    fw = open("resp.txt", "w")
    lines = csv_text.split("\\n")

    for line in lines:
        if count != 1:
            fw.write(line +"\n")

        count = 2

    fw.close()

downld_from_url(sap_url)