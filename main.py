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

#SUB-STATUS + BÔNUS DIVERSOS
VidaFlat = 0
VidaPorc = 0
AtaqueFlat = 0 + 200 + 1000
AtaquePorc = 0 + 0.276
DefesaFlat = 0
DefesaPorc = 0
EM = 0
ER = 0
CD = 0 + 0.384 + 0.4
CR = 0 + 0.25 + 0.4
BD = 0 + 0.15

#Multiplicadores
MultVida = 1+(AreiaVida_S*AreiaVida)+(CaliceVida_S*CaliceVida)+(CoroaVida_S*CoroaVida)+VidaPorc
MultAtaque = 1+(AreiaAtaque_S*AreiaAtaque)+(CaliceAtaque_S*CaliceAtaque)+(CoroaAtaque_S*CoroaAtaque)+AtaquePorc
MultDefesa = 1+(AreiaDefesa_S*AreiaDefesa)+(CaliceDefesa_S*CaliceDefesa)+(CoroaDefesa_S*CoroaDefesa)+DefesaPorc

#Status Totais
VidaTotal = (VidaBase*MultVida)+FlorVida+VidaFlat
AtaqueTotal = (AtaqueBase*MultAtaque)+PenaAtaque+AtaqueFlat
DefesaTotal = (DefesaBase*MultDefesa)+DefesaFlat
MaestriaElemental = (AreiaEM_S*AreiaEM)+(CaliceEM_S*CaliceEM)+(CoroaEM_S*CoroaEM)+EM
RecargaTotal = (AreiaER_S*AreiaER)+ER
DanoCritico = 0.5+(CoroaCD_S*CoroaCD)+CD
TaxaCritica = 0.05+(CoroaCR_S*CoroaCR)+CR
DanoElemental = (CaliceED_S*CaliceED)+BD
DanoFisico = (CalicePD_S*CalicePD)+BD

#Talentos
SkillDisparos = AtaqueTotal*1.03*(1+DanoElemental)*(1+DanoCritico)
SkillCanhao = AtaqueTotal*12.37*(1+DanoElemental+0.3)*(1+DanoCritico)
Ult = AtaqueTotal*2.05*(1+DanoElemental)*(1+DanoCritico)

print('< Personagem >')
print(f'Vida: {int(VidaTotal)}')
print(f'Ataque: {int(AtaqueTotal)}')
print(f'Defesa: {int(DefesaTotal)}')
print(f'Maest.Elemental: {int(MaestriaElemental)}')
print(f'Recarga: {RecargaTotal}%')
print(f'Dano Critico: {int(DanoCritico*100)}%')
print(f'Taxa Critica: {int(TaxaCritica*100)}%')
print(f'Dano Elemental: {int(DanoElemental*100)}%')
print(f'Dano Fisico: {int(DanoFisico)}%')
print('')
print('< Talentos >')
print(f'Skill (mini-disparos): {int(SkillDisparos)}')
print(f'Skill (canhão): {int(SkillCanhao)}')
print(f'Ult (laser): {int(Ult)}')
print('')
print(f'Dano Rotação: {int((SkillDisparos*4+SkillCanhao+Ult)*4)}')
