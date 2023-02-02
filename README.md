# Bitcoin Bruteforce private keys (24 address in one iteration)
Now you can Brute force all type of bitcoin addresses and private keys in one script (Uncompressed, Compressed, Segwit and Bech32)

# How to
This script runs on Python 3.*

You must install libs:

bit, itertools, bitcoinlib

Then you must open this script in any redactor and fill up lines 20-30 (smtp settings), set path to DATABASE at line 33, set path to winner file at line 81.

Run your script directly from command line: python BitStorm.py

# Speed
On my Macbook Air M1 it calculates 1 iteration (check 24 address in 43m database) by 0.0010245 secs.

# Database
You can use database from Loyce Club (List of all funded Bitcoin addresses (balance not shown, sorted in alphabetical order)) in .txt format
Put your database to a path, that you set in DATABASE (line 33)

# If you find something
Write to me at Telegram (@kumulative) and i send you instructions how to convert your HEX key to proper address/final key

# To do
- search for substrings to save memory
- speed up script
- write some at Readme
- add script to convert result HEX to addresses and final private keys

# How you can help
- you can rewrite this script for better performance and make pull request
- you can test it and write some issues
- you can donate me some to 1GBjnzLEcNwqcHwiJysZ2HjtCEyKF5ABQu (Bitcoin), 0x6ae7595202a4c296d23697014ec3c7112d4ee0de (Ethereum) or 0x6ae7595202a4c296d23697014ec3c7112d4ee0de (USDT BSC(BEP20))
