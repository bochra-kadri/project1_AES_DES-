# utils.py
def pad(data, block_size):
    while len(data) % block_size != 0:
        data += b' '
    return data