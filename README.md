# RaspberryPi eInk Headless Display

A simple diplay script for RaspberryPi with eInk HAT.

## How to use:
You may use the scripts directly or install them as a linux service.

### Scripts:

- Run `ePaper/main.sh` to run the main script displaying live time and IP address.
- Run `ePaper/goodbye.sh` to run the goodbye one time display script.

### Service:

Use the `ePaper/sample_service.service` to create the suitable service file and enable it in Raspbian using this [guide](https://www.raspberrypi.org/documentation/linux/usage/systemd.md).
