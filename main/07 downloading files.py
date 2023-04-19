import requests

# url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe"
# r = requests.get(url)
# fp = open("winrar.exe", "wb")
# fp.write(r.content)
# fp.close()

url = "https://assets.mixkit.co/active_storage/sfx/166/166.wav"
r = requests.get(url)
fp = open("sound.wav", "wb")
fp.write(r.content)
fp.close()