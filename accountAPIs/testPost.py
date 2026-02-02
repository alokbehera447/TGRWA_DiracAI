import os


def send_otp_sms(numbers: str, variables_values: str):
    import requests

    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"variables_values={variables_values}&route=otp&numbers={numbers}"
    headers = {
        "authorization": os.environ.get("FAST2SMS_AUTHORIZATION", ""),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }

    return requests.request("POST", url, data=payload, headers=headers)


if __name__ == "__main__":
    send_otp_sms(numbers="8790278025", variables_values="12332")
