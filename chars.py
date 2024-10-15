
#Kinich
Nome = 'Kinich'
VidaBase = 12858
AtaqueChar = 332
AtaqueArma = weapons.earthshaker_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 802
StatusAscensao = 0.384
#---------------------------------
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
BonusElm = 0 +relics.codice_obsidiana_2 #+relics.perg_hero_4
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
print('< Talentos >')
print(f'Skill (AA): {int(SkillDisparos)}')
print(f'Skill (canhao 1): {int(SkillCanhaoBuffado)}')
print(f'Skill (canhao 2/3/4): {int(SkillCanhao)}')
print(f'Ult (laser): {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(((SkillDisparos*4+SkillCanhaoBuffado+Ult)*1)+((SkillDisparos*4+SkillCanhao+Ult)*3))}')

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
AtaquePorc = 0 +0.3 +weapons.cancao_silencio_stat +relics.ritual_real_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0 +100
RecargaPorc = 0
CritDmg = 0 +0.4 +sups.faruzan_c6
CritRate = 0 +0.25 +StatusAscensao
BonusElm = 0 +weapons.cancao_silencio_p1 +relics.cronicas_deserto_2 +sups.furina_ult +sups.faruzan_ult_buff
BonusFis = 0
BonusAA = 0 +relics.cronicas_deserto_4
BonusCarregado = 0 +relics.cronicas_deserto_4
BonusImersivo = 0
BonusSkill = 0
BonusUlt = 0
BonusFaruzanPassiva = sups.faruzan_passiva
#--------------------------------------
Skill_NormalShots = (AtaqueTotal*1.09+BonusFaruzanPassiva)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
Skill_ShineShots = (AtaqueTotal*3.45+BonusFaruzanPassiva)*(1+DanoElemental+BonusCarregado)*EnemyReduct*(1+DanoCritico)
Ult_NormalShells = (AtaqueTotal*1.86+BonusFaruzanPassiva)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
Ult_RadiantShells = (AtaqueTotal*3.72+BonusFaruzanPassiva)*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)
DPR = Ult_NormalShells*2+Ult_RadiantShells*4+(Skill_NormalShots*4+Skill_ShineShots*2)*4
print('< Talentos >')
print(f'Skill (N-shots): {int(Skill_NormalShots)}')
print(f'Skill (S-shots): {int(Skill_ShineShots)}')
print(f'Ult (N-shells): {int(Ult_NormalShells)}')
print(f'Ult (R-shells): {int(Ult_RadiantShells)}')
print('')
print(f'DPR: {int(DPR)}')
