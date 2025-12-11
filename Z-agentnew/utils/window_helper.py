def close_other_tabs(driver, keep_last=1):
    handles = driver.window_handles
    while len(handles) > keep_last:
        driver.switch_to.window(handles[0])
        driver.close()
        handles = driver.window_handles
    driver.switch_to.window(handles[0])
