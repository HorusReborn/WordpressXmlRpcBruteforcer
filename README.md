# XML-RPC WordPress Brute Force Tool  

## ⚠️ IMPORTANT DISCLAIMER – READ BEFORE USING

This tool is provided **only for authorized testing and educational purposes**.  
Using it on any website you do not own or have **explicit written permission** to test is **illegal** and can result in serious legal consequences.

By using this tool, you confirm that you are performing a legal authorized test and will not misuse it.

Run the Tool

python3 wppasswordbruteforce.py https://example.com/xmlrpc.php thepasswordlist validusername


## What Is This Tool?

This is a fast and powerful **XML-RPC brute force** tool specifically designed for WordPress sites.  
It can crack the login to any WordPress site that has **XML-RPC enabled** (most sites do).

It is significantly faster than the normal login form because it uses the `wp.getUsersBlogs` method with `system.multicall`.

## Why Use XML-RPC Brute Force?

- Much faster than the normal login page
- Can test thousands of passwords per minute
- Works even when the normal login form is protected
- Excellent for red teaming and authorized testing only

## Target Requirements

- WordPress site (any version)
- **XML-RPC must be enabled** (check with: `https://example.com/xmlrpc.php`)
- You need:
  - A valid username
  - A list of passwords (one per line)
  - The target site URL

## Features

- Supports multiple usernames in one run
- Real-time progress with color output
- Saves successful credentials to `found.txt`
- Handles common WordPress login forms
- Very easy to use and modify

## Installation & Usage

### 1. Install Python
Make sure you have **Python 3** installed.

### 2. Copy the Script
Copy the entire code below into a file named `passbruteforcewp.py`

### 3. Install Dependencies (only once)
```bash
pip install requests
