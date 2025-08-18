
#Kinich
Nome = 'Kinich'
VidaBase = 12858
AtaqueChar = 332
AtaqueArma = weapons.earthshaker_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 802
StatusAscensao = 0.384
#---------------------------------se
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +35 +18 +51 +sups.benny_ult
AtaquePorc = 0 +weapons.earthshaker_stat +resso_pyro +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +0.14 +0.14 +0.078 +0.062 +0.08 +StatusAscensao
CritRate = 0 +0.25 +relics.codice_obsidiana_4
BonusElm = 0 +relics.codice_obsidiana_2 +relics.perg_hero_4 +sups.mavuika_buff
BonusFis = 0
BonusAA = 0 +0.15
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0 +weapons.earthshaker_p1
BonusUlt = 0
#--------------------------------------
Talento = 3.2*AtaqueTotal
SkillDisparos = AtaqueTotal*1.03*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
SkillCanhaoBuffado = (AtaqueTotal*12.37+Talento)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
SkillCanhao = (AtaqueTotal*12.37)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
Ult = AtaqueTotal*2.05*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = ((SkillDisparos*4+SkillCanhaoBuffado+Ult)*1)+((SkillDisparos*4+SkillCanhao+Ult)*3)
print('< Talentos >')
print(f'Skill (AA): {int(SkillDisparos)}')
print(f'Skill (canhao 1): {int(SkillCanhaoBuffado)}')
print(f'Skill (canhao 2/3/4): {int(SkillCanhao)}')
print(f'Ult (laser): {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(DPR)}')

#Gaming
Nome = 'Gaming'
VidaBase = 11419
AtaqueChar = 302
AtaqueArma = weapons.serp_spine_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 703
StatusAscensao = 0.24
#--------------------------------------
C2 = 0.2
C6_1 = 0.2
C6_2 = 0.4
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +33 +sups.benny_ult
AtaquePorc = 0 +StatusAscensao +0.082 +0.11 +0.157 +0.152 +resso_pyro +relics.ritual_real_4 +C2
DefesaFlat = 0
DefesaPorc = 0
EM = 0 + 37
RecargaPorc = 0
CritDmg = 0 +0.256 +0.202 +0.07 +0.109
CritRate = 0 +0.035 +0.035 +0.07 +0.035 +weapons.serp_spine_stat 
BonusElm = 0 +weapons.serp_spine_p1 +relics.bruxa_chamas_2 +sups.yelan_passiva +sups.kazuha_buff
BonusFis = 0
BonusAA = 0
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
#--------------------------------------
Passiva = 0.2
Suporte = sups.xianyun_ult*0
AtaqueNormal_H1 = AtaqueTotal*1.54*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueNormal_H2 = AtaqueTotal*1.45*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
SkillImersivo = (AtaqueTotal*4.89+Suporte)*(1+DanoElemental+BonusSkill+BonusImersivo+Passiva)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = AtaqueTotal*6.29*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
print('< Talentos >')
print(f'Ataque Normal (H1)): {int(AtaqueNormal_H1)}')
print(f'Ataque Normal (H2)): {int(AtaqueNormal_H2)}')
print(f'Skill (imersivo): {int(SkillImersivo)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(Ult+(AtaqueNormal_H1+AtaqueNormal_H2+SkillImersivo)*5)}')

#Neuvillette
Nome = 'Neuvillette'
VidaBase = 14695
AtaqueChar = 208
AtaqueArma = weapons.jade_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 576
StatusAscensao = 0.384
#--------------------------------------
Passiva2 = 0.3
VidaFlat = 0 +448 +478 +538 +747
VidaPorc = 0 +0.11 +0.087 +weapons.jade_p1 +resso_hydro
AtaqueFlat = 0 
AtaquePorc = 0 
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +StatusAscensao +0.2 +0.054 +0.132 +0.07
CritRate = 0 +0.027 +0.128 +0.035 +weapons.jade_stat +relics.cacador_sombras_4
BonusElm = 0 +Passiva2 +sups.furina_ult +sups.kazuha_buff +relics.perg_hero_4
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0 +relics.cacador_sombras_2
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
#--------------------------------------
Passiva1 = 1.25
AtaqueCarregado = VidaTotal*0.1447*(1+DanoElemental+BonusCarregado+Passiva1)*EnemyReduct*(1+DanoCritico)
Skill = VidaTotal*0.2316*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
UltOnda = VidaTotal*0.4006*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
UltCachoeira = VidaTotal*0.1639*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico) 
print('< Talentos >')
print(f'Ataque Carregado: {int(AtaqueCarregado)}')
print(f'Skill: {int(Skill)}')
print(f'Ult (onda): {int(UltOnda)}')
print(f'Ult (cachoeira): {int(UltCachoeira)}')
print('')
print(f'Dano Rotacao: {int(UltOnda+UltCachoeira+Skill+(AtaqueCarregado*8*3))}')

