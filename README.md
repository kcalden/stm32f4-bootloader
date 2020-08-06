# STM32F4 UART Bootloader
STM32F4 UART Bootloader using the libraries from https://github.com/ferenc-nemeth/stm32-bootloader

## Function

1. On reset, the MCU sends a BEL character through the UART.
2. The host responds with an ACK character. If not, the bootloader jumps to the application code.
3. MCU responds with its type for verification before uploading.
4. If the host sends ACK, begin flashing. If host sends NAK or nothing, jump to the application code.

## Build options

The highest optimization level this should be built with is -O1. (This the highest level I've had success)