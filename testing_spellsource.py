from spellsource.context import Context
from spellsource.behaviour import *

TOKEN_DRUID = '''### Token Druid - Standard Meta Snapshot - June 18, 2018
# Class: Druid
# Format: Standard
# Year of the Raven
#
# 2x (1) Lesser Jasper Spellstone
# 2x (2) Wild Growth
# 2x (2) Wrath
# 2x (3) Savage Roar
# 2x (4) Branching Paths
# 1x (4) Oaken Summons
# 2x (4) Soul of the Forest
# 2x (4) Swipe
# 2x (4) Violet Teacher
# 2x (4) Wispering Woods
# 2x (5) Arcane Tyrant
# 2x (5) Nourish
# 1x (6) Cairne Bloodhoof
# 2x (6) Spreading Plague
# 1x (7) Malfurion the Pestilent
# 1x (8) The Lich King
# 2x (10) Ultimate Infestation
#
AAECAZICBITmAqQDmdMCws4CDZjSAuQIxAbmBZ7SAv0CQIUI1+8C29MCX6DNAofOAgA=
#
# To use this deck, copy it to your clipboard and create a new deck in Hearthstone'''

EVEN_WARLOCK = '''### Even Warlock - Standard Meta Snapshot - June 18, 2018
# Class: Warlock
# Format: Standard
# Year of the Raven
#
# 1x (2) Acidic Swamp Ooze
# 2x (2) Defile
# 2x (2) Doomsayer
# 2x (2) Plated Beetle
# 2x (2) Sunfury Protector
# 2x (2) Vulgar Homunculus
# 2x (4) Hellfire
# 2x (4) Hooked Reaver
# 2x (4) Lesser Amethyst Spellstone
# 2x (4) Shroom Brewer
# 2x (4) Spellbreaker
# 2x (4) Twilight Drake
# 1x (6) Dread Infernal
# 1x (6) Genn Greymane
# 1x (6) Skulking Geist
# 1x (8) The Lich King
# 1x (10) Bloodreaver Gul'dan
# 2x (12) Mountain Giant
#
AAECAf0GBooH+wfN9AKgzgLCzgKX0wIM58sCigHq5gL7BvHQArYH/dACiNIC2OUC8gWNCOEHAA==
#
# To use this deck, copy it to your clipboard and create a new deck in Hearthstone
'''
ctx = Context()
game_context = ctx.GameContext.fromDeckLists([TOKEN_DRUID, EVEN_WARLOCK])
agent_1 = ctx.behaviour.FiberBehaviour()
agent_2 = ctx.behaviour.FiberBehaviour()
game_context.setBehaviour(ctx.GameContext.PLAYER_1, agent_1)
game_context.setBehaviour(ctx.GameContext.PLAYER_2, agent_2)
SEED = 10101
game_context.setLogic(ctx.GameLogic(SEED))
game_context.play()

def pending_mulligans():
    for i, agent in enumerate([agent_1, agent_2]):
        print('Agent', i+1, [card.toString() for card in agent.getMulliganCards()])

pending_mulligans()
'''
mullgan1 = [card.toString() for card in agent_1.getMulliganCards()]
mullgan2 = [card.toString() for card in agent_2.getMulliganCards()]
print(mullgan1)
print(mullgan2)
'''
