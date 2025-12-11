import os
import random
import string
import time


def generate_bot_name(length=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_invalid_name(length=15):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-[]{}|;:',.<>?/~`"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_first_name(length=6):
    return ''.join(random.choice(string.ascii_letters).capitalize() for _ in range(1)) + \
           ''.join(random.choice(string.ascii_lowercase) for _ in range(length-1))

def generate_last_name(length=6):
    return ''.join(random.choice(string.ascii_letters).capitalize() for _ in range(1)) + \
           ''.join(random.choice(string.ascii_lowercase) for _ in range(length-1))

def generate_org_name():
    companies = ["YavarTech", "CloudSphere", "SoftNova", "TechVibe", "InnoCore", "MetaSoft"]
    return random.choice(companies)

def generate_email():
    random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
    return f"{random_string}{int(time.time())}@yopmail.com"   # Always unique

def generate_phone_number():
    return ''.join(random.choice("987654321") for _ in range(10))

def generate_top_k(min_value=2, max_value=15):
    return random.randint(min_value, max_value)

def generate_chunk_size(min_value=200, max_value=1000):
    return random.randint(min_value, max_value)

def generate_chunk_overlap(min_value=50, max_value=200):
    return random.randint(min_value, max_value)

def get_random_file_path(folder_path, all_files):
        random_file = random.choice(all_files)
        file_path = os.path.join(folder_path, random_file)
        return file_path

def get_unique_random_file(folder_path, all_files, used_files):
    remaining = [f for f in all_files if f not in used_files]

    if not remaining:
        raise ValueError("No more unique files left to select!")

    random_file = random.choice(remaining)
    used_files.append(random_file)

    return os.path.join(folder_path, random_file)

def bot_settings_bot_name(length=10):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def get_random_greeting_msg():
    greeting_messages = [
        "Meet your AI assistant!",
        "Welcome to your AI helper!",
        "Say hello to your AI bot!",
        "Your smart AI is here!",
        "Hi! I'm your AI assistant.",
        "Hello! Your AI is ready.",
        "AI assistant at your service!",
        "Your AI helper is ready!",
        "Hey there! Meet your AI.",
        "Your AI buddy is here!"
    ]
    greeting = random.choice(greeting_messages)
    return greeting
def get_random_initial_msg():
    initial_messages = [
        "Hello! How can I assist you today?",
        "Hi there! What would you like help with?",
        "Greetings! How may I support you today?",
        "I'm here to help. What would you like to do?",
        "How can I make your day easier today?"
    ]
    initial = random.choice(initial_messages)
    return initial

