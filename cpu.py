import interaction

class Final_interact(interaction.waifu_interaction):
    def interact(wife, User):
        if wife.type == 'loli':
            if wife.name == 'laura' and wife.personality == 'notloli':
                interaction.laura.laura_info()
                interaction.laura.send_help()
            else:
                interaction.Loli.info_loli(wife)
                interaction.Loli.godpow(wife)
                if wife.age >= 18:
                    interaction.Loli.breed_loli(wife)
                else:
                    if wife.name == 'lmu' and wife.personality == 'gamer':
                        interaction.lmu.fake_breed(wife)
                    else: interaction.Loli.correction(wife)
        elif wife.type == 'trap':
            interaction.Trap.trap_info(wife)
            interaction.Trap.breed_trap(wife)
        elif wife.type == 'malewife':
            if wife.name == 'ttm':
                interaction.ttm.info_ttm()
                interaction.ttm.breed_ttm(wife)
            else:
                interaction.Malewife.info_malewife(wife)
                interaction.Malewife.breed_malewife(wife)
        elif wife.type == 'bom':
            if wife.name == 'pnm' and wife.personality == 'pervert':
                interaction.pnm.pmn_info()
                if User.username == 'ttm':
                    interaction.pnm.breed_as_ttm(wife)
                else:
                    interaction.pnm.breed_pnm(wife)
              
            else:
                interaction.BOM.info_bom(wife)
                interaction.BOM.breed_bom(wife)
        elif wife.type == 'shouta':
            interaction.shouta.info_loli(wife)
            interaction.shouta.godpow(wife)
            if wife.age >= 18:
                interaction.shouta.breed_loli(wife)
            else:
                interaction.shouta.correction(wife)