/**
 * @file main.c
 * @author Ashutosh Singh Parmar (ashutoshsingh291999@gmail.com)
 * @brief This file simply blinks the on-board led
 * @version 0.1
 * @date 2022-05-21
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include "pico/stdlib.h"
#include "pico/binary_info.h"

#include "main.h"

int main() {

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    
    while (1) {
        gpio_put(LED_PIN, 0);
        sleep_ms(250);
        gpio_put(LED_PIN, 1);
        sleep_ms(1000);
    }
}