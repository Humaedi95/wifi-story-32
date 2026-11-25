#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is a whole breakup story in 24 characters: the narrator
broke up with their ex, but the ex still pays the Wi-Fi bill, so
the narrator is still freeloading on the connection.
"""

import os

WIFI_NAME = "MyExStillPaysForThisWiFi"


def main() -> None:
    # A Wi-Fi name must be 1-32 characters; the gate rejects anything
    # longer, so fail loudly here instead of writing an invalid entry.
    assert 1 <= len(WIFI_NAME) <= 32, "Wi-Fi name must be 1-32 characters"
    assert WIFI_NAME.strip(), "Wi-Fi name must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WIFI_NAME)


if __name__ == "__main__":
    main()
