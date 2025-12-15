import os
import random
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,wait


from utils.data_generator import bot_settings_bot_name, get_random_greeting_msg, get_random_initial_msg, generate_email


class BotSettingsPage:
    def __init__(self, driver):
        self.driver = driver

        self.bot_settings_module= (By.XPATH, "//button[.//span[text()='Bot Settings']]")

        self.bot_personalization_expand =(By.XPATH, "//button[.//h3[normalize-space()='Bot Personalization']]")
        self.theme_settings_expand =(By.XPATH, "//button[.//h3[normalize-space()='Theme Settings']]")
        self.general_settings_expand =(By.XPATH, "//button[.//h3[normalize-space()='General Settings']]")
        self.tts_settings_expand=(By.XPATH, "//button[.//h3[normalize-space()='TTS Settings']]")
        self.security_expand =(By.XPATH,"//button[.//h3[normalize-space()='Security']]")

        self.bot_name=(By.XPATH, "//input[@placeholder='Enter bot name']")

        self.tts_stt_model=(By.XPATH, "//label[text()='TTS STT Model']/following::div[1]")
        self.tts_options=(By.XPATH, "//label[text()='TTS STT Model']//following::div[@role='option']")

        self.bot_lang=(By.XPATH, "//label[text()='Choose Bot Languages']/following::div[1]")
        self.bot_lang_options =(By.XPATH, "//label[text()='Choose Bot Languages']//following::div[@role='listbox']//div[@role='option']")
        self.remove_english = (By.XPATH, "//div[@role='button' and @aria-label='Remove English']")


        self.bot_mood=(By.XPATH, "//label[text()='Choose Bot Mood']/following::input[@role='combobox'][1]")
        self.playback_speed =(By.XPATH, "//label[text()='Choose Bot Playback Speed']/following::span[text()='1x'][1]")
        self.playback_options=(By.XPATH, "//label[text()='Choose Bot Playback Speed']//following::div[1]")

        self.cancel_btn_bot_voice=(By.XPATH, "//button[normalize-space()='Cancel']")
        self.save_btn_bot_voice=(By.XPATH, "//button[normalize-space()='Save Changes']")
        self.greeting_msg=(By.XPATH, "//textarea[@placeholder='Welcome to Z-Agent']")
        self.initial_message=(By.XPATH, "//textarea[@name='initial_message']")
        self.role=(By.XPATH, "//textarea[@name='role']")
        self.goal=(By.XPATH, "//textarea[@name='goal']")
        self.instructions=(By.XPATH, "//textarea[@name='instructions']")

        self.bot_lang_validation=(By.XPATH, "//p[normalize-space()='At least one language must be selected']")
        self.bot_name_validation=(By.XPATH, "//p[contains(text(), 'Bot name is required')]")

        self.bot_avatar=(By.XPATH, "//label[@for='image-upload']")
        self.bot_avatar_img_save =(By.XPATH,"//button[normalize-space()='Crop & Save']")
        self.header_bg=(By.CSS_SELECTOR, "input[name='chat_window_colors.header_background']")
        self.header_text=(By.CSS_SELECTOR, "input[name='chat_window_colors.header_text']")
        self.AI_msg_bg= (By.CSS_SELECTOR, "input[name='chat_window_colors.ai_message_background']")
        self.AI_msg_text= (By.CSS_SELECTOR, "input[name='chat_window_colors.ai_message_text']")
        self.user_msg_bg= (By.CSS_SELECTOR, "input[name='chat_window_colors.user_message_background']")
        self.user_msg_text= (By.CSS_SELECTOR, "input[name='chat_window_colors.user_message_text']")
        self.call_btn_bg= (By.CSS_SELECTOR, "input[name='chat_window_colors.call_button_background']")
        self.call_btn_text= (By.CSS_SELECTOR, "input[name='chat_window_colors.call_button_text']")
        self.send_btn_bg= (By.CSS_SELECTOR, "input[name='chat_window_colors.send_button_background']")
        self.send_btn_text= (By.CSS_SELECTOR, "input[name='chat_window_colors.send_button_text']")
        self.save_btn=(By.XPATH, "//h3[normalize-space()='TTS Settings']/following::*//button[@title='Save'][1]")
        self.success_msg=(By.XPATH, "//div[contains(text(),'Bot Updated Successfully')]")

        self.thinking_bg= (By.CSS_SELECTOR, "input[name='landing_page_colors.thinking_message_background']")
        self.thinking_text= (By.CSS_SELECTOR, "input[name='landing_page_colors.thinking_message_text']")
        self.next_btn_left= (By.CSS_SELECTOR, "input[name='landing_page_colors.next_button_left']")
        self.next_btn_right= (By.CSS_SELECTOR, "input[name='landing_page_colors.next_button_right']")
        self.next_btn_icon= (By.CSS_SELECTOR, "input[name='landing_page_colors.next_button_text']")
        self.language_underline= (By.CSS_SELECTOR, "input[name='landing_page_colors.underline_color']")
        self.user_avatar_color= (By.CSS_SELECTOR, "input[name='landing_page_colors.underline_color']")
        self.user_avatar_bg= (By.CSS_SELECTOR, "input[name='avatars.user_avatar_background']")

        self.forms_toggle=(By.XPATH, "//h4[normalize-space()='Enable Forms']/following::button[@role='switch'][1]")
        self.document_identity_toggle=(By.XPATH, "//h4[normalize-space()='Document Identity Details']/following::button[@role='switch'][1]")
        self.chat_summary_toggle=(By.XPATH, "//h4[normalize-space()='Chat Summary']/following::button[@role='switch'][1]")
        self.live_agent_toggle=(By.XPATH, "//h4[normalize-space()='Live Agent']/following::button[@role='switch'][1]")
        self.image_upload_toggle=(By.XPATH, "//h4[normalize-space()='Image Upload']/following::button[@role='switch'][1]")
        self.image_capture_toggle=(By.XPATH, "//h4[normalize-space()='Image Capture']/following::button[@role='switch'][1]")
        self.share_loc_toggle= (By.XPATH,"//h4[normalize-space()='Share Location']/following::button[@role='switch'][1]")
        self.know_more_toggle=(By.XPATH, "//h4[normalize-space()='Know More Setting']/following::button[@role='switch'][1]")
        self.enter_email_input =(By.XPATH, "//input[@name='know_more_email']")
        self.deactivate_but_btn = (By.XPATH, "//button[normalize-space()='Deactivate bot']")
        self.tts_settings_toggle= (By.XPATH, "//h4[normalize-space()='TTS Settings']/following::button[@role='switch'][1]")
        self.voice_interruption_toggle=(By.XPATH, "//h4[normalize-space()='Voice Interruption']/following::button[@role='switch'][1]")


        self.next_button=(By.XPATH, "//button[normalize-space()='Next']")

    def validation_msg_bot(self):
        wait = WebDriverWait(self.driver, 10)
        actions = ActionChains(self.driver)

        # Open bot settings
        wait.until(EC.element_to_be_clickable(self.bot_settings_module)).click()
        wait.until(EC.element_to_be_clickable(self.bot_personalization_expand)).click()

        # Clear bot name
        bot_name_field = wait.until(EC.element_to_be_clickable(self.bot_name))
        bot_name_field.click()
        bot_name_field.send_keys(Keys.CONTROL, "a")
        bot_name_field.send_keys(Keys.BACKSPACE)

        self.driver.execute_script("arguments[0].blur();", bot_name_field)
        # click empty spot
        print("clicked outside")
        wait = WebDriverWait(self.driver, 10)

        bot_val_msg = wait.until(
            EC.visibility_of_element_located(self.bot_name_validation)
        )
        assert "Bot name is required" in bot_val_msg.text

        # self.driver.find_element(*self.tts_stt_model).click()

        wait.until(EC.element_to_be_clickable(self.remove_english)).click()
        time.sleep(2)
        bot_lang_field = wait.until(EC.element_to_be_clickable(self.bot_lang))
        bot_lang_field.click()
        bot_lang_field.click()

        time.sleep(2)

        bot_lang_field.send_keys(Keys.TAB)
        print("clicked outside of bot language")
        wait = WebDriverWait(self.driver, 10)

        bot_lang_val_msg = wait.until(
            EC.visibility_of_element_located(self.bot_lang_validation)
        )
        assert "At least one language must be selected" in bot_lang_val_msg.text
        time.sleep(3)
        self.driver.navigate().refresh()
        time.sleep(3)

    def valid_bot_personalization(self):
        self.driver.find_element(*self.bot_personalization_expand).click()
        time.sleep(2)
        bot_name_value = bot_settings_bot_name()  # <-- call the function

        bot_name_field = self.driver.find_element(*self.bot_name)
        bot_name_field.click()
        bot_name_field.send_keys(Keys.CONTROL, "a")
        bot_name_field.send_keys(Keys.BACKSPACE)
        bot_name_field.send_keys(bot_name_value)
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable(self.tts_stt_model))
        dropdown.click()

        # Wait for all options to appear
        tts_options = wait.until(
            EC.visibility_of_all_elements_located(self.tts_options)
        )
        # Pick a random option
        tts_random_option = random.choice(tts_options)
        tts_selected_text = tts_random_option.text  # get before interacting
        # Click randomly chosen option
        self.driver.execute_script("arguments[0].scrollIntoView(true);", tts_random_option)
        time.sleep(2)
        tts_random_option.click()
        time.sleep(2)

        # --- If Elevenlabs is selected → remove English ---
        if tts_selected_text.strip().lower() == "elevenlabs":
            print("Elevenlabs selected → Clicking Remove English")
            remove_btn = self.driver.find_element(*self.remove_english)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_btn)
            remove_btn.click()
            time.sleep(2)
        else:
            print("TTS/STT is not Elevenlabs → Skipping Remove English")




        self.driver.find_element(*self.bot_lang).click()

        # Wait for all options to appear
        bot_lang_options = wait.until(
            EC.presence_of_all_elements_located(self.bot_lang_options)
        )
        # Pick a random option
        selected_option = random.choice(bot_lang_options)

        # Scroll to option
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            selected_option
        )
        time.sleep(1)

        # Extract exact text (each option is a single <div>)
        bot_lang_selected_text = selected_option.text.strip()

        # Click option
        selected_option.click()

        print("Random bot lang selected:", bot_lang_selected_text)



        # # Pick a random option
        # bot_lang_random_option = random.choice(bot_lang_options)
        # bot_lang_selected_text = bot_lang_random_option.text  # get before interacting
        #
        # print("random optionnnnnnnnn", bot_lang_selected_text)
        #
        # # Click randomly chosen option
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", bot_lang_random_option)
        # bot_lang_random_option.click()
        # time.sleep(3)
        # print("Random bot lang selected:", bot_lang_selected_text)





        wait = WebDriverWait(self.driver, 30)
        clean_text = bot_lang_selected_text.strip().replace("\n", "").replace("\r", "")

        dynamic_voice_locator = (
            By.XPATH,
            f"//button//*[normalize-space(text())='{clean_text}']"
        )

        print("Selected text raw →", repr(bot_lang_selected_text))
        print(f"//button//*[normalize-space(text())='{bot_lang_selected_text.strip()}']")
        # Wait for visible
        voice_btn = wait.until(EC.visibility_of_element_located(dynamic_voice_locator))

        # Scroll
        self.driver.execute_script("arguments[0].scrollIntoView(true);", voice_btn)

        # Wait until clickable
        voice_btn = wait.until(EC.element_to_be_clickable(dynamic_voice_locator))

        # Click
        voice_btn.click()

        time.sleep(2)
        wait.until(EC.element_to_be_clickable(self.playback_speed))
        # Click dropdown
        playback_speed_options = wait.until(
            EC.visibility_of_all_elements_located(self.playback_options)
        )
        # Pick a random option
        random_option = random.choice(playback_speed_options)
        time.sleep(2)
        playback_speed_selected_text = random_option.text  # get before interacting

        # Click randomly chosen option
        self.driver.execute_script("arguments[0].scrollIntoView(true);", random_option)
        random_option.click()

        print("Random playback speed options selected:", playback_speed_selected_text)
        self.driver.find_element(*self.save_btn_bot_voice).click()

        greeting_msg = get_random_greeting_msg()
        initial_msg = get_random_initial_msg()

        greeting=self.driver.find_element(*self.greeting_msg)
        greeting.send_keys(Keys.CONTROL, "a")
        greeting.send_keys(Keys.BACKSPACE)
        greeting.send_keys(greeting_msg)
        time.sleep(2)

        initial= self.driver.find_element(*self.initial_message)
        initial.send_keys(Keys.CONTROL, "a")
        initial.send_keys(Keys.BACKSPACE)
        initial.send_keys(initial_msg)

        time.sleep(4)
        self.driver.find_element(*self.bot_personalization_expand).click()
        time.sleep(2)

