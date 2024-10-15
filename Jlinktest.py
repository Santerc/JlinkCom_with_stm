"""
 @file name:       Jlinktest.py
 @brief:           using pylink to communicate between NUC&STM32 test code V0.0
 @Author:          Santerc
 @Last Edit Time:  2024/10/14 18:05
 tested python version = 2.7.13 & 3.12.5 
"""

import time
import pylink
def main() :
    jlink = pylink.JLink()
    while 1 :
        try:
            # Initialization
            
            jlink.open(0)
            jlink.connect('Cortex-M3')

            jlink.swo_start(9600)
            
            address = 0x00000

            # Try to read
            while 1 :
                num = jlink.memory_read8(address, 1)[0]
                print("Congratulations! number at address {hex(address)} is : {num}")
                time.sleep(0.01)

        except pylink.errors.JLinkException as e:
            print("[JLink Debug Error]: {e}")
            time.sleep(1)
    
if __name__ == '__main__':
    main()
