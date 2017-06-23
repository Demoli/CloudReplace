import urllib3
import json


class Client(object):
    url = 'http://localhost:5000/replace'

    def replace(self, subject, search, replace, ignoreCase=False):
        request = urllib3.PoolManager()
        params = {'subject': subject, 'search': search, 'replace': replace}
        if ignoreCase:
            params['ignore_case'] = True
        body = json.dumps(params)
        response = request.request('POST', self.url, body=body)
        result = json.loads(response.data.decode('utf-8'))
        if response.status != 200:
            message = 'Could not perform replace operation'
            if 'error' in result.keys():
                message += ' :' + result['error']
            raise Exception(message)
        return result['result']


if __name__ == '__main__':
    replace = Client()
    result = replace.replace('Hello World!', 'hello', 'Goodbye', True)
    print(result)
