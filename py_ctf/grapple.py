###
### Generated by QuakeC -> Python translator
### Id: qc2python.py,v 1.4 2001/02/05 16:26:04 barryp Exp 
###
from qwpython.qwsv import engine, Vector
from qwpython.qcsupport import qc

import defs
import subs
import combat
import weapons

# 
# ===========================================================================
# grapple.qc 12/29/96
# 
# Quakeworld-friendly grapple hook code by Wedge (Steve Bond)
#            visit Quake Command http://www.nuc.net/quake 
# 
# 
# Original 'Morning Star' (Grapple Hook) by "Mike" <amichael@asu.alasu.edu> 
# I took care to preserve the speed and damage values of the original
# Morning Star. Depending on latency, performance should be near exact.
# ===========================================================================
# 
#  prototypes for WEAPONS.QC functions
# 
#  Reset_Grapple - Removes the hook and resets its owner's state.
#                  expects a pointer to the hook
# 

def Reset_Grapple(rhook, *qwp_extra):
    if rhook.owner == qc.world:
        return 
    rhook.owner.sound(defs.CHAN_NO_PHS_ADD + defs.CHAN_WEAPON, 'weapons/bounce2.wav', 1, defs.ATTN_NORM)
    rhook.owner.on_hook = defs.FALSE
    rhook.owner.hook_out = defs.FALSE
    rhook.owner.weaponframe = 0
    rhook.owner.attack_finished = qc.time + 0.25
    rhook.think = subs.SUB_Remove
    rhook.nextthink = qc.time
    
# 
#  Grapple_Track - Constantly updates the hook's position relative to
#                  what it's hooked to. Inflicts damage if attached to
#                  a player that is not on the same team as the hook's
#                  owner.
# 

def Grapple_Track(*qwp_extra):
    #  Release dead targets
    if qc.self.enemy.classname == 'player' and qc.self.enemy.health <= 0:
        qc.self.owner.on_hook = defs.FALSE
        qc.self.owner.attack_finished = qc.time + 0.75
        
    #  drop the hook if owner is dead or has released the button
    if not qc.self.owner.on_hook or qc.self.owner.health <= 0:
        Reset_Grapple(qc.self)
        return 
        
    #  bring the pAiN!
    if qc.self.enemy.classname == 'player':
        #  4.1, if we can't see our enemy, unlock
        if not combat.CanDamage(qc.self.enemy, qc.self.owner):
            Reset_Grapple(qc.self)
            return 
            
        #  move the hook along with the player.  It's invisible, but
        #  we need this to make the sound come from the right spot
        qc.setorigin(qc.self, qc.self.enemy.origin)
        qc.self.sound(defs.CHAN_WEAPON, 'blob/land1.wav', 1, defs.ATTN_NORM)
        combat.T_Damage(qc.self.enemy, qc.self, qc.self.owner, 1)
        qc.makevectors(qc.self.v_angle)
        weapons.SpawnBlood(qc.self.enemy.origin, 1)
        
    #  If the hook is not attached to the player, constantly copy
    #  copy the target's velocity. Velocity copying DOES NOT work properly
    #  for a hooked client. 
    if qc.self.enemy.classname != 'player':
        qc.self.velocity = qc.self.enemy.velocity
    qc.self.nextthink = qc.time + 0.1
    
# 
#  MakeLink - spawns the chain link entities
# 

def MakeLink(*qwp_extra):
    qc.newmis = qc.spawn()
    qc.newmis.movetype = defs.MOVETYPE_FLYMISSILE
    qc.newmis.solid = defs.SOLID_NOT
    qc.newmis.owner = qc.self #  SELF is the hook!
    qc.newmis.avelocity = Vector(200, 200, 200)
    qc.newmis.setmodel('progs/bit.mdl')
    qc.setorigin(qc.newmis, qc.self.origin)
    qc.setsize(qc.newmis, Vector(0, 0, 0), Vector(0, 0, 0))
    return qc.newmis
    
# 
#  Remove_Chain - Removes all chain link entities; this is a separate
#                 function because CLIENT also needs to be able
#                 to remove the chain. Only one function required to
#                 remove all links.
# 

def Remove_Chain(*qwp_extra):
    qc.self.think = subs.SUB_Remove
    qc.self.nextthink = qc.time
    if qc.self.goalentity:
        qc.self.goalentity.think = subs.SUB_Remove
        qc.self.goalentity.nextthink = qc.time
        if qc.self.goalentity.goalentity:
            qc.self.goalentity.goalentity.think = subs.SUB_Remove
            qc.self.goalentity.goalentity.nextthink = qc.time
            
        
    
# 
#  Update_Chain - Repositions the chain links each frame. This single function
#                 maintains the positions of all of the links. Only one link
#                 is thinking every frame. 
# 

