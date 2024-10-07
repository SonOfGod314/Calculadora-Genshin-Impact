
import sups
import relics
import weapons

print('')
print('GI: DAMAGE CALCULATOR')
print('---------------------')
print('')

#STATUS BASE
Nome = 'Kinich'
VidaBase = 12858
AtaqueChar = 332
AtaqueArma = weapons.earthshaker_base
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 802
StatusAscensao = 0.384

#VALOR DOS ARTEFATOS NO +20
FlorVida = 4780
PenaAtaque = 311
AreiaVida = 0.466
AreiaAtaque = 0.466
AreiaDefesa = 0.583
AreiaEM = 186.5
AreiaER = 51.8
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
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 +35 +18 +51 +sups.benny_ult
AtaquePorc = 0 +weapons.earthshaker_stat +resso_pyro +relics.ritual_real_4 #+relics.milelith_4
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +0.14 +0.14 +0.078 +0.062 +StatusAscensao #+0.08
CritRate = 0 +0.25 +relics.codice_obsidiana_4
BonusElm = 0 +relics.codice_obsidiana_2 #+relics.perg_hero_4_2 
BonusFis = 0
BonusAA = 0 +0.15
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0 +weapons.earthshaker_p1
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
ReductRes = 0 +relics.mem_flo_4
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
BonusAmpReac = 0
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
MultAmp = (VapoPyro*(1+BonusAmpEM+BonusAmpReac))**TriggerReact
MultTrans = (Burn*BonusCharLevel*(1+BonusTransEM+BonusTransReac)*EnemyReduct)**TriggerReact

#DANO DOS TALENTOS
Talento = 3.2*AtaqueTotal
SkillDisparos = AtaqueTotal*1.03*(1+DanoElemental+BonusAA)*EnemyReduct*(1+DanoCritico)
SkillCanhaoBuffado = (AtaqueTotal*12.37+Talento)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
SkillCanhao = (AtaqueTotal*12.37)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
Ult = AtaqueTotal*2.05*(1+DanoElemental+BonusUlt)*EnemyReduct*(1+DanoCritico)

#EXIBICAO
print(f'< {Nome} >')
print(f'Vida: {int(VidaTotal)}')
print(f'Ataque: {int(AtaqueTotal)}')
print(f'Defesa: {int(DefesaTotal)}')
print(f'Maest.Elemental: {int(MaestriaElemental)}')
print(f'Recarga: {int(RecargaTotal)}%')
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
print(f'Skill (AA): {int(SkillDisparos)}')
print(f'Skill (canhao 1): {int(SkillCanhaoBuffado)}')
print(f'Skill (canhao 2/3/4): {int(SkillCanhao)}')
print(f'Ult (laser): {int(Ult)}')
print('')
print(f'Dano Rotacao: {int(((SkillDisparos*4+SkillCanhaoBuffado+Ult)*1)+((SkillDisparos*4+SkillCanhao+Ult)*3))}')
