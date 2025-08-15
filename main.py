
import sups
import relics
import weapons

print('')
print('GI: DAMAGE CALCULATOR')
print('---------------------')
print('')

#STATUS BASE
Nome = 'Skirk'
VidaBase = 12417
AtaqueChar = 358.77
AtaqueArma = weapons.blacksword_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 806
StatusAscensao = 0.384

#VALOR DOS ARTEFATOS NO +20
FlorVida = 4780
PenaAtaque = 311
AreiaVida = 0.466
AreiaAtaque = 0.466
AreiaDefesa = 0.583
AreiaEM = 186.5
AreiaER = 0.518
CaliceVida = 0.466
CaliceAtaque = 0.466
CaliceDefesa = 0.583
CaliceEM = 186.5
CaliceED = 0.466
CalicePD = 0.583
CoroaVida = 0.466
CoroaAtaque = 0.466
CoroaDefesa = 0.583
CoroaEM = 186.5
CoroaCR = 0.311
CoroaCD = 0.622
CoroaCura = 0.359

#SELETOR DE ARTEFATOS
AreiaVida_S = 0
AreiaAtaque_S = 1
AreiaDefesa_S = 0
AreiaEM_S = 0
AreiaER_S = 0
#-------------------
CaliceVida_S = 0
CaliceAtaque_S = 0
CaliceDefesa_S = 0
CaliceEM_S = 0
CaliceED_S = 1
CalicePD_S = 0
#--------------------
CoroaVida_S = 0
CoroaAtaque_S = 0
CoroaDefesa_S = 0
CoroaEM_S = 0
CoroaCR_S = 0
CoroaCD_S = 1
CoroaCura_S = 0

#RESSONANCIAS
resso_geo = 0.15
resso_pyro = 0.25
resso_hydro = 0.25
resso_cryo = 0.15
resso_dendro = 20

#SUB-STATUS + BÔNUS DIVERSOS
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

#MULTIPLICADORES
MultVida = 1+(AreiaVida_S*AreiaVida)+(CaliceVida_S*CaliceVida)+(CoroaVida_S*CoroaVida)+VidaPorc
MultAtaque = 1+(AreiaAtaque_S*AreiaAtaque)+(CaliceAtaque_S*CaliceAtaque)+(CoroaAtaque_S*CoroaAtaque)+AtaquePorc
MultDefesa = 1+(AreiaDefesa_S*AreiaDefesa)+(CaliceDefesa_S*CaliceDefesa)+(CoroaDefesa_S*CoroaDefesa)+DefesaPorc

#STATUS TOTAIS
VidaTotal = (VidaBase*MultVida)+FlorVida+VidaFlat
AtaqueTotal = (AtaqueBase*MultAtaque)+PenaAtaque+AtaqueFlat
DefesaTotal = (DefesaBase*MultDefesa)+DefesaFlat
MaestriaElemental = (AreiaEM_S*AreiaEM)+(CaliceEM_S*CaliceEM)+(CoroaEM_S*CoroaEM)+EM
RecargaTotal = (AreiaER_S*AreiaER)+RecargaPorc
DanoCritico = 0.5+(CoroaCD_S*CoroaCD)+CritDmg
TaxaCritica = 0.05+(CoroaCR_S*CoroaCR)+CritRate
DanoElemental = (CaliceED_S*CaliceED)+BonusElm
DanoFisico = (CalicePD_S*CalicePD)+BonusFis

#STATUS INIMIGO
EnemyLevel = 103
EnemyResEl = 0.1
EnemyResFis = 0.1
ReductDef = 0
ReductRes = 0 +sups.escoff_debuff
#-------------------------------------------------------
RD = 1-ReductDef
EnemyDef = 190/(RD*(EnemyLevel+100)+190)
RR = EnemyResEl - ReductRes
if RR < 0:
    EnemyRes = 1-(RR/2)
elif RR >= 0 and RR < 0.75:
    EnemyRes = 1-RR
elif RR >= 0.75:
    EnemyRes = 1/(4*RR+1)
EnemyReduct = EnemyDef*EnemyRes  
print('< Inimigo >')
print(f'Nivel: {int(EnemyLevel)}')
print(f'Resistencia: {int((1-EnemyRes)*100)}%')
print(f'Defesa: {int((1-EnemyDef)*100)}%')
print(f'Dano Tankado: {int((1-EnemyReduct)*100)}%')
print('')

#CALCULO REACOES
TriggerReact = 1
BonusCharLevel = 1446.85
BonusAmpReac = 0
BonusTransReac = 0
#------------------------------------------
MeltPyro = 2
MeltCryo = 1.5
VapoHydro = 2
VapoPyro = 1.5
Burn = 0.25
SuperCond = 1.5
Swirl = 0.6
ElecCharg = 2
Shatt = 3
Overload = 2.75
Bloom = 2
Burgeon = 3
HypBloom = 3
BonusAmpEM = 2.78*(MaestriaElemental/(MaestriaElemental+1400))
BonusTransEM = 16*(MaestriaElemental/(MaestriaElemental+2000))
#--------------------------------------------
MultAmp = (VapoPyro*(1+BonusAmpEM+BonusAmpReac))**TriggerReact
MultTrans = (ElecCharg*BonusCharLevel*(1+BonusTransEM+BonusTransReac)*EnemyRes)**TriggerReact

#DANO DOS TALENTOS
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

#EXIBICAO
print(f'< {Nome} >')
print(f'Vida: {int(VidaTotal)}')
print(f'Ataque: {int(AtaqueTotal)}')
print(f'Defesa: {int(DefesaTotal)}')
print(f'Maest.Elemental: {int(MaestriaElemental)}')
print(f'Recarga: {int(RecargaTotal*100)}%')
print(f'Dano Critico: {int(DanoCritico*100)}%')
print(f'Taxa Critica: {int(TaxaCritica*100)}%')
print(f'Bonus Elemental: {int(DanoElemental*100)}%')
print(f'Bonus Fisico: {int(DanoFisico*100)}%')
print(f'Bonus de Ataque Normal: {int(BonusAA*100)}%')
print(f'Bonus de Ataque Carregado: {int(BonusCarregado*100)}%')
print(f'Bonus de Ataque Imersivo: {int(BonusImersivo*100)}%')
print(f'Bonus de Skill: {int(BonusSkill*100)}%')
print(f'Bonus de Ult: {int(BonusUlt*100)}%')
print(f'Amplificador de Reacao: {(MultAmp):.2f}')
print(f'Reacao Transformativa: {int(MultTrans)}')
print('')
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
print('testefinal')
