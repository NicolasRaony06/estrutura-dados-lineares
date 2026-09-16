# --- Writing raw bytes to a file ---
data_to_write = b"Hello, this is raw binary data!"  # The 'b' prefix creates a bytes object

with open("example.bin", "wb") as file:  # 'wb' = Write Binary
    file.write(data_to_write)

# --- Reading raw bytes from a file ---
with open("example.bin", "rb") as file:  # 'rb' = Read Binary
    binary_content = file.read()
    print(list(binary_content))  # Output: b'Hello, this is raw binary data!'

with open("example.bin", "rb") as file:
    content = file.read()
    
    # Print the integer value of each byte
    #print(list(content))  
    # Output: [72, 101, 108, 108, 111, ...] -> (72 is 'H', 101 is 'e'...)

    # Print the actual 0s and 1s (binary representation)
    binary_strings = [format(b, '08b') for b in content]
    print(" ".join(binary_strings))
    # Output: 01001000 01100101 01101100 01101100 01101111 ...

