# random_logger.py
import random
import time
from datetime import datetime

messages = ["Hello, OpenShift!", "Logging a random message", "Welcome to Red Hat OCP", "Exploring containerized applications"]

while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time}: {random.choice(messages)}")
        time.sleep(2)  # Log a message every 2 seconds