#Ayaka
Nome = 'Ayaka'
VidaBase = 12858
AtaqueChar = 342
AtaqueArma = weapons.epi_prof_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 784
StatusAscensao = 0.384
#--------------------------------------
Passiva1 = 0.3
Passiva2 = 0.18
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +35 +51 +14 #+weapons.epi_prof_p2
AtaquePorc = 0 +0.157 +0.099 +0.163 +relics.ritual_real_4 +weapons.epi_prof_stat +weapons.epi_prof_p1
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +0.132 +0.109 +0.124 +StatusAscensao
CritRate = 0 +0.07 +0.117 +resso_cryo +relics.heroi_invernal_4
BonusElm = 0 +Passiva2 +relics.heroi_invernal_2 +sups.kazuha_buff +sups.furina_ult
BonusFis = 0
BonusAA = 0 +Passiva1
BonusCarregado = 0 +Passiva1
BonusImersivo = 0
BonusSkill = 0 
BonusUlt = 0
#--------------------------------------
AtaqueNormal_H1 = AtaqueTotal*0.9*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
AtaqueNormal_H2 = AtaqueTotal*0.96*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
AtaqueCarregado = (AtaqueTotal*1.08*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico))*3
Skill = AtaqueTotal*4.3*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
Ult = AtaqueTotal*2.02*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
print('< Talentos >')
print(f'Ataque Normal (H1): {int(AtaqueNormal_H1)}')
print(f'Ataque Normal (H2): {int(AtaqueNormal_H2)}')
print(f'Ataque Carregado: {int(AtaqueCarregado)}')
print(f'Skill: {int(Skill)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(AtaqueNormal_H1+AtaqueNormal_H2+AtaqueCarregado+Skill+(Ult*20))}')

#Ganyu
Nome = 'Ganyu'
VidaBase = 9797
AtaqueChar = 335
AtaqueArma = weapons.amos_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 630
StatusAscensao = 0.384
#--------------------------------------
Passiva = 0.2
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +35 +51 +14 +sups.benny_ult
AtaquePorc = 0 +0.157 +0.099 +0.163 +weapons.amos_stat +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +relics.trupe_iti_2
RecargaPorc = 0
CritDmg = 0 +0.132 +0.109 +0.124 +StatusAscensao
CritRate = 0 +0.25 +resso_cryo +0.2
BonusElm = 0 +Passiva +weapons.amos_p2 +sups.kazuha_buff
BonusFis = 0
BonusAA = 0
BonusCarregado = 0 +weapons.amos_p1 +relics.trupe_iti_4
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
#--------------------------------------
AtaqueCarregadoFlecha = AtaqueTotal*2.3*(1+DanoElemental+BonusCarregado)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueCarregadoExplosao = AtaqueTotal*3.91*(1+DanoElemental+BonusCarregado)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = AtaqueTotal*1.26*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
print('< Talentos >')
print(f'Ataque Carregado (flecha)): {int(AtaqueCarregadoFlecha)}')
print(f'Ataque Carregado (explosao)): {int(AtaqueCarregadoExplosao)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int((Ult+AtaqueCarregadoExplosao+AtaqueCarregadoFlecha)*4)}')

