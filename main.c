/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include "modules.h"

int main(){

  printf("1. Hex to Base64\n");
  char *test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
  printf("%s\n", test);
  char *res = hex_to_base64(test);
  printf("%s\n\n", res);

  printf("2. Fixed XOR\n");
  char *buffer1 = "1c0111001f010100061a024b53535009181c";
  char *buffer2 = "686974207468652062756c6c277320657965";

  printf("buffer 1: %s\nbuffer 2: %s\n", buffer1, buffer2);
  printf("%s\n", fixed_xor(buffer1, buffer2) );

  return 1;
}
