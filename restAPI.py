import requests

response = requests.get('https://blogs.msdn.microsoft.com/powershell/feed/')

print(response.text)
