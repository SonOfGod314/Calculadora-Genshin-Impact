
import sups
import relics
import weapons

print('')
print('GI: DAMAGE CALCULATOR')
print('---------------------')
print('')

#STATUS BASE
Nome = 'Hutao'
VidaBase = 15552
AtaqueChar = 106
AtaqueArma = weapons.perd_drag_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 876
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
AreiaVida_S = 1
AreiaAtaque_S = 0
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
CoroaCR_S = 1
CoroaCD_S = 0
CoroaCura_S = 0

#RESSONANCIAS
resso_geo = 0.15
resso_pyro = 0.25
resso_hydro = 0.25
resso_cryo = 0.15
resso_dendro = 20

#SUB-STATUS + BÔNUS DIVERSOS
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
ReductRes = 0
#-------------------------------------------------------
RD = 1-ReductDef
EnemyDef = 190/(RD*(EnemyLevel+100)+190)
EnemyRes = EnemyResEl - ReductRes
if EnemyRes < 0:
    EnemyReduct = EnemyDef*(1-(EnemyRes/2))
elif EnemyRes >= 0 and EnemyRes < 0.75:
    EnemyReduct = EnemyDef*(1-EnemyRes)
elif EnemyRes >= 0.75:
    EnemyReduct = EnemyDef*(1/(4*EnemyRes+1))
print('< Inimigo >')
print(f'Nivel: {int(EnemyLevel)}')
print(f'Resistencia: {int(EnemyRes*100)}%')
print(f'Defesa: {int((1-EnemyDef)*100)}%')
print(f'Dano Tankado: {int((1-EnemyReduct)*100)}%')
print('')

#CALCULO REACOES
TriggerReact = 1
BonusCharLevel = 1446.85
BonusAmpReac = 0 +relics.bruxa_chamas_4
BonusTransReac = 0
#------------------------------------------
MeltPyro = 2
MeltCryo = 1.5
VapoHydro = 2
VapoPyro = 1.5
Burn = 0.25
SuperCond = 0.5
Swirl = 0.6
ElecCharg = 1.2
Shatt = 1.5
Overload = 2
Bloom = 2
Burgeon = 3
HypBloom = 3
BonusAmpEM = 2.78*(MaestriaElemental/(MaestriaElemental+1400))
BonusTransEM = 16*(MaestriaElemental/(MaestriaElemental+2000))
#--------------------------------------------
MultAmp = (VapoPyro*(1+BonusAmpEM+BonusAmpReac))**TriggerReact
MultTrans = (Burn*BonusCharLevel*(1+BonusTransEM+BonusTransReac)*EnemyReduct)**TriggerReact

#DANO DOS TALENTOS
AtaqueNormal = AtaqueTotal*0.8365*(1+DanoElemental+BonusAA)*EnemyReduct*MultAmp*(1+DanoCritico)
AtaqueCarregado = AtaqueTotal*2.42*(1+DanoElemental+BonusCarregado)*EnemyReduct*MultAmp*(1+DanoCritico)
Ult = AtaqueTotal*6.17*(1+DanoElemental+BonusUlt)*EnemyReduct*MultAmp*(1+DanoCritico)

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
print(f'Ataque Normal: {int(AtaqueNormal)}')
print(f'Ataque Carregado: {int(AtaqueCarregado)}')
print(f'Ult: {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(Ult+(AtaqueNormal+AtaqueCarregado)*10)}')
