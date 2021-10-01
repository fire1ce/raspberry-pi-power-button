
# Raspberry Pi Power Button - Wake/Power Off/Restart(Double Press)

## Information

When Raspberry Pi is powered off, shortening GPIO3 (Pin 5) to ground will wake the Raspberry Pi.

This script will use pin GPIO3(5), Ground(6) with momentary button.

![gpio layout](https://github.com/fire1ce/raspberry-pi-power-button/raw/main/gpio_layout.jpg)


       3V3  (1) (2)  5V         
     GPIO2  (3) (4)  5V         
    -----------------------     
    | GPIO3  (5) (6)  GND | <-  
    -----------------------     
     GPIO4  (7) (8)  GPIO14     
       GND  (9) (10) GPIO15     
    GPIO17 (11) (12) GPIO18     
    GPIO27 (13) (14) GND        
    GPIO22 (15) (16) GPIO23     
       3V3 (17) (18) GPIO24     
    GPIO10 (19) (20) GND        
     GPIO9 (21) (22) GPIO25     
    GPIO11 (23) (24) GPIO8      
       GND (25) (26) GPIO7      
     GPIO0 (27) (28) GPIO1      
     GPIO5 (29) (30) GND        
     GPIO6 (31) (32) GPIO12     
    GPIO13 (33) (34) GND        
    GPIO19 (35) (36) GPIO16     
    GPIO26 (37) (38) GPIO20     
       GND (39) (40) GPIO21     

## Requirements

* python3-gpiozero

Can be install via apt

```bash
sudo apt install python3-gpiozero
```

## Install

This will install the script as `service` and it will run at boot

```bash
curl https://raw.githubusercontent.com/fire1ce/raspberry-pi-power-button/main/install.sh | bash
```

## Uninstall

```bash
curl https://raw.githubusercontent.com/fire1ce/raspberry-pi-power-button/main/uninstall.sh | bash
```

## Default Behavior

| __Button Press When Pi is On__      | __Description__ |
| ----------------------------------- | --------------- |
| Single                              | Nothing         |
| Double                              | Reboot          |
| Long and releases (Above 3 seconds) | Power off       |

| __Button Press When Pi is off__ | __Description__            |
| ------------------------------- | -------------------------- |
| Single                          | Powers on the Raspberry Pi |

## Check if service is running

```bash
sudo systemctl status power_button.service
```