def Update_Chain(*qwp_extra):
    temp = Vector(0, 0, 0)
    if not qc.self.owner.hook_out:
        qc.self.think = Remove_Chain
        qc.self.nextthink = qc.time
        return 
        
    temp = (qc.self.owner.hook.origin - qc.self.owner.origin)
    #  These numbers are correct assuming 3 links.
    #  4 links would be *20 *40 *60 and *80
    qc.setorigin(qc.self, qc.self.owner.origin + temp * 0.25)
    qc.setorigin(qc.self.goalentity, qc.self.owner.origin + temp * 0.5)
    qc.setorigin(qc.self.goalentity.goalentity, qc.self.owner.origin + temp * 0.75)
    qc.self.nextthink = qc.time + 0.1
    
# 
#  Build_Chain - Builds the chain (linked list)
# 

def Build_Chain(*qwp_extra):
    qc.self.goalentity = MakeLink()
    qc.self.goalentity.think = Update_Chain
    qc.self.goalentity.nextthink = qc.time + 0.1
    qc.self.goalentity.owner = qc.self.owner
    qc.self.goalentity.goalentity = MakeLink()
    qc.self.goalentity.goalentity.goalentity = MakeLink()
    
# 
#  Check_Overhead - Makes sure there is sufficient headroom above the player
#                   so that setorigin doesn't stick them into a wall. I tried
#                   to compare pointcontents, but that was too flaky.
# 

def Check_Overhead(*qwp_extra):
    src = Vector(0, 0, 0)
    end = Vector(0, 0, 0)
    qc.makevectors(qc.self.owner.angles)
    #  The following comparisons could be optimized by doing away with
    #  SRC and END, and plugging the values directly into the traceline
    #  function calls. Using SRC and END made debugging easier. You
    #  decide if it's worth it.
    #  quick check right above head
    src = qc.self.owner.origin - Vector(0, 0, 24)
    end = qc.self.owner.origin - Vector(0, 0, 24)
    qc.traceline(src, end, defs.FALSE, qc.self.owner)
    if qc.trace_fraction != 1.0:
        return defs.FALSE
    src = qc.self.owner.origin - Vector(0, 0, 24) - qc.v_forward * 16
    end = qc.self.owner.origin - Vector(0, 0, 24) - qc.v_forward * 16 + Vector(0, 0, 58)
    qc.traceline(src, end, defs.FALSE, qc.self.owner)
    if qc.trace_fraction != 1.0:
        return defs.FALSE
    src = qc.self.owner.origin - Vector(0, 0, 24) + qc.v_forward * 16
    end = qc.self.owner.origin - Vector(0, 0, 24) + qc.v_forward * 16 + Vector(0, 0, 58)
    qc.traceline(src, end, defs.FALSE, qc.self.owner)
    if qc.trace_fraction != 1.0:
        return defs.FALSE
    src = qc.self.owner.origin - Vector(0, 0, 24) - qc.v_right * 16
    end = qc.self.owner.origin - Vector(0, 0, 24) - qc.v_right * 16 + Vector(0, 0, 58)
    qc.traceline(src, end, defs.FALSE, qc.self.owner)
    if qc.trace_fraction != 1.0:
        return defs.FALSE
    src = qc.self.owner.origin - Vector(0, 0, 24) + qc.v_right * 16
    end = qc.self.owner.origin - Vector(0, 0, 24) + qc.v_right * 16 + Vector(0, 0, 58)
    qc.traceline(src, end, defs.FALSE, qc.self.owner)
    if qc.trace_fraction != 1.0:
        return defs.FALSE
    return defs.TRUE
    
# 
#  Anchor_Grapple - Tries to anchor the grapple to whatever it touches
# 

