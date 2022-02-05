import requests


def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")

    contracts = []

    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts


conts = get_contracts()
print(conts)

upload_file_path = str("contracts") + ".txt"

# Write text to the file
file = open(upload_file_path, 'w')
for a in conts:
    file.write(a +'\n')
file.close()