#Xiangling
Nome = 'Xiangling'
VidaBase = 10875
AtaqueChar = 225
AtaqueArma = weapons.fisgada_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 669
StatusAscensao = 96
#--------------------------------------
C1 = 0.15
C6 = 0.15
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +sups.benny_ult
AtaquePorc = 0 +0.3 +resso_pyro +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +StatusAscensao
RecargaPorc = 0 +0.5 +weapons.fisgada_stat +relics.selo_2
CritDmg = 0 +0.5
CritRate = 0 +weapons.fisgada_p2 +0.2
BonusElm = 0 +C6 +sups.furina_ult
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0 +weapons.fisgada_p1 +relics.selo_4
#--------------------------------------
Skill = AtaqueTotal*2.36*(1+DanoElemental+BonusSkill)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = AtaqueTotal*2.38*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
print('< Talentos >')
print(f'Skill: {int(Skill)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int((Ult)*7)}')

#Hutao
Nome = 'Hutao'
VidaBase = 15552
AtaqueChar = 106
AtaqueArma = weapons.perd_drag_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 876
StatusAscensao = 0.384
#--------------------------------------
Passiva = 0.33
VidaFlat = 0
VidaPorc = 0 +0.3 +resso_hydro
BuffSkill = 0.0626*((VidaBase*(1+(AreiaVida_S*AreiaVida)+(CaliceVida_S*CaliceVida)+(CoroaVida_S*CoroaVida)+VidaPorc))+FlorVida+VidaFlat)
if(BuffSkill>(AtaqueBase*4)):
    BuffSkill = AtaqueBase*4
AtaqueFlat = 0 +BuffSkill
AtaquePorc = 0 +0.3
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +weapons.perd_drag_stat
RecargaPorc = 0
CritDmg = 0 +0.6 +StatusAscensao
CritRate = 0 +0.20
BonusElm = 0 +Passiva +relics.bruxa_chamas_2 +0.075 +sups.furina_ult +sups.yelan_passiva +weapons.perd_drag_p1
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
#--------------------------------------
AtaqueNormal = AtaqueTotal*0.8365*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueCarregado = AtaqueTotal*2.42*(1+DanoElemental+BonusCarregado)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = AtaqueTotal*6.17*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
print('< Talentos >')
print(f'Ataque Normal: {int(AtaqueNormal)}')
print(f'Ataque Carregado: {int(AtaqueCarregado)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(Ult+(AtaqueNormal+AtaqueCarregado)*10)}')

#Chasca
Nome = 'Chasca'
VidaBase = 9797
AtaqueChar = 346
AtaqueArma = weapons.cancao_silencio_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 614
StatusAscensao = 0.192
#--------------------------------------
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +sups.benny_ult
AtaquePorc = 0 +0.3 +weapons.cancao_silencio_stat +relics.ritual_real_4 +relics.milelith_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +100
RecargaPorc = 0
CritDmg = 0 +0.4 +sups.faruzan_c6
CritRate = 0 +0.25 +StatusAscensao
BonusElm = 0 +weapons.cancao_silencio_p1 +relics.cronicas_deserto_2 +sups.furina_ult
BonusFis = 0
BonusAA = 0 +relics.cronicas_deserto_4
BonusCarregado = 0 +relics.cronicas_deserto_4
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusAditivo = 0
#--------------------------------------
Passiva1 = 0.65 #(stacks = 0.15/0.35/0.65)
Skill_NormalShots = (AtaqueTotal*0.87+BonusAditivo)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
Skill_ShineShots = (AtaqueTotal*3+BonusAditivo)*(1+DanoElemental+BonusCarregado+Passiva1)*EnemyReduct*(1+DanoCritico)
Ult_NormalShells = (AtaqueTotal*1.86+BonusAditivo)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
Ult_RadiantShells = (AtaqueTotal*3.72)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = Ult_NormalShells*2+Ult_RadiantShells*4+(Skill_NormalShots*2+Skill_ShineShots*4)*4
print('< Talentos >')
print(f'Skill (N-shots): {int(Skill_NormalShots)}')
print(f'Skill (S-shots): {int(Skill_ShineShots)}')
print(f'Ult (N-shells): {int(Ult_NormalShells)}')
print(f'Ult (R-shells): {int(Ult_RadiantShells)}')
print('')
print(f'DPR: {int(DPR)}')

