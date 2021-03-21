import http.client

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")
client_secret = 'MOIzlmVBXYVSzTXT'
client_id = 'kOJu9Th2fskaVeJWsSGxscJFPBhBU2B3'
refresh_token = 'b8c903b6fcb682672554868223090c83'
redirect_uri = 'http://46.117.37.91/'

payload = f"client_secret={client_secret}&client_id={client_id}&refresh_token={refresh_token}&grant_type=refresh_token&redirect_uri={redirect_uri}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))