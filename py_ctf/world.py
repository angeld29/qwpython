###
### Generated by QuakeC -> Python translator
### Id: qc2python.py,v 1.5 2001/02/05 21:15:44 barryp Exp 
###
from qwpython.qwsv import engine, Vector
from qwpython.qcsupport import qc

import defs
import weapons


def main(*qwp_extra):
    engine.dprint('main function\012')
    #  these are just commands the the prog compiler to copy these files
    qc.precache_file('progs.dat')
    qc.precache_file('gfx.wad')
    qc.precache_file('quake.rc')
    qc.precache_file('default.cfg')
    qc.precache_file('end1.bin')
    qc.precache_file('end2.bin')
    qc.precache_file('demo1.dem')
    qc.precache_file('demo2.dem')
    qc.precache_file('demo3.dem')
    # 
    #  these are all of the lumps from the cached.ls files
    # 
    qc.precache_file('gfx/palette.lmp')
    qc.precache_file('gfx/colormap.lmp')
    qc.precache_file('gfx/pop.lmp')
    qc.precache_file('gfx/complete.lmp')
    qc.precache_file('gfx/inter.lmp')
    qc.precache_file('gfx/ranking.lmp')
    qc.precache_file('gfx/vidmodes.lmp')
    qc.precache_file('gfx/finale.lmp')
    qc.precache_file('gfx/conback.lmp')
    qc.precache_file('gfx/qplaque.lmp')
    qc.precache_file('gfx/menudot1.lmp')
    qc.precache_file('gfx/menudot2.lmp')
    qc.precache_file('gfx/menudot3.lmp')
    qc.precache_file('gfx/menudot4.lmp')
    qc.precache_file('gfx/menudot5.lmp')
    qc.precache_file('gfx/menudot6.lmp')
    qc.precache_file('gfx/menuplyr.lmp')
    qc.precache_file('gfx/bigbox.lmp')
    qc.precache_file('gfx/dim_modm.lmp')
    qc.precache_file('gfx/dim_drct.lmp')
    qc.precache_file('gfx/dim_ipx.lmp')
    qc.precache_file('gfx/dim_tcp.lmp')
    qc.precache_file('gfx/dim_mult.lmp')
    qc.precache_file('gfx/mainmenu.lmp')
    qc.precache_file('gfx/box_tl.lmp')
    qc.precache_file('gfx/box_tm.lmp')
    qc.precache_file('gfx/box_tr.lmp')
    qc.precache_file('gfx/box_ml.lmp')
    qc.precache_file('gfx/box_mm.lmp')
    qc.precache_file('gfx/box_mm2.lmp')
    qc.precache_file('gfx/box_mr.lmp')
    qc.precache_file('gfx/box_bl.lmp')
    qc.precache_file('gfx/box_bm.lmp')
    qc.precache_file('gfx/box_br.lmp')
    qc.precache_file('gfx/sp_menu.lmp')
    qc.precache_file('gfx/ttl_sgl.lmp')
    qc.precache_file('gfx/ttl_main.lmp')
    qc.precache_file('gfx/ttl_cstm.lmp')
    qc.precache_file('gfx/mp_menu.lmp')
    qc.precache_file('gfx/netmen1.lmp')
    qc.precache_file('gfx/netmen2.lmp')
    qc.precache_file('gfx/netmen3.lmp')
    qc.precache_file('gfx/netmen4.lmp')
    qc.precache_file('gfx/netmen5.lmp')
    qc.precache_file('gfx/sell.lmp')
    qc.precache_file('gfx/help0.lmp')
    qc.precache_file('gfx/help1.lmp')
    qc.precache_file('gfx/help2.lmp')
    qc.precache_file('gfx/help3.lmp')
    qc.precache_file('gfx/help4.lmp')
    qc.precache_file('gfx/help5.lmp')
    qc.precache_file('gfx/pause.lmp')
    qc.precache_file('gfx/loading.lmp')
    qc.precache_file('gfx/p_option.lmp')
    qc.precache_file('gfx/p_load.lmp')
    qc.precache_file('gfx/p_save.lmp')
    qc.precache_file('gfx/p_multi.lmp')
    #  sounds loaded by C code
    engine.precache_sound('misc/menu1.wav')
    engine.precache_sound('misc/menu2.wav')
    engine.precache_sound('misc/menu3.wav')
    engine.precache_sound('ambience/water1.wav')
    engine.precache_sound('ambience/wind2.wav')
    #  shareware
    qc.precache_file('maps/start.bsp')
    qc.precache_file('maps/e1m1.bsp')
    qc.precache_file('maps/e1m2.bsp')
    qc.precache_file('maps/e1m3.bsp')
    qc.precache_file('maps/e1m4.bsp')
    qc.precache_file('maps/e1m5.bsp')
    qc.precache_file('maps/e1m6.bsp')
    qc.precache_file('maps/e1m7.bsp')
    qc.precache_file('maps/e1m8.bsp')
    #  registered
    qc.precache_file('gfx/pop.lmp')
    qc.precache_file('maps/e2m1.bsp')
    qc.precache_file('maps/e2m2.bsp')
    qc.precache_file('maps/e2m3.bsp')
    qc.precache_file('maps/e2m4.bsp')
    qc.precache_file('maps/e2m5.bsp')
    qc.precache_file('maps/e2m6.bsp')
    qc.precache_file('maps/e2m7.bsp')
    qc.precache_file('maps/e3m1.bsp')
    qc.precache_file('maps/e3m2.bsp')
    qc.precache_file('maps/e3m3.bsp')
    qc.precache_file('maps/e3m4.bsp')
    qc.precache_file('maps/e3m5.bsp')
    qc.precache_file('maps/e3m6.bsp')
    qc.precache_file('maps/e3m7.bsp')
    qc.precache_file('maps/e4m1.bsp')
    qc.precache_file('maps/e4m2.bsp')
    qc.precache_file('maps/e4m3.bsp')
    qc.precache_file('maps/e4m4.bsp')
    qc.precache_file('maps/e4m5.bsp')
    qc.precache_file('maps/e4m6.bsp')
    qc.precache_file('maps/e4m7.bsp')
    qc.precache_file('maps/e4m8.bsp')
    qc.precache_file('maps/end.bsp')
    qc.precache_file('maps/dm1.bsp')
    qc.precache_file('maps/dm2.bsp')
    qc.precache_file('maps/dm3.bsp')
    qc.precache_file('maps/dm4.bsp')
    qc.precache_file('maps/dm5.bsp')
    qc.precache_file('maps/dm6.bsp')
    
