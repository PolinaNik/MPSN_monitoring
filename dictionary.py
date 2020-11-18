import datetime
import pickle

router1 = {1: ['R05 - SDP3 - 1', 53],
           2: ['R06 - ZKU (Утес) - 1', 52],
           3: ['R07 - ORLA - 1', 51],
           4: ['R08 - SDP2 - 1', 50],
           5: ['R09 - KRM234 - 1', 49],
           6: ['R10 - GRM54 - 1', 48],
           7: ['R11 - BPRM234L - 1', 54],
           8: ['R12 - BPRM234R - 1', 55],
           9: ['R13 - PM (Прожек. мачта) - 1', 56],
           10: ['R14 - SHDA (Штаб. Даль Авиа) - 1', 57],
           11: ['R15 - AERO1 (Аэровокзал поз.1)', 58],
           12: ['R17 - ZAS (Зд.Аэрод.Служб.) - 1', 59],
           13: ['R18 - ZST (Зд.Служб.Спецтран.) - 1', 60],
           14: ['R21 - BPRM54 - 1', 61],
           15: ['R23 - TERM (Международный Аэр.) - 1', 62],
           16: ['R24 - SOSN (Сосновка) - 1', 11],
           17: ['R25 - DRUZ (Дружба) - 1', 10],
           18: ['R26 - ANAS (Анастасьевка) - 1', 6]}


router2 = {1: ['R09 - KRM234 - 2', 63],
           2: ['R10 - GRM54 - 2', 61],
           3: ['R11 - BPRM234L - 2', 53],
           4: ['R12 - BPRM234R - 2', 52],
           5: ['R16 - AERO2 (Аэровокзал поз.2)', 62],
           6: ['R17 - ZAS (Зд.Аэрод.Служб.) - 2', 60],
           7: ['R21 - BPRM54 - 2', 54],
           8: ['R24 - SOSN (Сосновка) - 2', 11],
           9: ['R25 - DRUZ (Дружба) - 2', 10],
           10: ['R27 - PREA (Преамурское) - 1', 6]}

router3 = {1: ['R05 - SDP3 - 2', 18],
           2: ['R06 - ZKU (Утес) - 2', 15],
           3: ['R07 - ORLA - 2', 16],
           4: ['R08 - SDP2 -2', 17],
           5: ['R26 - ANAS (Анастасьевка) - 2', 5],
           6: ['R27 - PREA (Преамурское) - 2', 6]}


router4 = {1: ['R19 - TRAP (Пл.сущ.трапной) - 1', 12],
           2: ['R20 - KTPN31 - 1', 9],
           3: ['R22 - TP3A - 1', 10]}

  updatetime, IT

rx1 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0', 7: '0', 8: '0', 9: '0',
      10: '0', 11: '0', 12: '0', 13: '0', 14: '0', 15: '0', 16: '0',
      17: '0', 18: '0'}

rx2 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0', 7: '0', 8: '0', 9: '0',
      10: '0'}

rx3 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0'}

rx4 = {1: '0', 2: '0', 3: '0'}

tx1 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0', 7: '0', 8: '0', 9: '0',
      10: '0', 11: '0', 12: '0', 13: '0', 14: '0', 15: '0', 16: '0',
      17: '0', 18: '0'}

tx2 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0', 7: '0', 8: '0', 9: '0',
      10: '0'}

tx3 = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0'}

tx4 = {1: '0', 2: '0', 3: '0'}

updatetime1 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
              3: datetime.datetime.today(), 4: datetime.datetime.today(),
              5: datetime.datetime.today(), 6: datetime.datetime.today(),
              7: datetime.datetime.today(), 8: datetime.datetime.today(),
              9: datetime.datetime.today(), 10: datetime.datetime.today(),
              11: datetime.datetime.today(), 12: datetime.datetime.today(),
              13: datetime.datetime.today(), 14: datetime.datetime.today(),
              15: datetime.datetime.today(), 16: datetime.datetime.today(),
              17: datetime.datetime.today(), 18: datetime.datetime.today()}

updatetime2 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
              3: datetime.datetime.today(), 4: datetime.datetime.today(),
              5: datetime.datetime.today(), 6: datetime.datetime.today(),
              7: datetime.datetime.today(), 8: datetime.datetime.today(),
              9: datetime.datetime.today(), 10: datetime.datetime.today()}

updatetime3 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
              3: datetime.datetime.today(), 4: datetime.datetime.today(),
              5: datetime.datetime.today(), 6: datetime.datetime.today()}

updatetime4 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
              3: datetime.datetime.today()}


IT1 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
      3: datetime.datetime.today(), 4: datetime.datetime.today(),
      5: datetime.datetime.today(), 6: datetime.datetime.today(),
      7: datetime.datetime.today(), 8: datetime.datetime.today(),
      9: datetime.datetime.today(), 10: datetime.datetime.today(),
      11: datetime.datetime.today(), 12: datetime.datetime.today(),
      13: datetime.datetime.today(), 14: datetime.datetime.today(),
      15: datetime.datetime.today(), 16: datetime.datetime.today(),
      17: datetime.datetime.today(), 18: datetime.datetime.today()}

IT2 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
      3: datetime.datetime.today(), 4: datetime.datetime.today(),
      5: datetime.datetime.today(), 6: datetime.datetime.today(),
      7: datetime.datetime.today(), 8: datetime.datetime.today(),
      9: datetime.datetime.today(), 10: datetime.datetime.today()}

IT3 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
      3: datetime.datetime.today(), 4: datetime.datetime.today(),
      5: datetime.datetime.today(), 6: datetime.datetime.today()}

IT4 = {1: datetime.datetime.today(), 2: datetime.datetime.today(),
      3: datetime.datetime.today()}

add_in_table1 = {}
add_in_table2 = {}
add_in_table3 = {}
add_in_table4 = {}

check1 = {}
check2 = {}
check3 = {}
check4 = {}
