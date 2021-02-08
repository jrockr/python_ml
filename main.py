import trafilatura
from textsummery import getDeepaiSummery
from newsummerizer import summery
url = 'https://www.iol.co.za/news/world/south-africa-faces-widespread-scepticism-over-vaccine-safety-86536d3f-64fb-5c63-a1fa-2e2db2b66cef'

downloaded = trafilatura.fetch_url(url)
extract_val = trafilatura.extract(downloaded)

print(extract_val)
print("-----------------------summery----------------")
print(getDeepaiSummery(extract_val))

print("-----------------------summery2----------------")
print(summery())