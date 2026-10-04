from fastapi.testclient import TestClient
from ragagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'answer with tools', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["tools_run"] == ["retrieve", "call_tool"]
    refused = client.post("/agent/run", json={"goal": 'apply the change'}).json()
    assert refused["refused"] is True
