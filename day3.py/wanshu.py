#!/usr/bin/env prthon

a = 1
while a <= 1000:
     j = 0
     i = 1
     while i < a:
         if a % i == 0:
             j = j + i
         i += 1
     if j == a:
         print "%d "%j
     a += 1
