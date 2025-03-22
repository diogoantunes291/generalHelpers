import re
from re import *
from datetime import *


def strip(txt):
    #txt = txt.strip().replace('“','')
    #txt = txt.strip().replace('”','')
    txt = txt.strip().replace('>','')
    txt = txt.strip().replace('\"','')
    txt=txt.replace("\n",'')
    txt=txt.replace("\t",'')
    txt=txt.replace("\r",'')
    txt=txt.replace("\v",'')
    txt=txt.replace("  ",' ')
    txt=txt.replace("  ",' ')
    return txt

def removeMiddleSpaces(txt):
    return txt.replace(" ","")

def convert_roman_number(roman):
    roman_numbers = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
                "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    
    i = 0
    result = 0
    while i < len(roman):
        # checks if there's a number like "IV" to convert to 4 and not I + V
        if i + 1 < len(roman) and roman[i:i+2] in roman_numbers:
            result += roman_numbers[roman[i:i+2]]
            i += 2 
        else:
            result += roman_numbers[roman[i]]
            i += 1
    
    return result

def stripList(repeatedItem:list[str]):
    for i in range (0,len(repeatedItem)):
            repeatedItem[i] =  repeatedItem[i].strip()

