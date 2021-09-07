from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']

class Client(object):
    def __init__(self, credentials, view):
        sac = ServiceAccountCredentials.from_json_keyfile_name(
            credentials, SCOPES)
        self.client = build('analyticsreporting', 'v4', credentials=sac)
        self.view = view
        
    def get_report(self, daterange, dimensions, metrics):
        request = {
            'reportRequests': [
            {
                'viewId': self.view,
                'dateRanges': [daterange],
                'metrics': [{'expression': 'ga:'+m} for m in metrics],
                'dimensions': [{'name': 'ga:'+d} for d in dimensions]
            }]
        }
        
        return analytics.reports().batchGet(request).execute()
