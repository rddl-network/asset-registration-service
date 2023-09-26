```
1. pipenv install --python 3.10 -> get the venv path
2. edit the service file accordingly with the correct venv path and the user and group
3. you might need to check pipenv location on the target device (which pipenv)
4. define the ENVIRONMENT variables: ASSET_REG_URL and WELL_KNOWN_FOLDER for your process or service
4. sudo cp asset_registry.service /lib/systemd/system/
5. sudo systemctl start asset_registry.service 
6. sudo systemctl status asset_registry.service 
7. sudo journalctl -u asset_registry.service

```