Python Script to read bluetooth data off a Calypso Ultrasonic Protable mini Anemometer

Just run `python3 anemometer.py` in terminal.

If you want it to automatically run on boot, follow these steps:

1.  Create a `.desktop` file
2.  Copy and paste this code into the new file

```ini
[Desktop Entry]
Type=Application
Name=Plot Generator
Exec=/usr/bin/python3 /path/to/your_script.py
Terminal=false
```
3.  Move the `.desktop` file into the `~/.config/autostart` or equivalent directory
4.  Make it executable using `sudo chmod +x ~/.config/autostart/{filename}.desktop`
5.  Run `sudo reboot`
