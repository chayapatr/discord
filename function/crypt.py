from fetch import fetch

def btc():
  coin = fetch(" https://api.coindesk.com/v1/bpi/currentprice.json")
  # coin = coin[0]
  text = ""
  return coin["bpi"]["USD"]["rate"]