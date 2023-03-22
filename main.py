import json
import subprocess
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from decouple import config

ASSET_REG_URL: str = config("ASSET_REG_URL", default="https://assets.blockstream.info")
LOCAL_STORAGE_LOCATION: str = config("LOCAL_STORAGE_LOCATION", default="/var/www/html")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RegisterRequest(BaseModel):
    asset_id: str
    contract: dict


@app.get("/health")
def health():
    return {"health": "ok"}


@app.post("/register_asset", status_code=201)
async def register_asset_id(request_body: RegisterRequest):
    print(f" request_body: { request_body }")
    print(f" TYPE : {isinstance(request_body.contract, dict)}")
    print(f" TYPE : {isinstance(request_body.contract, str)}")
    if register_asset_id_local(request_body.asset_id):
        print(f"File succesffully written: {request_body.asset_id}")
    register_asset_id_on_liquid(request_body.asset_id, request_body.contract)
    return {"asset_id": request_body.asset_id}


def register_asset_id_local(asset_id: str):
    try:
        f = open(f"{LOCAL_STORAGE_LOCATION}/.well-known/liquid-asset-proof-" + asset_id, "w")
        f.write("Authorize linking the domain name lab.r3c.network to the Liquid asset " + asset_id)
        f.close()
    except Exception as e:
        print(f"File Write execption: {e}")
        return False
    return True


def schedule_task(task_array: list):
    register_response = subprocess.run(task_array, stdout=subprocess.PIPE)
    if register_response.returncode == 0:
        print(register_response.stdout.decode("ASCII"))
    else:
        print(register_response.returncode)


def register_asset_id_on_liquid(asset_id: str, contract: dict):
    contract = json.dumps(contract)
    input_json = f'{{"asset_id":"{asset_id}","contract":{contract}}}'
    register_request = [
        "tsp",
        "curl",
        f"{ASSET_REG_URL}",
        "-H",
        "Content-Type: application/json",
        "-d",
        f"{input_json}",
    ]
    schedule_task(["tsp", "sleep", "15m"])
    schedule_task(register_request)