def Anchor_Grapple(*qwp_extra):
    test = 0
    if qc.other == qc.self.owner:
        return 
    #  DO NOT allow the grapple to hook to any projectiles, no matter WHAT!
    #  if you create new types of projectiles, make sure you use one of the
    #  classnames below or write code to exclude your new classname so
    #  grapples will not stick to them.
    if qc.other.classname == 'missile' or qc.other.classname == 'grenade' or qc.other.classname == 'spike' or qc.other.classname == 'hook':
        return 
    #  Don't stick the the sky.
    if engine.pointcontents(qc.self.origin) == defs.CONTENT_SKY:
        Reset_Grapple(qc.self)
        return 
        
    if qc.other.classname == 'player':
        #  glance off of teammates
        if qc.other.steam == qc.self.owner.steam:
            return 
        qc.self.sound(defs.CHAN_WEAPON, 'player/axhit1.wav', 1, defs.ATTN_NORM)
        combat.T_Damage(qc.other, qc.self, qc.self.owner, 10)
        #  make hook invisible since we will be pulling directly
        #  towards the player the hook hit. Quakeworld makes it
        #  too quirky to try to match hook's velocity with that of
        #  the client that it hit. 
        qc.self.setmodel(None)
        
    elif qc.other.classname != 'player':
        qc.self.sound(defs.CHAN_WEAPON, 'player/axhit2.wav', 1, defs.ATTN_NORM)
        #  One point of damage inflicted upon impact. Subsequent
        #  damage will only be done to PLAYERS... this way secret
        #  doors and triggers will only be damaged once.
        if qc.other.takedamage:
            combat.T_Damage(qc.other, qc.self, qc.self.owner, 1)
        qc.self.velocity = Vector(0, 0, 0)
        qc.self.avelocity = Vector(0, 0, 0)
        
    #  conveniently clears the sound channel of the CHAIN1 sound,
    #  which is a looping sample and would continue to play. Tink1 is
    #  the least offensive choice, ass NULL.WAV loops and clogs the
    #  channel with silence
    qc.self.owner.sound(defs.CHAN_NO_PHS_ADD + defs.CHAN_WEAPON, 'weapons/tink1.wav', 1, defs.ATTN_NORM)
    if not qc.self.owner.button0:
        Reset_Grapple(qc.self)
        return 
        
    # 
    #         // our last chance to avoid being picked up off of the ground.
    #         // check over the client's head to make sure there is one unit
    #         // clearance so we can lift him off of the ground.
    #         test = Check_Overhead ();
    #         if (!test)
    #         {
    #                 Reset_Grapple (self);
    #                 return;
    #         }
    # 
    # 
    if qc.self.owner.flags & defs.FL_ONGROUND:
        qc.self.owner.flags -= defs.FL_ONGROUND
        #                 setorigin(self.owner,self.owner.origin + '0 0 1');
        
    qc.self.owner.on_hook = defs.TRUE
    qc.self.owner.sound(defs.CHAN_WEAPON, 'weapons/chain2.wav', 1, defs.ATTN_NORM)
    #  CHAIN2 is a looping sample. Use LEFTY as a flag so that client.qc
    #  will know to only play the tink sound ONCE to clear the weapons
    #  sound channel. (Lefty is a leftover from AI.QC, so I reused it to
    #  avoid adding a field)
    qc.self.owner.lefty = defs.TRUE
    qc.self.enemy = qc.other #  remember this guy!
    qc.self.think = Grapple_Track
    qc.self.nextthink = qc.time
    qc.self.solid = defs.SOLID_NOT
    qc.self.touch = subs.SUB_Null
    
# 
#  Throw_Grapple - called from WEAPONS.QC, 'fires' the grapple
# 

def Throw_Grapple(*qwp_extra):
    if qc.self.hook_out: #  reject subsequent calls from player.qc
        return 
    qc.msg_entity = qc.self
    qc.WriteByte(defs.MSG_ONE, defs.SVC_SMALLKICK)
    #  chain out sound (loops)
    qc.self.sound(defs.CHAN_WEAPON, 'weapons/chain1.wav', 1, defs.ATTN_NORM)
    qc.newmis = qc.spawn()
    qc.newmis.movetype = defs.MOVETYPE_FLYMISSILE
    qc.newmis.solid = defs.SOLID_BBOX
    qc.newmis.owner = qc.self #  newmis belongs to me
    qc.self.hook = qc.newmis #  This is my newmis
    qc.newmis.classname = 'hook'
    qc.makevectors(qc.self.v_angle)
    qc.newmis.velocity = qc.v_forward * 800
    qc.newmis.avelocity = Vector(0, 0, -500)
    qc.newmis.touch = Anchor_Grapple
    qc.newmis.think = Build_Chain
    qc.newmis.nextthink = qc.time + 0.1 #  don't jam newmis and links into same packet
    qc.newmis.setmodel('progs/star.mdl')
    qc.setorigin(qc.newmis, qc.self.origin + qc.v_forward * 16 + Vector(0, 0, 16))
    qc.setsize(qc.newmis, Vector(0, 0, 0), Vector(0, 0, 0))
    qc.self.hook_out = defs.TRUE
    
# 
#  Service_Grapple - called each frame by CLIENT.QC if client is ON_HOOK
# 

def Service_Grapple(*qwp_extra):
    hook_dir = Vector(0, 0, 0)
    #  drop the hook if player lets go of button
    if not qc.self.button0:
        if qc.self.weapon == defs.IT_GRAPPLE:
            Reset_Grapple(qc.self.hook)
            return 
            
        
    #  If hooked to a player, track them directly!
    if qc.self.hook.enemy.classname == 'player':
        hook_dir = (qc.self.hook.enemy.origin - qc.self.origin)
    #  else, track to hook
    elif qc.self.hook.enemy.classname != 'player':
        hook_dir = (qc.self.hook.origin - qc.self.origin)
    qc.self.velocity = hook_dir.normalize() * 750
    if hook_dir.length() <= 100 and qc.self.lefty: #  cancel chain sound
        #  If there is a chain, ditch it now. We're
        #  close enough. Having extra entities lying around
        #  is never a good idea.
        if qc.self.hook.goalentity:
            qc.self.hook.goalentity.think = Remove_Chain
            qc.self.hook.goalentity.nextthink = qc.time
            
        qc.self.sound(defs.CHAN_NO_PHS_ADD + defs.CHAN_WEAPON, 'weapons/chain3.wav', 1, defs.ATTN_NORM)
        qc.self.lefty = defs.FALSE #  we've reset the sound channel.
        
    