lastspawn = engine.world
# =======================
# QUAKED worldspawn (0 0 0) ?
# Only used for the world entity.
# Set message to the level name.
# Set sounds to the cd track to play.
# 
# World Types:
# 0: medieval
# 1: metal
# 2: base
# 
# =======================

def worldspawn(*qwp_extra):
    global lastspawn
    lastspawn = qc.world
    defs.runespawn = qc.world
    defs.runespawned = 0
    InitBodyQue()
    #  custom map attributes
    #  can't change gravity in QuakeWorld
    # 
    # 	if (self.model == "maps/e1m8.bsp")
    # 		cvar_set ("sv_gravity", "100");
    # 	else
    # 		cvar_set ("sv_gravity", "800");
    # 
    if qc.self.model == 'maps/ctfstart.bsp' or qc.self.model == 'maps/start.bsp':
        defs.gamestart = 1
    else:
        defs.gamestart = 0
    #  the area based ambient sounds MUST be the first precache_sounds
    #  player precaches	
    weapons.W_Precache() #  get weapon precaches
    #  sounds used from C physics code
    engine.precache_sound('demon/dland2.wav') #  landing thud
    engine.precache_sound('misc/h2ohit1.wav') #  landing splash
    #  setup precaches allways needed
    engine.precache_sound('items/itembk2.wav') #  item respawn sound
    engine.precache_sound('player/plyrjmp8.wav') #  player jump
    engine.precache_sound('player/land.wav') #  player landing
    engine.precache_sound('player/land2.wav') #  player hurt landing
    engine.precache_sound('player/drown1.wav') #  drowning pain
    engine.precache_sound('player/drown2.wav') #  drowning pain
    engine.precache_sound('player/gasp1.wav') #  gasping for air
    engine.precache_sound('player/gasp2.wav') #  taking breath
    engine.precache_sound('player/h2odeath.wav') #  drowning death
    engine.precache_sound('misc/talk.wav') #  talk
    engine.precache_sound('player/teledth1.wav') #  telefrag
    engine.precache_sound('misc/r_tele1.wav') #  teleport sounds
    engine.precache_sound('misc/r_tele2.wav')
    engine.precache_sound('misc/r_tele3.wav')
    engine.precache_sound('misc/r_tele4.wav')
    engine.precache_sound('misc/r_tele5.wav')
    engine.precache_sound('weapons/lock4.wav') #  ammo pick up
    engine.precache_sound('weapons/pkup.wav') #  weapon up
    engine.precache_sound('items/armor1.wav') #  armor up
    engine.precache_sound('weapons/lhit.wav') # lightning
    engine.precache_sound('weapons/lstart.wav') # lightning start
    engine.precache_sound('items/damage3.wav')
    engine.precache_sound('misc/power.wav') # lightning for boss
    #  player gib sounds
    engine.precache_sound('player/gib.wav') #  player gib sound
    engine.precache_sound('player/udeath.wav') #  player gib sound
    engine.precache_sound('player/tornoff2.wav') #  gib sound
    #  player pain sounds
    engine.precache_sound('player/pain1.wav')
    engine.precache_sound('player/pain2.wav')
    engine.precache_sound('player/pain3.wav')
    engine.precache_sound('player/pain4.wav')
    engine.precache_sound('player/pain5.wav')
    engine.precache_sound('player/pain6.wav')
    #  player death sounds
    engine.precache_sound('player/death1.wav')
    engine.precache_sound('player/death2.wav')
    engine.precache_sound('player/death3.wav')
    engine.precache_sound('player/death4.wav')
    engine.precache_sound('player/death5.wav')
    #  ax sounds	
    engine.precache_sound('weapons/ax1.wav') #  ax swoosh
    engine.precache_sound('player/axhit1.wav') #  ax hit meat
    engine.precache_sound('player/axhit2.wav') #  ax hit world
    engine.precache_sound('hknight/hit.wav') #  ZOID: hook launch
    engine.precache_sound('player/h2ojump.wav') #  player jumping into water
    engine.precache_sound('player/slimbrn2.wav') #  player enter slime
    engine.precache_sound('player/inh2o.wav') #  player enter water
    engine.precache_sound('player/inlava.wav') #  player enter lava
    engine.precache_sound('misc/outwater.wav') #  leaving water sound
    engine.precache_sound('player/lburn1.wav') #  lava burn
    engine.precache_sound('player/lburn2.wav') #  lava burn
    engine.precache_sound('misc/water1.wav') #  swimming
    engine.precache_sound('misc/water2.wav') #  swimming
    engine.precache_model('progs/player.mdl')
    engine.precache_model('progs/h_player.mdl')
    engine.precache_model('progs/eyes.mdl')
    engine.precache_model('progs/gib1.mdl')
    engine.precache_model('progs/gib2.mdl')
    engine.precache_model('progs/gib3.mdl')
    engine.precache_model('progs/s_bubble.spr') #  drowning bubbles
    engine.precache_model('progs/s_explod.spr') #  sprite explosion
    engine.precache_model('progs/v_axe.mdl')
    engine.precache_model('progs/v_shot.mdl')
    engine.precache_model('progs/v_nail.mdl')
    engine.precache_model('progs/v_rock.mdl')
    engine.precache_model('progs/v_shot2.mdl')
    engine.precache_model('progs/v_nail2.mdl')
    engine.precache_model('progs/v_rock2.mdl')
    engine.precache_model('progs/v_star.mdl') #  precache grapple (Wedge)
    engine.precache_model('progs/bit.mdl') #  precache grapple (Wedge)
    engine.precache_model('progs/star.mdl') #  precache grapple (Wedge)
    engine.precache_model('progs/bolt.mdl') #  for lightning gun
    engine.precache_model('progs/bolt2.mdl') #  for lightning gun
    engine.precache_model('progs/bolt3.mdl') #  for boss shock
    engine.precache_model('progs/lavaball.mdl') #  for testing
    engine.precache_model('progs/missile.mdl')
    engine.precache_model('progs/grenade.mdl')
    engine.precache_model('progs/spike.mdl')
    engine.precache_model('progs/s_spike.mdl')
    engine.precache_model('progs/backpack.mdl')
    engine.precache_model('progs/zom_gib.mdl')
    engine.precache_model('progs/v_light.mdl')
    # 
    #  Setup light animation tables. 'a' is total darkness, 'z' is maxbright.
    # 
    #  0 normal
    engine.lightstyle(0, 'm')
    #  1 FLICKER (first variety)
    engine.lightstyle(1, 'mmnmmommommnonmmonqnmmo')
    #  2 SLOW STRONG PULSE
    engine.lightstyle(2, 'abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba')
    #  3 CANDLE (first variety)
    engine.lightstyle(3, 'mmmmmaaaaammmmmaaaaaabcdefgabcdefg')
    #  4 FAST STROBE
    engine.lightstyle(4, 'mamamamamama')
    #  5 GENTLE PULSE 1
    engine.lightstyle(5, 'jklmnopqrstuvwxyzyxwvutsrqponmlkj')
    #  6 FLICKER (second variety)
    engine.lightstyle(6, 'nmonqnmomnmomomno')
    #  7 CANDLE (second variety)
    engine.lightstyle(7, 'mmmaaaabcdefgmmmmaaaammmaamm')
    #  8 CANDLE (third variety)
    engine.lightstyle(8, 'mmmaaammmaaammmabcdefaaaammmmabcdefmmmaaaa')
    #  9 SLOW STROBE (fourth variety)
    engine.lightstyle(9, 'aaaaaaaazzzzzzzz')
    #  10 FLUORESCENT FLICKER
    engine.lightstyle(10, 'mmamammmmammamamaaamammma')
    #  11 SLOW PULSE NOT FADE TO BLACK
    engine.lightstyle(11, 'abcdefghijklmnopqrrqponmlkjihgfedcba')
    #  styles 32-62 are assigned by the light program for switchable lights
    #  63 testing
    engine.lightstyle(63, 'a')
    

