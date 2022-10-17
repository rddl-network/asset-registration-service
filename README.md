```
1. pipenv install --python 3.9 -> get the venv path
2. edit the service file accordingly with the correct venv path
3. you might need to check pipenv location on the target device (which pipenv)
3. sudo cp liquid_registry.service /lib/systemd/system/
4. sudo systemctl start liquid_registry.service 
5. sudo systemctl status liquid_registry.service 
6. sudo journalctl -u liquid_registry.service

```