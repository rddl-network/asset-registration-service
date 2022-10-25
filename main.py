from fastapi import FastAPI
import subprocess

from pydantic import BaseModel

app = FastAPI()


class RegisterRequest(BaseModel):
    asset_id: str
    contract: dict


@app.post("/register_asset")
async def register_asset_id(request_body: RegisterRequest):
    register_asset_id_local(request_body.asset_id)
    register_asset_id_on_liquid(request_body.asset_id, request_body.contract)
    return request_body


def register_asset_id_local(asset_id: str):
    asset_id_string = 'Authorize linking the domain name lab.r3c.network to the Liquid asset ' + asset_id
    result = subprocess.run(['sudo', 'touch', '/var/www/html/.well-known/liquid-asset-proof-' + asset_id],
                            stdout=subprocess.PIPE)
    result = subprocess.run(['echo', '/var/www/html/.well-known/'], stdout=subprocess.PIPE)

    ps = subprocess.run(['echo', asset_id_string], check=True, capture_output=True)
    processNames = subprocess.run(['sudo', 'tee', '-a', '/var/www/html/.well-known/liquid-asset-proof-' + asset_id],
                                  input=ps.stdout, capture_output=True)


def register_asset_id_on_liquid(asset_id: str, contract: dict):
    register_request = ['curl', 'https://assets.blockstream.info/', '-H', 'Content-Type: application/json', '-d',
                        F'{{"asset_id":"{asset_id}","contract": {contract} }}']

    register_response = subprocess.run(register_request, stdout=subprocess.PIPE)
    if register_response.returncode == 0:
        print(register_response.stdout.decode('ASCII'))
    else:
        print(register_response.returncode)
