import http.client

conn = http.client.HTTPSConnection("api.dexcom.com")

payload = "client_secret=MOIzlmVBXYVSzTXT&client_id=kOJu9Th2fskaVeJWsSGxscJFPBhBU2B3&code=0dc2734d51ad78778c917b40097366a3&grant_type=authorization_code&redirect_uri=http://46.117.37.91/"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

conn.request("POST", "/v2/oauth2/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))