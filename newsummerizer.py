import requests

url = "https://news-summarizer.p.rapidapi.com/summarize"

def summery():

  payload = "{\r\n    \"input_link\": \"https://www.iol.co.za/news/world/south-africa-faces-widespread-scepticism-over-vaccine-safety-86536d3f-64fb-5c63-a1fa-2e2db2b66cef\",\r\n    \"input_text\": \"\"\r\n}"
  headers = {
      'content-type': "application/json",
      'x-rapidapi-key': "19fed258c2mshf61ab28502a74e9p12f95ajsn9bee8981b258",
      'x-rapidapi-host': "news-summarizer.p.rapidapi.com"
      }

  response = requests.request("POST", url, data=payload, headers=headers)

  return(response.text)