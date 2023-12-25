import queue
import uuid

queue = queue.Queue()

def generate_request():
    value = uuid.uuid4()
    queue.put(value)

def process_request():
    if not queue.empty():
        processed_request = queue.get()
        print(f"Request processed: {processed_request}")
    else:
        print("Queue is empty. No requests to process.")

while True:
    generate_request()

    process_request()