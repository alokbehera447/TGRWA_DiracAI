import requests

url = "https://www.fast2sms.com/dev/bulkV2"

otpNum=23442
payload = "variables_values=12332&route=otp&numbers=8790278025"
headers = {
    'authorization': "CqDtUWF4wjpv5brzxXPlaOic2IZS6GYkNLdy7hKfJM9A10BguEDiG0mLEcxyKnApUqMaCu7Jl1eRbF9o",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
