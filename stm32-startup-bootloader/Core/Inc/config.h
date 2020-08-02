/*
 * config.h
 *
 *  Created on: Aug 2, 2020
 *      Author: Karl Calden
 */

#ifndef CONFIG_H_
#define CONFIG_H_

/* MCU ID */
#define F411RE
//#define F446RC
//#define F411RC

/* AUTO CONFIG */

// DEFINE SIZE OF THE FLASH MEMORY
#if defined(F411RC) | defined(F446RC)
#define FLASH_SIZE_256K
#elif defined(F411RE)
#define FLASH_SIZE_512K
#endif

#if  defined(FLASH_SIZE_512K)
#define USER_FLASH_END 0x8080000
#define NUM_USER_SECTORS 7
#elif defined(FLASH_SIZE_256K)
#define USER_FLASH_END 0x8040000
#define NUM_USER_SECTORS 5
#endif

#endif /* CONFIG_H_ */
