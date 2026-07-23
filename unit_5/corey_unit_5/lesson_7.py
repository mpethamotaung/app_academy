"""All evaluate to False Values
- False
- None
- Zero of any numeric data type and parse into conditional
- Any empty sequence. For example: '',(), [].
- Any empty mapping. For exampel: {}
"""

condition = False #None, 0, '', (), [], {}

if condition:
    print('Evaluated to True')
else: 
    print('Evaluated to False')