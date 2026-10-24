import json, sys
from client import CrossBorderDutyCustomsTariffCalculatorClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "customs-tariff-calculator", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "calculate_customs_tariff", "description": "Calculates cross-border e-commerce customs duty, import VAT, and landed cost."}]}}
    elif method == "tools/call":
        client = CrossBorderDutyCustomsTariffCalculatorClient()
        res = client.calculate_customs_tariff()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = CrossBorderDutyCustomsTariffCalculatorClient()
        print(json.dumps(client.calculate_customs_tariff(), indent=2))