# Themeeeeee Settings
    def theme_settings(self):
        self.driver.find_element(*self.theme_settings_expand).click()
        self.driver.find_element(*self.bot_avatar)
        time.sleep(2)
        folder_path = r"C:\Users\admin\PycharmProjects\ZagentStage\Z-agentnew\images"

        # Get all image files (jpg, png, jpeg)
        image_files = [f for f in os.listdir(folder_path)
                       if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        if not image_files:
            raise Exception("No image files found in the folder!")

        # Pick random image
        random_image = random.choice(image_files)
        image_full_path = os.path.join(folder_path, random_image)

        print("Selected random image:", image_full_path)

        # Locate the file input element where image must be uploaded
        upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        # Upload image using send_keys
        upload_input.send_keys(image_full_path)
        time.sleep(2)
        self.driver.find_element(*self.bot_avatar_img_save).click()
        time.sleep(5)

        print("Image uploaded successfully!")

        header_field=self.driver.find_element(*self.header_bg)
        header_field.click()

        colors = ["#c3cb12", "#a88e88", "#339fc0","#30c45c", "#000000",
                  "#a319c6", "#f8deff","#aa1919", "#ffffff", "#ebe5fd"]

        # Choose random color
        random_color = random.choice(colors)
        print("Selected random color header bg:", random_color)

        # Clear existing value
        header_field.send_keys(Keys.CONTROL, "a")  # select all
        header_field.send_keys(Keys.BACKSPACE)  # delete
        time.sleep(2)

        # Enter the random color
        header_field.send_keys(random_color)
        time.sleep(1)

        # All your locators
        color_fields = [
            self.header_text,
            self.AI_msg_bg,
            self.AI_msg_text,
            self.user_msg_bg,
            self.user_msg_text,
            self.call_btn_bg,
            self.call_btn_text,
            self.send_btn_bg,
            self.send_btn_text
        ]

        # Assign random color to each locator
        for locator in color_fields:
            # Pick a random color every time
            random_color = random.choice(colors)
            print(f"Applying {random_color} to {locator}")

            field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )

            # field.click()
            # time.sleep(3)
            # field.clear()

            field.send_keys(Keys.CONTROL, "a")
            field.send_keys(Keys.BACKSPACE)
            time.sleep(2)

            # Apply the random color
            field.send_keys(random_color)
            time.sleep(2)

