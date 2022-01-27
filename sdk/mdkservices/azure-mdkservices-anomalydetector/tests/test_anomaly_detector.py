import math
import os
import json
import functools

from devtools_testutils import AzureTestCase, PowerShellPreparer
from azure.mdkservices import anomalydetector
from azure.mdkservices.anomalydetector import AnomalyDetectorClient
from azure.core.credentials import AzureKeyCredential

AnomalyDetectorPreparer = functools.partial(
    PowerShellPreparer, 'anomalydetector',
    anomalydetector_endpoint="fake_resource.servicebus.windows.net/",
    anomalydetector_apikey="fakeZmFrZV9hY29jdW50X2tleQ=="
)

def arrayIsClose(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    t = [i for i in range(len(a)) if not math.isclose(a[i], b[i], rel_tol=1e-6)]
    return len(t) == 0

class TestAnomalyDetector(AzureTestCase):

# Start with any helper functions you might need, for example a client creation method:
    def create_test_client(self, endpoint, apikey):
        credential = AzureKeyCredential(apikey)
        client = self.create_client_from_credential(AnomalyDetectorClient, credential=credential, endpoint=endpoint)
        return client

# Write your tests
    @AnomalyDetectorPreparer()
    def test_client_creation(self, anomalydetector_endpoint, anomalydetector_apikey):
        client = self.create_test_client(anomalydetector_endpoint, anomalydetector_apikey)
        assert client is not None

    # Test for DetectEntireSeries
    @AnomalyDetectorPreparer()
    def test_detect_entire_series(self, anomalydetector_endpoint, anomalydetector_apikey):
        client = self.create_test_client(anomalydetector_endpoint, anomalydetector_apikey)
        with open("tests/examples/EntireDetect.json") as f:
            example = json.load(f)
        ret = client.detect_entire_series(body=example["parameters"]["body"])
        # structure
        assert ret.keys() == example["responses"]["200"]["body"].keys()
        # isAnomaly
        assert ret['isAnomaly'] == example["responses"]["200"]["body"]['isAnomaly']
        # expectedValues
        assert len(ret['expectedValues']) == len(example["responses"]["200"]["body"]['expectedValues'])
        # assert arrayIsClose(ret['expectedValues'], example["responses"]["200"]["body"]['expectedValues'])

    # Test for DetectLastPoint
    @AnomalyDetectorPreparer()
    def test_detect_last_point(self, anomalydetector_endpoint, anomalydetector_apikey):
        client = self.create_test_client(anomalydetector_endpoint, anomalydetector_apikey)
        with open("tests/examples/LastDetect.json") as f:
            example = json.load(f)
        ret = client.detect_last_point(body=example["parameters"]["body"])
        # structure
        assert ret.keys() == example["responses"]["200"]["body"].keys()
        # isAnomaly
        assert ret['isAnomaly'] == example["responses"]["200"]["body"]['isAnomaly']
        # period
        assert ret['period'] == example["responses"]["200"]["body"]['period']
        # suggestedWindow
        assert ret['suggestedWindow'] == example["responses"]["200"]["body"]['suggestedWindow']
        # expectedValue
        # assert math.isclose(ret['expectedValue'], example["responses"]["200"]["body"]['expectedValue'], rel_tol=1e-6)
        # lowerMargin
        # assert math.isclose(ret['lowerMargin'], example["responses"]["200"]["body"]['lowerMargin'], rel_tol=1e-6)
        # upperMargin
        # assert math.isclose(ret['upperMargin'], example["responses"]["200"]["body"]['upperMargin'], rel_tol=1e-6)

    # Test for DetectChangePoint
    @AnomalyDetectorPreparer()
    def test_detect_change_point(self, anomalydetector_endpoint, anomalydetector_apikey):
        client = self.create_test_client(anomalydetector_endpoint, anomalydetector_apikey)
        with open("tests/examples/ChangePointDetect.json") as f:
            example = json.load(f)
        ret = client.detect_change_point(body=example["parameters"]["body"])
        # structure
        assert ret.keys() == example["responses"]["200"]["body"].keys()
        # assert ret['isChangePoint'] == example["responses"]["200"]["body"]['isChangePoint']
