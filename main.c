/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include "modules.h"

int main(){
  char *test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
  printf("%s\n", test);
  char *res = hex_to_base64(test);
  printf("%s\n", res);
  return 1;
}
