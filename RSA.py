p = 17
q = 23
e = 5
plaintext = "PhanHuynhSaLinh"

n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)  # modular inverse

# convert chars to integers
m_blocks = [ord(ch) for ch in plaintext]

# encrypt
c_blocks = [pow(m, e, n) for m in m_blocks]

# decrypt (verify)
decrypted_blocks = [pow(c, d, n) for c in c_blocks]
decrypted_text = ''.join(chr(m) for m in decrypted_blocks)

print("n =", n, "phi =", phi, "d =", d)
print("m_blocks =", m_blocks)
print("c_blocks =", c_blocks)
print("decrypted =", decrypted_text)

