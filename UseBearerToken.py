import http.client

conn = http.client.HTTPSConnection("sandbox-api.dexcom.com")

headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxZjliNzc3OC1kNTNhLTRiY2QtOWRkYi0zOWVhOGQ1MGQ3ZTQiLCJhdWQiOiJodHRwczovL3NhbmRib3gtYXBpLmRleGNvbS5jb20iLCJzY29wZSI6WyJlZ3YiLCJjYWxpYnJhdGlvbiIsImRldmljZSIsImV2ZW50Iiwic3RhdGlzdGljcyIsIm9mZmxpbmVfYWNjZXNzIl0sImlzcyI6Imh0dHBzOi8vc2FuZGJveC1hcGkuZGV4Y29tLmNvbSIsImV4cCI6MTU5NzkxODQ4MiwiaWF0IjoxNTk3OTExMjgyLCJjbGllbnRfaWQiOiJrT0p1OVRoMmZza2FWZUpXc1NHeHNjSkZQQmhCVTJCMyJ9.vKPTP9VFEBhszN5OlAzdcZZVyi1jxhoxFsH87QOwE4oC6E6krd-3qCaon77f2PfNP9kbX3SDjVeo1oLDcdN1oAVQvzJ24FeTOTEeQPSqmxJ0sdJKSlHLhx35cV2MSfaDIBY0CcEyY3r1XrWc21HhJdrg_Lu950Uk5NNLfuLqb3bk0-xzNJgr0BXho3IoHDJT33HRKPXHCUBQvCrJ8qjQt0WJzfY8EKcoX5FrlNqoqWJMaN1u3FyD54eTDiHR0t7dxMBsYi9u0b_KJmmgnRC4zZ4S2gIxBaqP_acuIUEQkXA-r9shIoqLOhq2pmNJPz5fGYcrZzPgvhCLQfSUG9Nubw"
    }

conn.request("GET", "/v2/users/self/egvs?startDate=2017-06-16T15:30:00&endDate=2017-06-16T15:45:00", headers=headers)

res = conn.getresponse()
data = res.read()

dec_data = data.decode("utf-8")

print(dec_data)