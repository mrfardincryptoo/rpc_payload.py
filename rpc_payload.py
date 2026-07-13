import json

def build_rpc_request(method, params, request_id=1):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": request_id
    }
    return json.dumps(payload, indent=2)

print(build_rpc_request("eth_blockNumber", []))
