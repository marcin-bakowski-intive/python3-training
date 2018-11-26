import requests

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {"user-agent": "dummy-test"}
response = requests.get('https://httpbin.org/get', params=payload, headers=headers)
print(response)
print("Response status code: %s" % response.status_code)
print("Response headers %s" % response.headers)

# Get individual header like an item from python dict
print("Content-type: %s" % response.headers['content-type'])
print("Raw binary content: ")
print(response.content)

# if you're sure that response is json serialized you can use short-cut method to deserialize it to python dict()
print("Content as json: ")
print(response.json())
print("Response time %s" % response.elapsed)


# post json content
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', json=payload)
print(response)
print(response.json())
print("Response time %s" % response.elapsed)
# if response is ok then raise_for_status won't raise an error
response.raise_for_status()


# check response status
response = requests.post('https://httpbin.org/get')
print(response)
print("Response headers %s" % response.headers)
if not response.ok:
    print("response status is %s, error will be raised" % response.status_code)
response.raise_for_status()
