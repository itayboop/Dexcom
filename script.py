import http.client
import webbrowser
import json


def get_tokens(client_secret, client_id, redirect_uri, auth_code):
    conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")
    grant_type = "authorization_code"
    dexcom_url = "https://sandbox-api.dexcom.com/v2/oauth2/"
    auth_url = \
        f"{dexcom_url}login?client_id=kOJu9Th2fskaVeJWsSGxscJFPBhBU2B3&redirect_uri={redirect_uri}&response_type=code" \
        f"&scope=offline_access"

    print("Running Auth...")
    webbrowser.open_new(auth_url)

    payload = f"client_secret={client_secret}&client_id={client_id}&code={auth_code}&grant_type={grant_type}&redirect_uri={redirect_uri}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    conn.request("POST", "/v2/oauth2/token", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data_dict = json.loads(data)

    print(data_dict)


def token_refresh(client_secret, client_id, refresh_token, redirect_uri):
    conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

    payload = f"client_secret={client_secret}&client_id={client_id}&refresh_token={refresh_token}&grant_type=refresh_token&redirect_uri={redirect_uri}"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    conn.request("POST", "/v2/oauth2/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    data_dict = json.loads(data)

    return data_dict


def use_bearer_token(bearer_token):
    conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

    headers = {
        'authorization': f"Bearer {bearer_token}"
    }

    conn.request("GET", "/v2/users/self/egvs?startDate=2017-06-16T15:30:00&endDate=2017-06-16T15:45:00",
                 headers=headers)

    res = conn.getresponse()
    data = res.read()

    dec_data = data.decode("utf-8")

    print(dec_data)


def main():
    bearer = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxZjliNzc3OC1kNTNhLTRiY2QtOWRkYi0zOWVhOGQ1MGQ3ZTQiLCJhdWQiOiJodHRwczovL3NhbmRib3gtYXBpLmRleGNvbS5jb20iLCJzY29wZSI6WyJlZ3YiLCJjYWxpYnJhdGlvbiIsImRldmljZSIsImV2ZW50Iiwic3RhdGlzdGljcyIsIm9mZmxpbmVfYWNjZXNzIl0sImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hcGkuZGV4Y29tLmNvbSIsImV4cCI6MTU5ODgxMjUwMCwiaWF0IjoxNTk4ODA1MzAwLCJjbGllbnRfaWQiOiJrT0p1OVRoMmZza2FWZUpXc1NHeHNjSkZQQmhCVTJCMyJ9.Gsz6m3oJkLW-EryyguHaaGzFAsi5jYxfd2H3-6waHC2cmnQC7uKzkBu38F_XfN8CbpZBh3q-VS76g4izAG9AY7rC7RSo4Dk0yB-72u7iLNv-kwckHqC3fRI8MlgSzfFBbUB4GutBeYPzRoB5uWO6KxpsRFpS2T5or-lkqybhED_BBZD0R-ulkQXmkuSvxnyrWpN5NdcseqFzLZdCaXQ_jPw4YYwdbyPZQ5gT8VX0si8wB9OcGtVaEPeCn8Dm9VjNVKENQghdgBnm6aHd6EZqtIKGapc-FCywF810HfuAAdHQza3AqqaI9Q5Q8z7EVd4vuXTd3VtVP1eeCTZh04GOZg'
    info = token_refresh('MOIzlmVBXYVSzTXT', 'kOJu9Th2fskaVeJWsSGxscJFPBhBU2B3', 'b8c903b6fcb682672554868223090c83', 'http://89.139.235.114/')
    use_bearer_token(info['access_token'])
    use_bearer_token(bearer)


if __name__ == '__main__':
    main()
