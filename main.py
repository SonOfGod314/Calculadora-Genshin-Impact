
import chars
import relics
import weapons

print('')
print('GI: DAMAGE CALCULATOR')
print('---------------------')
print('')

#STATUS BASE
VidaBase = 12858
AtaqueChar = 332
AtaqueArma = 565
AtaqueBase = AtaqueChar + AtaqueArma
DefesaBase = 802

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
AtaqueFlat = 0 +35 +18 +51 +chars.benny_ult
AtaquePorc = 0 +0.276 +relics.ritual_real_4 +relics.milelith_4 +resso_pyro
DefesaFlat = 0
DefesaPorc = 0
EM = 0
RecargaPorc = 0
CritDmg = 0 +0.14 +0.14 +0.078 +0.062 +0.38
CritRate = 0 +0.25 +relics.codice_obsidiana_4
BonusElm = 0 +relics.codice_obsidiana_2 #+relics.perg_hero_4_2
BonusFis = 0
BonusAA = 0
BonusCarregado = 0
BonusImersivo = 0
BonusSkill = 0 +weapons.earthshaker
BonusUlt = 0
ReductRes = 0 +relics.mem_flo_4

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
EnemyLevel = 104
EnemyDef = 190/((EnemyLevel+100)+190)
EnemyRes = 0-ReductRes
EnemyReduct = (1-EnemyDef)*(1-EnemyRes)
print('< Inimigo >')
print(f'Resistencia: {int(EnemyRes*100)}%')
print(f'Mult.Defesa: {int(EnemyDef*100)}%')
print('')

#DANO DOS TALENTOS
Talento = 3.2*AtaqueTotal*0
SkillDisparos = AtaqueTotal*1.03*(1+DanoElemental)*EnemyReduct*(1+DanoCritico)
SkillCanhao = (AtaqueTotal*12.7+Talento)*(1+DanoElemental+BonusSkill)*EnemyReduct*(1+DanoCritico)
Ult = AtaqueTotal*2.05*(1+DanoElemental)*EnemyReduct*(1+DanoCritico)

#EXIBICAO
print('< Personagem >')
print(f'Vida: {int(VidaTotal)}')
print(f'Ataque: {int(AtaqueTotal)}')
print(f'Defesa: {int(DefesaTotal)}')
print(f'Maest.Elemental: {int(MaestriaElemental)}')
print(f'Recarga: {int(RecargaTotal)}%')
print(f'Dano Critico: {int(DanoCritico*100)}%')
print(f'Taxa Critica: {int(TaxaCritica*100)}%')
print(f'Dano Elemental: {int(DanoElemental*100)}%')
print(f'Dano Fisico: {int(DanoFisico*100)}%')
print(f'Bonus de Dano (Ataque Normal): {int(BonusAA*100)}%')
print(f'Bonus de Dano (Ataque Carregado): {int(BonusCarregado*100)}%')
print(f'Bonus de Dano (Ataque Imersivo): {int(BonusImersivo*100)}%')
print(f'Bonus de Dano (Skill): {int(BonusSkill*100)}%')
print(f'Bonus de Dano (Ult): {int(BonusUlt*100)}%')
print('')
print('< Talentos >')
print(f'Skill (mini-disparos): {int(SkillDisparos)}')
print(f'Skill (canhao): {int(SkillCanhao)}')
print(f'Ult (laser): {int(Ult)}')
print('')
print(f'Dano Rotacao: {int((SkillDisparos*4+SkillCanhao+Ult)*4)}')
