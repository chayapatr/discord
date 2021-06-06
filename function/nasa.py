from fetch import fetch

def pic():
  nasa = fetch("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
  print(nasa)
  return [nasa["hdurl"], nasa["explaination"]]