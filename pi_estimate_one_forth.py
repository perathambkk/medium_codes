#!/usr/bin/env python
# -- coding: utf-8 --
"""การประมาณค่าพายด้วยวิธี Monte Carlo
"""
import random
import math
num_samples = 100000 # จำนวนตัวอย่าง
r = 5.0 # รัศมีวงกลมหรือครึ่งหนึ่งของความยาวด้านของสี่เหลี่ยมจัตุรัส
a, b = 0, r # ช่วง [a, b] คือ [0, r]
in_circle = 0
for i in range(num_samples): # สุ่มไปเรื่อยๆ
    x = random.uniform(a, b)
    y = random.uniform(a, b)
    if x**2 + y**2 <= r**2: # หากอยู่ในวงกลมก็นับ
        in_circle += 1
print('[Result] pi estimation: {0:.5f}'.format(4*float(in_circle)/num_samples))