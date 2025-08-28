
# API Documentation

## Endpoints

### GET /health
- **Description:** Health check endpoint.
- **Response:**
	```json
	{ "health": "ok" }
	```

**Sample curl:**
```sh
curl -X GET http://localhost:8000/health
```

### GET /.well-known
- **Description:** Lists files in the `.well-known` directory.
- **Response:** HTML page listing file URLs.

**Sample curl:**
```sh
curl -X GET http://localhost:8000/.well-known
```

### POST /register_asset
- **Description:** Registers a new asset.
- **Request Body:**
	```json
	{
		"asset_id": "string",
		"contract": { }
	}
	```
- **Response:**
	```json
	{ "asset_id": "string" }
	```
- **Status Code:** 201 Created

**Sample curl:**
```sh
curl -X POST http://localhost:8000/register_asset \
	-H "Content-Type: application/json" \
	-d '{"asset_id": "your_asset_id", "contract": {}}'
```

## Environment Variables

- `ASSET_REG_URL`: URL for asset registration (default: `https://assets.blockstream.info`)
- `WELL_KNOWN_FOLDER`: Path to `.well-known` directory (default: `/var/www/html/.well-known`)

---

```
0. Make sure tsp (apt install task-spooler) is installed
1. pipenv install --python 3.10 -> get the venv path
2. edit the service file accordingly with the correct venv path and the user and group
3. you might need to check pipenv location on the target device (which pipenv)
4. define the ENVIRONMENT variables: ASSET_REG_URL and WELL_KNOWN_FOLDER for your process or service
4. sudo cp asset_registry.service /lib/systemd/system/
5. sudo systemctl start asset_registry.service 
6. sudo systemctl status asset_registry.service 
7. sudo journalctl -u asset_registry.service

```
