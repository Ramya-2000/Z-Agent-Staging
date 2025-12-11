import os
import time

def take_screenshot(driver, name="screenshot"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, f"{name}_{timestamp}.png")

    driver.save_screenshot(path)
    return path