# Landing Pages
        colors = ["#c3cb12", "#a88e88", "#339fc0", "#30c45c","#000000",
                  "#a319c6", "#f8deff", "#aa1919", "#ffffff", "#ebe5fd"]
        color_fd = [
            self.thinking_bg,
            self.thinking_text,
            self.next_btn_left,
            self.next_btn_right,
            self.next_btn_icon,
            self.language_underline]

        # Assign random color to each locator
        for loc in color_fd:
            # Pick a random color every time
            random_color = random.choice(colors)
            print(f"Applying {random_color} to {loc}")

            landing_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(loc)
            )

            landing_field.click()
            time.sleep(2)

            # Clear existing text
            landing_field.send_keys(Keys.CONTROL, "a")
            landing_field.send_keys(Keys.BACKSPACE)

            # Apply the random color
            landing_field.send_keys(random_color)
            time.sleep(1)
        save_button = self.driver.find_element(*self.save_btn)

        # Scroll to the element (center of screen recommended)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)

        # Click
        save_button.click()

        wait = WebDriverWait(self.driver, 20)
        bot_settings_msg = wait.until(
            EC.visibility_of_element_located(self.success_msg)
        )
        assert "Bot Updated Successfully" in bot_settings_msg.text

    def general_settings(self):
        time.sleep(2)
        self.driver.find_element(*self.general_settings_expand).click()

    def toggle_all(self):
            time.sleep(2)
            toggle = self.driver.find_element(*self.forms_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", toggle)

            # Read current state (true / false)
            state = toggle.get_attribute("aria-checked")

            print(f"Toggle: {toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                toggle.click()
                print(f"Clicked toggle {toggle}")
            else:
                print(f"⚠ Unknown toggle state for {toggle}: {state}")
            time.sleep(4)


            document_toggle = self.driver.find_element(*self.document_identity_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", document_toggle)

            # Read current state (true / false)
            state =document_toggle.get_attribute("aria-checked")

            print(f"Toggle: {document_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                document_toggle.click()
                print(f"Clicked toggle {document_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {document_toggle}: {state}")
            time.sleep(4)

            chat_toggle = self.driver.find_element(*self.chat_summary_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", chat_toggle)

            # Read current state (true / false)
            state = chat_toggle.get_attribute("aria-checked")

            print(f"Toggle: {chat_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                chat_toggle.click()
                print(f"Clicked toggle {chat_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {chat_toggle}: {state}")
            time.sleep(4)

            live_toggle = self.driver.find_element(*self.live_agent_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", live_toggle)

            # Read current state (true / false)
            state = live_toggle.get_attribute("aria-checked")

            print(f"Toggle: {live_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                live_toggle.click()
                print(f"Clicked toggle {live_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {live_toggle}: {state}")
            time.sleep(4)



            img_toggle = self.driver.find_element(*self.image_upload_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", img_toggle)

            # Read current state (true / false)
            state = img_toggle.get_attribute("aria-checked")

            print(f"Toggle: {img_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                img_toggle.click()
                print(f"Clicked toggle {img_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {img_toggle}: {state}")
            time.sleep(4)

            #
            img_cap_toggle = self.driver.find_element(*self.image_capture_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", img_cap_toggle)

            # Read current state (true / false)
            state = img_cap_toggle.get_attribute("aria-checked")

            print(f"Toggle: {img_cap_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                img_cap_toggle.click()
                print(f"Clicked toggle {img_cap_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {img_cap_toggle}: {state}")
            time.sleep(4)



            loc_toggle = self.driver.find_element(*self.share_loc_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", loc_toggle)

            # Read current state (true / false)
            state = loc_toggle.get_attribute("aria-checked")

            print(f"Toggle: {loc_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                loc_toggle.click()
                print(f"Clicked toggle {loc_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {loc_toggle}: {state}")
            time.sleep(4)


            know_toggle = self.driver.find_element(*self.know_more_toggle)

            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", know_toggle)

            # Read current state (true / false)
            state = know_toggle.get_attribute("aria-checked")

            print(f"Toggle: {know_toggle} → Current State: {state}")

            # If enabled or disabled → click anyway (as per your requirement)
            if state in ["true", "false"]:
                know_toggle.click()
                print(f"Clicked toggle {loc_toggle}")
            else:
                print(f"⚠ Unknown toggle state for {know_toggle}: {state}")
            time.sleep(4)

            know_more_email=self.driver.find_element(*self.enter_email_input)
            know_more_email_id=generate_email()
            know_more_email.send_keys(know_more_email_id)
            time.sleep(3)

            save_button = self.driver.find_element(*self.save_btn)
            # Scroll to the element (center of screen recommended)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
            # Click
            save_button.click()



    def tts_settings(self):
        time.sleep(2)
        self.driver.find_element(*self.tts_settings_expand).click()
        time.sleep(2)
        tts_toggle = self.driver.find_element(*self.tts_settings_toggle)

        # Scroll element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",tts_toggle)

        # Read current state (true / false)
        state = tts_toggle.get_attribute("aria-checked")

        print(f"Toggle: {tts_toggle} → Current State: {state}")

        # If enabled or disabled → click anyway (as per your requirement)
        if state in ["true", "false"]:
            tts_toggle.click()
            print(f"Clicked toggle {tts_toggle}")
        else:
            print(f"⚠ Unknown toggle state for {tts_toggle}: {state}")
        time.sleep(4)


        voice_toggle = self.driver.find_element(*self.voice_interruption_toggle)

        # Scroll element into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",voice_toggle)

        # Read current state (true / false)
        state =voice_toggle.get_attribute("aria-checked")

        print(f"Toggle: {voice_toggle} → Current State: {state}")

        # If enabled or disabled → click anyway (as per your requirement)
        if state in ["true", "false"]:
            voice_toggle.click()
            print(f"Clicked toggle {voice_toggle}")
        else:
            print(f"⚠ Unknown toggle state for {voice_toggle}: {state}")
        time.sleep(4)

        save_button = self.driver.find_element(*self.save_btn)
        # Scroll to the element (center of screen recommended)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_button)
        # Click
        save_button.click()


        wait = WebDriverWait(self.driver, 10)
        bot_settings_msg = wait.until(
            EC.visibility_of_element_located(self.success_msg)
        )
        assert "Bot Updated Successfully" in bot_settings_msg.text
        time.sleep(4)

        self.driver.find_element(*self.next_button).click()







