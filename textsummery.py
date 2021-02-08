# Ensure your pyOpenSSL pip package is up to date
# Example posting a text URL:

# Example directly sending a text string:

import requests

api_key = '84816503-a90d-4e4e-84fe-a4aab784f4c1'

def getDeepaiSummery(article_text):
  
  r = requests.post(
      "https://api.deepai.org/api/summarization",
      data={
          'text': article_text,
      },
      headers={'api-key': api_key}
  )
  response = r.json()
  #print(response)
  return(response['output'])