#Ororon
Nome = 'Ororon'
VidaBase = 9244
AtaqueChar = 244
AtaqueArma = weapons.ultimo_acorde_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 586 
StatusAscensao = 0.24
#--------------------------------------
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 
AtaquePorc = 0 +StatusAscensao +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +weapons.ultimo_acorde_stat +200
RecargaPorc = 0
CritDmg = 0 +0.5
CritRate = 0 +0.20
BonusElm = 0 
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0 +weapons.ultimo_acorde_p1
BonusUlt = 0 +weapons.ultimo_acorde_p1 +relics.ritual_real_2
#--------------------------------------
Skill = AtaqueTotal*4.19*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
Ult = AtaqueTotal*0.7*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
Passiva = AtaqueTotal*1.3*(1+DanoElemental)*EnemyReduct*(1+DanoCritico)
Reacao = MultTrans
DPR = Skill+(Ult*12)+(Passiva*6)+(Reacao*6)
print('< Talentos >')
print(f'Skill: {int(Skill)}')
print(f'Ult: {int(Ult)}')
print(f'Passiva: {int(Passiva)}')
print(f'Reacao: {int(Reacao)}')
print('')
print(f'DPR: {int(DPR)}')

#Ayato
Nome = 'Ayato'
VidaBase = 13715
AtaqueChar = 299
AtaqueArma = weapons.cal_eshu_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 769
StatusAscensao = 0.384
#--------------------------------------
Buff_Ult = 0.2
VidaFlat = 0 +1000
VidaPorc = 0 +0.2
AtaqueFlat = 0
AtaquePorc = 0 +weapons.cal_eshu_stat +0.3 +relics.sonho_ninfa_4_2 +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +sups.diona_c6
RecargaPorc = 0
CritDmg = 0 +StatusAscensao +0.4
CritRate = 0 +weapons.cal_eshu_p2 +0.25
BonusElm = 0 +relics.sonho_ninfa_2 +relics.sonho_ninfa_4_1 +resso_geo +relics.perg_hero_4
BonusFis = 0
BonusAA = 0 +weapons.cal_eshu_p1 +Buff_Ult +sups.yunjin_c2
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusAditivo = 0 +sups.yunjin_ult
#--------------------------------------
Skill_Passiva = 0.011*VidaTotal*4 #stack máximo = 4
Skill_H1 = (AtaqueTotal*1.04+BonusAditivo+Skill_Passiva)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
Skill_H2 = (AtaqueTotal*1.16+BonusAditivo+Skill_Passiva)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
Skill_H3 = (AtaqueTotal*1.28+BonusAditivo+Skill_Passiva)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = (AtaqueTotal*1.19+BonusAditivo)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = (Skill_H1+Skill_H2+Skill_H3)*6
print('< Talentos >')
print(f'Skill (hit 1): {int(Skill_H1)}')
print(f'Skill (hit 2): {int(Skill_H2)}')
print(f'Skill (hit 3): {int(Skill_H3)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'DPR: {int(DPR)}')

#Mavuika
Nome = 'Mavuika'
VidaBase = 12552
AtaqueChar = 358
AtaqueArma = weapons.blacklif_foice_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 791
StatusAscensao = 0.38
#--------------------------------------
PassivaBuff = 0.5
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +37 +33 +14 +sups.iansan_ult 
AtaquePorc = 0 +0.14 +0.16 +0.09 +resso_pyro +relics.ritual_real_4 +sups.iansan_c2 +sups.chev_buff
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +0.21 +0.07 +0.13 +0.11 +StatusAscensao +weapons.blacklif_foice_stat
CritRate = 0 +0.6
BonusElm = 0 +relics.perg_hero_4 +PassivaBuff +sups.chev_c6
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusAditivo = 0
#--------------------------------------
UltBuffExplosion = 0.0288*AtaqueTotal*200
UltBuffMotoHits = 0.0051*AtaqueTotal*200
UltBuffMotoCharg = 0.0102*AtaqueTotal*200
SkillRemote = (AtaqueTotal*2.3+BonusAditivo)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
SkillCharg = (AtaqueTotal*1.955+BonusAditivo+UltBuffMotoCharg)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
Ult = (AtaqueTotal*8+BonusAditivo+UltBuffExplosion)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = (SkillCharg)*8+(SkillRemote)*6+Ult
print('< Talentos >')
print(f'SkillRemote: {int(SkillRemote)}')
print(f'SkillCharged: {int(SkillCharg)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'DPR: {int(DPR)}')

#Viajante Pyro
Nome = 'Viajante Pyro'
VidaBase = 10875
AtaqueChar = 212
AtaqueArma = weapons.chuva_floral_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 682
StatusAscensao = 0.24
#--------------------------------------
c1 = 0.12
c4 = 0.2
c6 = 0.4
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +sups.benny_ult
AtaquePorc = 0 +StatusAscensao +resso_pyro +0.5 +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +weapons.chuva_floral_stat +100
RecargaPorc = 0
CritDmg = 0 +c6 +0.4
CritRate = 0 +0.25 +relics.codice_obsidiana_4
BonusGeral = 0 +weapons.chuva_floral_p1 +c1 +relics.codice_obsidiana_2
BonusElm = 0 +c4 +sups.benny_c6 +relics.perg_hero_4
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusAditivo = 0
#--------------------------------------
AtaqueNormal1 = (AtaqueTotal*1.06+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueNormal2 = (AtaqueTotal*1.04+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueNormal3 = (AtaqueTotal*1.26+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueNormal4 = (AtaqueTotal*1.39+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueNormal5 = (AtaqueTotal*1.69+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
Skill = (AtaqueTotal*1.94+BonusAditivo)*(1+DanoElemental+BonusSkill)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = (AtaqueTotal*9+BonusAditivo)*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
DPR = (AtaqueNormal1+AtaqueNormal2+AtaqueNormal3+AtaqueNormal4+AtaqueNormal5)*3+Skill*5+Ult
print('< Talentos >')
print(f'Ataque Normal (H1): {int(AtaqueNormal1)}')
print(f'Ataque Normal (H2): {int(AtaqueNormal2)}')
print(f'Ataque Normal (H3): {int(AtaqueNormal3)}')
print(f'Ataque Normal (H4): {int(AtaqueNormal4)}')
print(f'Ataque Normal (H5): {int(AtaqueNormal5)}')
print(f'Skill: {int(Skill)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'DPR: {int(DPR)}')

#Citlali
Nome = 'Citlali'
VidaBase = 11634
AtaqueChar = 126
AtaqueArma = weapons.mem_sac_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 763
StatusAscensao = 115
#--------------------------------------
VidaFlat = 0
VidaPorc = 0 +relics.milelith_2
AtaqueFlat = 0 
AtaquePorc = 0 +0.5 +relics.milelith_4_1
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +StatusAscensao +weapons.mem_sac_stat +200
RecargaPorc = 0
CritDmg = 0 
CritRate = 0 +resso_cryo +0.25
BonusElm = 0 
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusP1 = 0.9*((AreiaEM_S*AreiaEM)+(CaliceEM_S*CaliceEM)+(CoroaEM_S*CoroaEM)+EM)
BonusP2 = 24*((AreiaEM_S*AreiaEM)+(CaliceEM_S*CaliceEM)+(CoroaEM_S*CoroaEM)+EM)
BonusAditivo = 0
#--------------------------------------
SkillShield = (10.36*MaestriaElemental+3050)*(1+relics.milelith_4_2)
SkillHits = (AtaqueTotal*0.3+BonusP1)*(1+DanoElemental+BonusSkill)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = (AtaqueTotal*9.67+BonusP2)*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)
DPR = SkillHits*10+Ult
print('< Talentos >')
print(f'Skill (shield): {int(SkillShield)}')
print(f'Skill (hits): {int(SkillHits)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'DPR: {int(DPR)}')


#Sethos
Nome = 'Sethos'
VidaBase = 9787
AtaqueChar = 227
AtaqueArma = weapons.estlg_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 560
StatusAscensao = 96
#--------------------------------------
Sethos_C2 = 0.3
VidaFlat = 0 
VidaPorc = 0
AtaqueFlat = 0 +51 +27 +62 +27 +sups.iansan_ult
AtaquePorc = 0 +0.093 +sups.iansan_c2 +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +StatusAscensao +resso_dendro +relics.trupe_iti_2 +58 +sups.nahida_buff
RecargaPorc = 0
CritDmg = 0 +0.179 +0.241 +0.249 +0.117
CritRate = 0 +weapons.estlg_stat +0.039 +0.058 +0.035 +0.062
BonusElm = 0 +weapons.estlg_p1 +Sethos_C2 +relics.perg_hero_4 +sups.iansan_c6
BonusFis = 0
BonusAA = 0 
BonusCarregado = 0 +relics.trupe_iti_4
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
#--------------------------------------
BonusAditivo = 0 +(3.53*MaestriaElemental)+AddCat
AtaqueCarregado_H1 = (AtaqueTotal*0.96+BonusAditivo)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
AtaqueCarregado_H2 = (AtaqueTotal*0.43+BonusAditivo)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
AtaqueCarregado_H3 = (AtaqueTotal*0.48+BonusAditivo)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
AtaqueCarregado_H4 = (AtaqueTotal*1.35+BonusAditivo)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
DPR = (AtaqueCarregado_H1+AtaqueCarregado_H2+AtaqueCarregado_H3+AtaqueCarregado_H4)*4
print('< Talentos >')
print(f'Flecha Crepusculo H1: {int(AtaqueCarregado_H1)}')
print(f'Flecha Crepusculo H2: {int(AtaqueCarregado_H2)}')
print(f'Flecha Crepusculo H3: {int(AtaqueCarregado_H3)}')
print(f'Flecha Crepusculo H4: {int(AtaqueCarregado_H4)}')
print('')
print(f'DPR: {int(DPR)}')

#Skirk
Nome = 'Skirk'
VidaBase = 12417
AtaqueChar = 358.77
AtaqueArma = weapons.blacksword_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 806
StatusAscensao = 0.384
tal_buff_aa = 0.7
tal_buff_ult = 0.6 
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0  
AtaquePorc = 0 +0.5
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +StatusAscensao +0.5
CritRate = 0 +0.25 +resso_cryo +weapons.blacksword_stat
BonusElm = 0 +relics.epi_cor_2 +sups.furina_ult
BonusFis = 0
BonusAA = 0 +tal_buff_aa +relics.epi_cor_4 +weapons.blacksword_p1
BonusCarregado = 0 
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0 +tal_buff_ult +relics.epi_cor_4
BonusAditivo = 0
StackSerpent = 12 #max=12
Ult_B1 = (0.347*AtaqueTotal)*StackSerpent
StackVoid = 3 #max=3
Ult_B2 = (StackVoid+2)*0.04
BonusAA = BonusAA + Ult_B2
Skill_H1 = (AtaqueTotal*2.62+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
Skill_H2 = (AtaqueTotal*2.36+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
Skill_H3 = (AtaqueTotal*1.49+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
Skill_H4 = (AtaqueTotal*1.59+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
Skill_H5 = (AtaqueTotal*3.88+BonusAditivo)*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
Ult_H1 = (AtaqueTotal*2.20+BonusAditivo+Ult_B1)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
Ult_H2 = (AtaqueTotal*3.68+BonusAditivo+Ult_B1)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = (Ult_H1*5)+Ult_H2+(Skill_H1+Skill_H2+(Skill_H3*2)+(Skill_H4*2)+Skill_H5)*2
print('< Talentos >')
print(f'Hit 1: {int(Skill_H1)}')
print(f'Hit 2: {int(Skill_H2)}')
print(f'Hit 3: {int(Skill_H3)}')
print(f'Hit 4: {int(Skill_H4)}')
print(f'Hit 5: {int(Skill_H5)}')
print(f'Ult (slash): {int(Ult_H1)}')
print(f'Ult (explosion): {int(Ult_H2)}')
print('')
print(f'DPR: {int(DPR)}')
print('teste4')



