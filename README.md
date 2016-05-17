# matasono_crypto
Description: Code for the matasano crypto challenges. C-language.

Author: Abraham Adberstein

1. **Hex to Base64**

  I took a hex string converting it into a binary string. Then, every six bits I converted them into
  into decimal. Each decimal is matched to its corresponding base64 character. Then all the characters
  are concatenated.

2. **Fixed XOR**

  When trying to xor two hex strings, take each individual hex byte, convert it into decimal, and xor it
  with the second hex byte. After that encode the integer into an ascii hex. Concatenate all ascii characters.

3. **Single Byte XOR Cipher**
  Use the code from the Fixed XOR challenge to find the plaintext. After trying single characters, X was the
  key to xor the cipher-text. Then the cipher-text had to be encoded into ascii. 
