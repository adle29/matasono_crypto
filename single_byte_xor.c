/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "modules.h"

void single_byte_xor(char *hexString){
  int elements = 16;
  char hex[16] = {'0','1','2', '3', '4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f'};
  int length = strlen(hexString);
  int i, j;

  for ( i = 0; i < elements; i++){
    char buffer[length];
    char letter = hex[i];

    for ( j = 0; j < length; j++)
        buffer[j] = letter;

    buffer[length] = '\0';

    //xor string
    char *result = fixed_xor(hexString, buffer);
    printf("buffer 1: %s\nbuffer 2: %s\n", buffer, hexString);
    printf("%s\n\n", result );

  }

  char *buffer = "58585858585858585858585858585858585858585858585858585858585858585858";
  char *result = fixed_xor(hexString, buffer);
  printf("buffer 1: %s\nbuffer 2: %s\n", buffer, hexString);
  printf("%s\n\n", result );
}
