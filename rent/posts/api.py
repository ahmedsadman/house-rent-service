import requests
import json


class Api(object):
    base_url = 'http://localhost:7000/caas/'
    response = None

    def refine_data(self, res, data):
        # get the expected data from json response
        if self.execute_success():
            return res[data]
        else:
            return None

    def execute_success(self):
        # returns if the last request was successful
        if self.response != 200:
            return False
        return True


class Caas(Api):

    def __init__(self, password, subscriberId, applicationId):
        self.applicationId = applicationId
        self.password = password
        self.subscriberId = subscriberId
        self.baseData = {
            'applicationId': self.applicationId,
            'password': self.password,
            'subscriberId': self.subscriberId,
            'paymentInstrumentName': 'Mobile Account'
        }

    def get_balance(self):
        url = self.base_url + 'balance/query'
        res = requests.post(url, json=self.baseData)
        self.response = res.status_code
        data = res.json()
        return self.refine_data(data, 'chargeableBalance')

    def direct_debit(self, tran_id, amount):
        url = self.base_url + 'direct/debit'
        jsonData = self.baseData
        jsonData['externalTrxId'] = tran_id
        jsonData['amount'] = amount

        res = requests.post(url, json=jsonData)
        self.response = res.status_code
        data = res.json()
        print(data)
        success = self.refine_data(data, 'statusDetail')

        if 'Success' in success:
            print('Direct debit successful')
            return True
        else:
            print('Error occured during debit')
            return False


# req = Caas('password', '8801866742387', 'APP_000001')
# print(req.get_balance())
# print(req.execute_success())
# print(req.direct_debit('25601', '50'))
