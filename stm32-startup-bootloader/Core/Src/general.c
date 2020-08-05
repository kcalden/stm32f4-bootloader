/*
 * general.c
 *
 *  Created on: Aug 2, 2020
 *      Author: kcald
 */

#include "general.h"

int str_cmp(uint8_t * s1, uint8_t * s2, unsigned int length) {
	int match = 1;

	for(int i = 0; i<length; i++) {
		if(s1[i] != s2[i]) {
			match = 0;
			break;
		}
	}
	return match;
}
