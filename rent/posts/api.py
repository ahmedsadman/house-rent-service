import requests
import json


class Api(object):
    base_url = 'http://developer.bdapps.com/'
    response = None

    def __init__(self):
        self.applicationId = 'APP_005956'
        self.password = '18815b346f736b3e6223404d2a82afc9'

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

    def __init__(self, subscriberId):
        super().__init__()
        self.subscriberId = subscriberId
        self.baseData = {
            'applicationId': self.applicationId,
            'password': self.password,
            'subscriberId': self.subscriberId,
            'paymentInstrumentName': 'Mobile Account'
        }
        self.base_url += 'caas/'

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


class Subscribe(Api):

    def __init__(self, subscriberId):
        super().__init__()
        self.baseData = {
            'applicationId': self.applicationId,
            'password': self.password,
            'subscriberId': subscriberId,
        }
        self.base_url += 'subscription/'

    def get_status(self):
        url = self.base_url + 'getstatus'
        res = requests.post(url, json=self.baseData)
        self.response = res.status_code
        print(self.response, url, self.baseData)
        data = res.json()
        print(data)
        status = self.refine_data(data, 'subscriptionStatus')

        if 'REGISTERED' in status:
            print('SUBSCRIBED')
            return True
        else:
            print('SUBSCRIBED')
            return False

    def opt_in(self):
        url = self.base_url + 'send'
        jsonData = self.baseData
        jsonData['action'] = 1
        res = requests.post(url, json=jsonData)
        print(url)
        self.response = res.status_code
        data = res.json()
        status = self.refine_data(data, 'statusDetail')

        if 'Success' in status:
            print('Opted In')
            return True
        else:
            return False

    def opt_out(self):
        url = self.base_url + 'send'
        jsonData = self.baseData
        jsonData['action'] = 0
        res = requests.post(url, json=jsonData)
        self.response = res.status_code
        data = res.json()
        status = self.refine_data(data, 'statusDetail')

        if 'Success' in status:
            print('Opted Out')
            return True
        else:
            return False

# req = Caas('8801521423582')
# print(req.get_balance())
# print(req.execute_success())
# print(req.direct_debit('25601', '50'))
# print(req.response)

# req = Subscribe('tel:8801521423582')
# req.opt_out()
