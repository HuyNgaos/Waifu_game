import tecinical_logic as lg
import interaction

class breeding_waifu():
    def interact_breed(wife, breed_status, admin, sound):
        vanila = False
        nat = f'Narrator: You breed your {wife.type}'
        ending = {'waifu': wife.type}
        if breed_status:
            sound.play()
            match wife.type:
                case 'loli':
                    if (lg.legal.legal_age(wife)):
                        noises = interaction.loli.legal_breed(wife)
                        vanila = True
                        ending['route'] = 'legal breeding'
                    else:
                        nat = 'Narrator: You correct the brat'
                        noises = interaction.loli.correction(wife)
                        ending['route'] = 'horny jail'
                case 'trap':
                    noises = interaction.trap.breed_trap(wife)
                    vanila = True
                    ending['route'] = 'Bred'
                case 'malewife':
                    noises = interaction.malewife.breed_mw(wife)
                    vanila = True
                    ending['route'] = 'Bred'
                case 'bom':
                    noises = interaction.bom.breed_bom(wife)
                    vanila = True
                    ending['route'] = 'Bred'
                case 'shouta':
                    noises = interaction.shouta.breed_shouta(wife)
                    vanila = True
                    ending['route'] = 'Bred'
                case _:
                    print("Testin'")
                    ending['route'] = 'Test'
                    return "Test_Dummy", vanila, nat, ending
        else:
            vanila = True
            nat = f"Narrator: Oh, you don't breed your {wife.type}. Ok"
            ending['route'] = 'No breed (boring)'
            noises = ''
            match wife.type:
                case 'loli':
                    if (lg.legal.legal_age(wife)):
                        pass
                    else:
                        nat = "Narrator: Good choice. (Unload gun)"
                        ending['route'] = 'No Horny'
                case 'bom':
                    nat = f'Narrator: Poor the big old man, he got rejected at such an old age of {wife.age}'
        if admin:
            lg.admin_log.log(breed_choice = breed_status, noises = noises, ending = ending)
        return noises, vanila, nat, ending
    
    def interact_result(wife, admin):
        result = 'You had a good time'
        force_loop = False
        match wife.type:
            case 'loli':
                if (lg.legal.legal_age(wife)):
                    result = interaction.loli.legal_finished(wife)
                else:
                    result = interaction.loli.illegal_finished(wife)
            case 'trap':
                result = interaction.trap.trap_finished(wife)
            case 'malewife':
                result = interaction.malewife.malewife_finished(wife)
            case 'bom':
                result = interaction.bom.bom_finished(wife)
            case 'shouta':
                result = interaction.shouta.legal_finished(wife)
            case _:
                print("Testin'")
                return "Testing", force_loop
        if admin:
            lg.admin_log.log(result = result, force_loop = force_loop)
        return result, force_loop