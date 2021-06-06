from fetch import fetch

def crypt():
  coin = fetch("https://static.coinpaper.io/api/coins.json")
  text = ""
  for i in range(3):
    text += coin[i]["symbol"] + ": " + str(coin[i]["price"])+  " USTD\n"
  return text