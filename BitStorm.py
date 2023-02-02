import itertools
import smtplib
import bit
import secrets
import bitcoinlib
from bit import *
import os
import multiprocessing
###############################################################################
# Field secp256k1
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

###############################################################################
# Constant
lmda = 0x5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72
lmda2 = 0xac9c52b33fa3cf1f5ad9e3fd77ed9ba4a880b9fc8ec739c2e0cfc810b51283ce      # lmda*lmda

###############################################################################
# Send email
def send_notification(email, txt):
    sender = 'email@email.com'
    sender_password = 'YourPassword'
    mail_lib = smtplib.SMTP_SSL('smtp.server.com', 465)
    mail_lib.login(sender, sender_password)
    msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (
    sender, email, 'Congrats! You find the KEY!')
    msg += txt
    mail_lib.sendmail(sender, email, msg.encode('utf8'))
    mail_lib.quit()

# Loading database
DATABASE = r'/path_to_database_files/'
print('Loading database...')
database = set()
for filename in os.listdir(DATABASE):
    with open(DATABASE + filename) as file:
         for address in file:
            address = address.strip()
            database.add(address)
print('READY')
print('Total address count: ' + str(len(database)))

# Generating 24 address from one key (6 unique privkeys total)
def search():
    for i in itertools.count():
        try:
            secretsGenerator = secrets.SystemRandom()
            privetkey = secretsGenerator.randrange(1,115792089237316195423570985008687907852837564279074904382605163141518161494336)
            privetkey = hex(privetkey)
            pvk = int(privetkey, 16)
            addr1 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk)._pk.public_key.format(compressed=True)))
            addr2 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk)._pk.public_key.format(compressed=False)))
            addr3 = str(bit.Key.from_int(pvk).segwit_address)
            addr4 = str(bitcoinlib.keys.Address(bit.Key.from_int(pvk).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            addr5 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk*lmda%N)._pk.public_key.format(compressed=True)))
            addr6 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk*lmda%N)._pk.public_key.format(compressed=False)))
            addr7 = str(bit.Key.from_int(pvk*lmda%N).segwit_address)
            addr8 = str(bitcoinlib.keys.Address(bit.Key.from_int(pvk*lmda%N).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            addr9 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk*lmda2%N)._pk.public_key.format(compressed=True)))
            addr10 = str(bit.format.public_key_to_address(bit.Key.from_int(pvk*lmda2%N)._pk.public_key.format(compressed=False)))
            addr11 = str(bit.Key.from_int(pvk*lmda2%N).segwit_address)
            addr12 = str(bitcoinlib.keys.Address(bit.Key.from_int(pvk*lmda2%N).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            addr13 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk)._pk.public_key.format(compressed=True)))
            addr14 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk)._pk.public_key.format(compressed=False)))
            addr15 = str(bit.Key.from_int(N-pvk).segwit_address)
            addr16 = str(bitcoinlib.keys.Address(bit.Key.from_int(N-pvk).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            addr17 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk*lmda%N)._pk.public_key.format(compressed=True)))
            addr18 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk*lmda%N)._pk.public_key.format(compressed=False)))
            addr19 = str(bit.Key.from_int(N-pvk*lmda%N).segwit_address)
            addr20 = str(bitcoinlib.keys.Address(bit.Key.from_int(N-pvk*lmda%N).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            addr21 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk*lmda2%N)._pk.public_key.format(compressed=True)))
            addr22 = str(bit.format.public_key_to_address(bit.Key.from_int(N-pvk*lmda2%N)._pk.public_key.format(compressed=False)))
            addr23 = str(bit.Key.from_int(N-pvk*lmda2%N).segwit_address)
            addr24 = str(bitcoinlib.keys.Address(bit.Key.from_int(N-pvk*lmda2%N).public_key.hex(),encoding='bech32',script_type='p2wpkh').address)
            setaddr = set()
            setaddr = [addr1,addr2,addr3,addr4,addr5,addr6,addr7,addr8,addr9,addr10,addr11,addr12,addr13,addr14,addr15,addr16,addr17,addr18,addr19,addr20,addr21,addr22,addr23,addr24]
            for i in setaddr:
                if i in database:
                    print ('Congrats! Your key is here: ', privetkey)
                    f=open('/path_to_winner_file/winner.txt','a')
                    f.write(privetkey)
                    f.close()
                    txt1 = ('Private key in HEX = ', privetkey)
                    txt = str(txt1)
                    send_notification('your@email.com', txt)
        except:
            continue

# Multiprocess this
if __name__ == '__main__':
        for cpu in range(4):
            multiprocessing.Process(target = search).start()
