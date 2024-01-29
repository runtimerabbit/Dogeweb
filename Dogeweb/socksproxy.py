import requests
torport = 9150
proxies = {
    'http': "socks5h://localhost:{}".format(torport),
    'https': "socks5h://localhost:{}".format(torport)
}
search = requests.get('http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/', proxies=proxies).text
print(search)
with open('test.html', 'w') as f:
    f.writelines(search)