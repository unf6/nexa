import requests
import threading
from modules.funcs.console import *

def f(url, payloads):
    try:
        num_threads = 5  # Number of threads to run concurrently (you can adjust this as needed)
        payloads_per_thread = len(payloads) // num_threads

        def test_payloads_thread(payloads, thread_id):
            try:
                start_idx = thread_id * payloads_per_thread
                end_idx = start_idx + payloads_per_thread if thread_id < num_threads - 1 else len(payloads)

                for i in range(start_idx, end_idx):
                    payload = payloads[i].strip()
                    try:
                        data = {'message': payload}
                        response = requests.post(url, data=data)

                        if 'XSS' in response.text:
                            print_success(f"URL: {url} - Payload: {payload} - XSS Found(via requests)")
                        else:
                            print_warning(f"URL: {url} - Payload: {payload} - No XSS (via requests)")

                    except requests.exceptions.RequestException as e:
                        print_error(f"Error (requests): {e}")

            except Exception as e:
                print_error(f"Error in test_payloads_thread: {e}")

        threads = []
        for i in range(num_threads):
            thread = threading.Thread(target=test_payloads_thread, args=(payloads, i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print_error(f"Error in test_reflected_xss_payloads: {e}")