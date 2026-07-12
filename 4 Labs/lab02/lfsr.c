#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include "lfsr.h"

void lfsr_calculate(uint16_t *reg) {
    uint16_t val = ((*reg & 1 << 5)  >> 5 ^ ((*reg & 1 << 3)  >> 3 ^ ((*reg & 1 << 2) >> 2 ^ (*reg & 1))));
    *reg = *reg >> 1;
    if (val) {
        *reg |= (val << 15);      // force bit n to 1
    } else {
        *reg &= ~(val << 15);     // force bit n to 0
    }
}