def StartFrame(*qwp_extra):
    defs.timelimit = engine.cvar('timelimit') * 60
    defs.fraglimit = engine.cvar('fraglimit')
    defs.teamplay = engine.cvar('teamplay')
    defs.deathmatch = engine.cvar('deathmatch')
    defs.framecount += 1
    
# 
# ==============================================================================
# 
# BODY QUE
# 
# ==============================================================================
# 
bodyque_head = engine.world

def bodyque(*qwp_extra):
    pass

def InitBodyQue(*qwp_extra):
    global bodyque_head
    e = engine.world
    bodyque_head = qc.spawn()
    bodyque_head.classname = 'bodyque'
    bodyque_head.owner = qc.spawn()
    bodyque_head.owner.classname = 'bodyque'
    bodyque_head.owner.owner = qc.spawn()
    bodyque_head.owner.owner.classname = 'bodyque'
    bodyque_head.owner.owner.owner = qc.spawn()
    bodyque_head.owner.owner.owner.classname = 'bodyque'
    bodyque_head.owner.owner.owner.owner = bodyque_head
    
#  make a body que entry for the given ent so the ent can be
#  respawned elsewhere

def CopyToBodyQue(ent, *qwp_extra):
    global bodyque_head
    bodyque_head.skin = ent.skin
    bodyque_head.angles = ent.angles
    bodyque_head.model = ent.model
    bodyque_head.modelindex = ent.modelindex
    bodyque_head.frame = ent.frame
    bodyque_head.colormap = ent.colormap
    bodyque_head.movetype = ent.movetype
    bodyque_head.velocity = ent.velocity
    bodyque_head.flags = 0
    qc.setorigin(bodyque_head, ent.origin)
    qc.setsize(bodyque_head, ent.mins, ent.maxs)
    bodyque_head = bodyque_head.owner
    


def qwp_reset_world(*qwp_extra):
    global lastspawn
    global bodyque_head
    lastspawn = engine.world
    bodyque_head = engine.world
