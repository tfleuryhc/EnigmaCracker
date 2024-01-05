ciphertext = 'YJPYITREDSYUPIU'
cribtext = 'THISXISXWORKING'

rotors = ["I II III", "I II IV", "I II V", "I III II",
"I III IV", "I III V", "I IV II", "I IV III",
"I IV V", "I V II", "I V III", "I V IV",
"II I III", "II I IV", "II I V", "II III I",
"II III IV", "II III V", "II IV I", "II IV III",
"II IV V", "II V I", "II V III", "II V IV",
"III I II", "III I IV", "III I V", "III II I",
"III II IV", "III II V", "III IV I", "III IV II",
"III IV V", "IV I II", "IV I III", "IV I V",
"IV II I", "IV II III", "IV I V", "IV II I",
"IV II III", "IV II V", "IV III I", "IV III II",
"IV III V", "IV V I", "IV V II", "IV V III",
"V I II", "V I III", "V I IV", "V II I",
"V II III", "V II IV", "V III I", "V III II",
"V III IV", "V IV I", "V IV II", "V IV III"]

def find_rotor_start(rotor_choice, ciphertext, cribtext):
    from enigma.machine import EnigmaMachine
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    machine = EnigmaMachine.from_key_sheet(rotors=rotor_choice, reflector="B", ring_settings="1 1 1", plugboard_settings="AV BS CG DL FU HZ IN KM OW RX")
    
    
    for rotor1 in alphabet:
        for rotor2 in alphabet:
            for rotor3 in alphabet:
                
                start_pos = rotor1 + rotor2 + rotor3
                
                machine.set_display(start_pos)
                
                plaintext = machine.process_text(ciphertext)
                print(plaintext)
                
                if plaintext == cribtext:
                    print("Valid settings found!")
                    return rotor_choice, start_pos
    
    return rotor_choice, "Cannot find settings"
                     

for i in rotors:
    rotor_choice, start_pos = find_rotor_start(i, ciphertext, cribtext)
    print(rotor_choice + " " + start_pos)
    if start_pos != "Cannot find settings":
        break


                     