#imports
from enigma.machine import EnigmaMachine

#Setup Enigma Machine
machine = EnigmaMachine.from_key_sheet(rotors='V III II', reflector='B', ring_settings='01 02 23', plugboard_settings='EI DY PO SJ FN LB RK QX AH CU')

machine.set_display('FNZ')

msg_key = machine.process_text('BFR')
print(msg_key)

plaintext = "RASPBERRYPI"
ciphertext = machine.process_text(plaintext)
print(ciphertext)