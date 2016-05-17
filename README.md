# matasono_crypto
Description: Code for the matasano crypto challenges. C-language.

Author: Abraham Adberstein

1. **Hex to Base64**

  I took a hex string converting it into a binary string. Then, every six bits I converted them into
  into decimal. Each decimal is matched to its corresponding base64 character. Then all the characters
  are concatenated.

2. **Fixed XOR**

  When trying to xor to hex strings, I took each individual hex byte, converted it into decimal, xor it
  with the second hex byte. After that I encoded the integer into an ascii hex. Concatenated all ascii characters.
