from tsuru_autoscale.client.instance import InstanceClient
from tsuru_autoscale.client.event import EventClient
from tsuru_autoscale.client.wizard import WizardClient
from tsuru_autoscale.client.datasource import DatasourceClient



class Client(object):
    def __init__(self, target, token):
        self.instance = InstanceClient(target, token)
        self.event = EventClient(target, token)
        self.wizard = WizardClient(target, token)
        self.datasource = DatasourceClient(target, token)