#!/usr/bin/env python3

print ("badchars=")
print ("(\"",end='')
[print ("\\x%02x" %i, end='') for i in range(0, 16)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(16, 32)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(32, 48)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(48, 64)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(64, 80)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(80, 96)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(96, 112)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(112, 128)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(128, 144)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(144, 160)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(160, 176)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(176, 192)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(192, 208)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(208, 224)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(224, 240)]
print ("\")")
print ("(\"", end='')
[print ("\\x%02x" %i, end='') for i in range(240, 256)]
print ("\")")
