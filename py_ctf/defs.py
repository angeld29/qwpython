###
### Generated by QuakeC -> Python translator
### Id: qc2python.py,v 1.4 2001/02/05 16:26:04 barryp Exp 
###
from qwpython.qwsv import engine, Vector
from qwpython.qcsupport import qc


# 
# ==============================================================================
# 
# 			SOURCE FOR GLOBALVARS_T C STRUCTURE
# 
# ==============================================================================
# 
# 
#  system globals
# 
#  if this is set, the entity that just
#  run created a new missile that should
#  be simulated immediately
#  force all entities to touch triggers
#  next frame.  this is needed because
#  non-moving things don't normally scan
#  for triggers, and when a trigger is
#  created (like a teleport trigger), it
#  needs to catch everything.
#  decremented each frame, so set to 2
#  to guarantee everything is touched
#  propagated from level to level, used to
#  keep track of completed episodes
#  number of secrets found
#  number of monsters killed
#  spawnparms are used to encode information about clients across server
#  level changes
# 
#  global variables set by built in functions
# 	
#  set by makevectors()
#  set by traceline / tracebox
#  destination of single entity writes
# 
#  required prog functions
# 
#  only for testing
#  call after setting the parm1... parms
#  called when a client first connects to
#  a server. sets parms so they can be
#  saved off for restarts
#  call to set parms for self so they can
#  be saved for a level transition
# ================================================
#  flag for structure dumping
# ================================================
# 
# ==============================================================================
# 
# 			SOURCE FOR ENTVARS_T C STRUCTURE
# 
# ==============================================================================
# 
# 
#  system fields (*** = do not set in prog code, maintained by C code)
# 
#  *** model index in the precached list
#  *** origin + mins / maxs
#  local time for entity
#  *** to allow entities to run out of sequence
#  ***
#  ***
#  spawn function
#  bounding box extents reletive to origin
#  maxs - mins
#  for doors or plats, called when can't push other
#  stats
#  one of the IT_SHOTGUN, etc flags
#  bit flags
#  add to origin to get eye point
#  fire
#  use
#  jump
#  weapon changes
#  view / targeting angle for players
#  players maximum health is stored here
#  don't back up
#  save this fraction of incoming damage
#  0 = not in, 1 = feet, 2 = wast, 3 = eyes
#  a contents value
#  a movetarget or an enemy
#  damage is accumulated through a frame. and sent as one single
#  message, so the super shotgun doesn't generate huge messages
#  who launched a missile
#  mostly for doors, but also used for waterjump
#  trigger messages
#  either a cd track number or sound number
#  contains names of wavs to play
# ================================================
#  flag for structure dumping
# ================================================
# 
# ==============================================================================
# 
# 				VARS NOT REFERENCED BY C CODE
# 
# ==============================================================================
# 
# 
#  constants
# 
FALSE = 0
TRUE = 1
#  edict.flags
FL_FLY = 1
FL_SWIM = 2
FL_CLIENT = 8 #  set for all client edicts
FL_INWATER = 16 #  for enter / leave water splash
FL_MONSTER = 32
FL_GODMODE = 64 #  player cheat
FL_NOTARGET = 128 #  player cheat
FL_ITEM = 256 #  extra wide size for bonus items
FL_ONGROUND = 512 #  standing on something
FL_PARTIALGROUND = 1024 #  not all corners are valid
FL_WATERJUMP = 2048 #  player jumping out of water
FL_JUMPRELEASED = 4096 #  for jump debouncing
#  edict.movetype values
MOVETYPE_NONE = 0 #  never moves
# float	MOVETYPE_ANGLENOCLIP	= 1;
# float	MOVETYPE_ANGLECLIP		= 2;
MOVETYPE_WALK = 3 #  players only
MOVETYPE_STEP = 4 #  discrete, not real time unless fall
MOVETYPE_FLY = 5
MOVETYPE_TOSS = 6 #  gravity
MOVETYPE_PUSH = 7 #  no clip to world, push and crush
MOVETYPE_NOCLIP = 8
MOVETYPE_FLYMISSILE = 9 #  fly with extra size against monsters
MOVETYPE_BOUNCE = 10
MOVETYPE_BOUNCEMISSILE = 11 #  bounce with extra size
#  edict.solid values
SOLID_NOT = 0 #  no interaction with other objects
SOLID_TRIGGER = 1 #  touch on edge, but not blocking
SOLID_BBOX = 2 #  touch on edge, block
SOLID_SLIDEBOX = 3 #  touch on edge, but not an onground
SOLID_BSP = 4 #  bsp clip, touch on edge, block
#  range values
RANGE_MELEE = 0
RANGE_NEAR = 1
RANGE_MID = 2
RANGE_FAR = 3
#  deadflag values
DEAD_NO = 0
DEAD_DYING = 1
DEAD_DEAD = 2
DEAD_RESPAWNABLE = 3
#  takedamage values
DAMAGE_NO = 0
DAMAGE_YES = 1
DAMAGE_AIM = 2
#  items
IT_AXE = 4096
IT_SHOTGUN = 1
IT_SUPER_SHOTGUN = 2
IT_NAILGUN = 4
IT_SUPER_NAILGUN = 8
IT_GRENADE_LAUNCHER = 16
IT_ROCKET_LAUNCHER = 32
IT_LIGHTNING = 64
IT_GRAPPLE = 128
IT_SHELLS = 256
IT_NAILS = 512
IT_ROCKETS = 1024
IT_CELLS = 2048
IT_ARMOR1 = 8192
IT_ARMOR2 = 16384
IT_ARMOR3 = 32768
IT_SUPERHEALTH = 65536
IT_KEY1 = 131072
IT_KEY2 = 262144
IT_INVISIBILITY = 524288
IT_INVULNERABILITY = 1048576
IT_SUIT = 2097152
IT_QUAD = 4194304
IT_SIGIL1 = 268435456
IT_SIGIL2 = 536870912
IT_SIGIL3 = 1073741824
IT_SIGIL4 = 0x80000000
#  point content values
CONTENT_EMPTY = -1
CONTENT_SOLID = -2
CONTENT_WATER = -3
CONTENT_SLIME = -4
CONTENT_LAVA = -5
CONTENT_SKY = -6
STATE_TOP = 0
STATE_BOTTOM = 1
STATE_UP = 2
STATE_DOWN = 3
VEC_ORIGIN = Vector(0, 0, 0)
VEC_HULL_MIN = Vector(-16, -16, -24)
VEC_HULL_MAX = Vector(16, 16, 32)
VEC_HULL2_MIN = Vector(-32, -32, -24)
VEC_HULL2_MAX = Vector(32, 32, 64)
#  protocol bytes
SVC_TEMPENTITY = 23
SVC_KILLEDMONSTER = 27
SVC_FOUNDSECRET = 28
SVC_INTERMISSION = 30
SVC_FINALE = 31
SVC_CDTRACK = 32
SVC_SELLSCREEN = 33
SVC_SMALLKICK = 34
SVC_BIGKICK = 35
SVC_MUZZLEFLASH = 39
TE_SPIKE = 0
TE_SUPERSPIKE = 1
TE_GUNSHOT = 2
TE_EXPLOSION = 3
TE_TAREXPLOSION = 4
TE_LIGHTNING1 = 5
TE_LIGHTNING2 = 6
TE_WIZSPIKE = 7
TE_KNIGHTSPIKE = 8
TE_LIGHTNING3 = 9
TE_LAVASPLASH = 10
TE_TELEPORT = 11
TE_BLOOD = 12
TE_LIGHTNINGBLOOD = 13
#  sound channels
#  channel 0 never willingly overrides
#  other channels (1-7) allways override a playing sound on that channel
CHAN_AUTO = 0
CHAN_WEAPON = 1
CHAN_VOICE = 2
CHAN_ITEM = 3
CHAN_BODY = 4
CHAN_NO_PHS_ADD = 8 #  ie: CHAN_BODY+CHAN_NO_PHS_ADD
ATTN_NONE = 0
ATTN_NORM = 1
ATTN_IDLE = 2
ATTN_STATIC = 3
#  update types
UPDATE_GENERAL = 0
UPDATE_STATIC = 1
UPDATE_BINARY = 2
UPDATE_TEMP = 3
#  entity effects
# float	EF_BRIGHTFIELD	= 1;
# float	EF_MUZZLEFLASH 	= 2;
EF_BRIGHTLIGHT = 4
EF_DIMLIGHT = 8
EF_FLAG1 = 16
EF_FLAG2 = 32
#  messages
MSG_BROADCAST = 0 #  unreliable to all
MSG_ONE = 1 #  reliable to one (msg_entity)
MSG_ALL = 2 #  reliable to all
MSG_INIT = 3 #  write to the init string
MSG_MULTICAST = 4 #  for multicast() call
#  message levels
PRINT_LOW = 0 #  pickup messages
PRINT_MEDIUM = 1 #  death messages
PRINT_HIGH = 2 #  critical messages
PRINT_CHAT = 3 #  also goes to chat console
#  multicast sets
MULTICAST_ALL = 0 #  every client
MULTICAST_PHS = 1 #  within hearing
MULTICAST_PVS = 2 #  within sight
MULTICAST_ALL_R = 3 #  every client, reliable
MULTICAST_PHS_R = 4 #  within hearing, reliable
MULTICAST_PVS_R = 5 #  within sight, reliable
runespawn = engine.world
runespawned = 0
gamestart = 0 #  at start
# ================================================
# 
#  globals
# 
movedist = 0
gameover = 0 #  set when a rule exits
string_null = None #  null string, nothing should be held here
empty_float = 0
activator = engine.world #  the entity that activated a trigger or brush
damage_attacker = engine.world #  set by T_Damage
framecount = 0
# 
#  cvars checked each frame
# 
teamplay = 0
timelimit = 0
fraglimit = 0
deathmatch = 0
# ================================================
# 
#  world fields (FIXME: make globals)
# 
#  0=medieval 1=metal 2=base
# ================================================
# 
#  quakeed fields
# 
#  not used by game, but parsed by light util
# 
#  monster ai
# 
#  mad at this player before taking damage
#  Monsters use this. I use it to flag the player's CHAN_WEAP
#  to be cleared (see client.qc) -Wedge
AS_STRAIGHT = 1
AS_SLIDING = 2
AS_MELEE = 3
AS_MISSILE = 4
# 
#  player only fields
# 
#  *TEAMPLAY*
#  Current team player is on
#  time of last team set
#  selected ctf skin
#  selected ctf skin
#  *XXX* EXPERT CTF ALTERNATE SCORING
#  time values
#  how long a player has had the flag
#  last time player returned his own flag
#  last time player fragged a flag carrier
#  last time player hurt the flag carrier
#  *XXX* end 
#  Zoid Additions
#  Used to set Maxspeed on a player
#  Gravity Multiplier (0 to 1.0)
# RUNE: Elder Magic
# RUNE: Hell Magic
#  set to time+0.2 whenever a client fires a
#  weapon or takes damage.  Used to alert
#  monsters that otherwise would let the player go
#  player jump flag
#  player swimming sound flag
#  when time > air_finished, start drowning
#  keeps track of the number of bubbles
#  keeps track of how the player died
#  misc flags (skins, etc.)
#  how long we should stay dead
#  time to next regen
#  last time we notified about multi-runes
#  non-zero if voted
#  ZOID: Runes
ITEM_RUNE1_FLAG = 1
ITEM_RUNE2_FLAG = 2
ITEM_RUNE3_FLAG = 4
ITEM_RUNE4_FLAG = 8
ITEM_RUNE_MASK = 15
#  ZOID: Capture the flag
ITEM_ENEMY_FLAG = 16
#  TEAMPLAY
TEAM_STUFF_COLOR = 32
#  Connection tracking
PF_GHOST = 64
#  have we been killed yet
# McBain: PreviousWeaponCommand
#  one of the IT_SHOTGUN, etc flags
# 
#  object stuff
# 
#  angle at start
#  only used by secret door
# 
#  doors, etc
# 
#  time from firing to restarting
#  time from activation to firing
#  door's trigger entity
# 
#  monsters
# 
# 
#  doors
# 
#  damage done by door when hit
# 
#  misc
# 
#  misc flag
# 
#  subs
# 
# 
#  triggers
# 
#  for counting triggers
# 
#  plats / doors / buttons
# 
#  top and bottom positions
# 
#  sounds
# 
# ===========================================================================
# 
#  builtin functions
# 
#  sets v_forward, etc globals
#  set movetype and solid first
#  #5 was removed
#  returns 0 - 1
#  sets trace_* globals
#  nomonsters can be:
#  An entity will also be ignored for testing if forent == test,
#  forent->owner == test, or test->owner == forent
#  a forent of world is ignored
#  returns a client to look for
#  prints all edicts
#  turns statment trace on
#  prints an entire edict
#  returns TRUE or FALSE
#  #33 was removed
#  TRUE if landed on floor
#  round to nearest int
#  largest integer <= v
#  smallest integer >= v
#  #39 was removed
#  true if self is on ground
#  returns a CONTENT_*
#  #42 was removed
#  returns the shooting vector
#  return cvar.value
#  put string into local que
#  for looping through all ents
#  #48 was removed
#  turn towards self.ideal_yaw
#  at self.yaw_speed
#  #50 was removed
# 
#  direct client message generation
# 
#  several removed
#  no effect except for -copy
# #71 was removed
#  sets cvar.value
#  sprint, but in middle
#  sprint, but in middle
#  sprint, but in middle
#  sprint, but in middle
#  sprint, but in middle
#  sprint, but in middle
#  sprint, but in middle
#  registered version only
#  registered version only
#  registered version only
#  set parm1... to the
#  values at level start
#  for coop respawn
#  add to stats
#  get a key value (world = serverinfo)
#  convert string to float
#  sends the temp message to a set
#  of clients, possibly in PVS or PHS
# ============================================================================
# 
#  subs.qc
# 
# 
# 	combat.qc
# 
#  health function
# 
#  Grapple.qc - Wedge 
# 
#  TRUE if hook is anchored and client is being pulled
#  TRUE if hook is in use
#  pointer to client's hook


def qwp_reset_defs(*qwp_extra):
    global FALSE
    global TRUE
    global FL_FLY
    global FL_SWIM
    global FL_CLIENT
    global FL_INWATER
    global FL_MONSTER
    global FL_GODMODE
    global FL_NOTARGET
    global FL_ITEM
    global FL_ONGROUND
    global FL_PARTIALGROUND
    global FL_WATERJUMP
    global FL_JUMPRELEASED
    global MOVETYPE_NONE
    global MOVETYPE_WALK
    global MOVETYPE_STEP
    global MOVETYPE_FLY
    global MOVETYPE_TOSS
    global MOVETYPE_PUSH
    global MOVETYPE_NOCLIP
    global MOVETYPE_FLYMISSILE
    global MOVETYPE_BOUNCE
    global MOVETYPE_BOUNCEMISSILE
    global SOLID_NOT
    global SOLID_TRIGGER
    global SOLID_BBOX
    global SOLID_SLIDEBOX
    global SOLID_BSP
    global RANGE_MELEE
    global RANGE_NEAR
    global RANGE_MID
    global RANGE_FAR
    global DEAD_NO
    global DEAD_DYING
    global DEAD_DEAD
    global DEAD_RESPAWNABLE
    global DAMAGE_NO
    global DAMAGE_YES
    global DAMAGE_AIM
    global IT_AXE
    global IT_SHOTGUN
    global IT_SUPER_SHOTGUN
    global IT_NAILGUN
    global IT_SUPER_NAILGUN
    global IT_GRENADE_LAUNCHER
    global IT_ROCKET_LAUNCHER
    global IT_LIGHTNING
    global IT_GRAPPLE
    global IT_SHELLS
    global IT_NAILS
    global IT_ROCKETS
    global IT_CELLS
    global IT_ARMOR1
    global IT_ARMOR2
    global IT_ARMOR3
    global IT_SUPERHEALTH
    global IT_KEY1
    global IT_KEY2
    global IT_INVISIBILITY
    global IT_INVULNERABILITY
    global IT_SUIT
    global IT_QUAD
    global IT_SIGIL1
    global IT_SIGIL2
    global IT_SIGIL3
    global IT_SIGIL4
    global CONTENT_EMPTY
    global CONTENT_SOLID
    global CONTENT_WATER
    global CONTENT_SLIME
    global CONTENT_LAVA
    global CONTENT_SKY
    global STATE_TOP
    global STATE_BOTTOM
    global STATE_UP
    global STATE_DOWN
    global VEC_ORIGIN
    global VEC_HULL_MIN
    global VEC_HULL_MAX
    global VEC_HULL2_MIN
    global VEC_HULL2_MAX
    global SVC_TEMPENTITY
    global SVC_KILLEDMONSTER
    global SVC_FOUNDSECRET
    global SVC_INTERMISSION
    global SVC_FINALE
    global SVC_CDTRACK
    global SVC_SELLSCREEN
    global SVC_SMALLKICK
    global SVC_BIGKICK
    global SVC_MUZZLEFLASH
    global TE_SPIKE
    global TE_SUPERSPIKE
    global TE_GUNSHOT
    global TE_EXPLOSION
    global TE_TAREXPLOSION
    global TE_LIGHTNING1
    global TE_LIGHTNING2
    global TE_WIZSPIKE
    global TE_KNIGHTSPIKE
    global TE_LIGHTNING3
    global TE_LAVASPLASH
    global TE_TELEPORT
    global TE_BLOOD
    global TE_LIGHTNINGBLOOD
    global CHAN_AUTO
    global CHAN_WEAPON
    global CHAN_VOICE
    global CHAN_ITEM
    global CHAN_BODY
    global CHAN_NO_PHS_ADD
    global ATTN_NONE
    global ATTN_NORM
    global ATTN_IDLE
    global ATTN_STATIC
    global UPDATE_GENERAL
    global UPDATE_STATIC
    global UPDATE_BINARY
    global UPDATE_TEMP
    global EF_BRIGHTLIGHT
    global EF_DIMLIGHT
    global EF_FLAG1
    global EF_FLAG2
    global MSG_BROADCAST
    global MSG_ONE
    global MSG_ALL
    global MSG_INIT
    global MSG_MULTICAST
    global PRINT_LOW
    global PRINT_MEDIUM
    global PRINT_HIGH
    global PRINT_CHAT
    global MULTICAST_ALL
    global MULTICAST_PHS
    global MULTICAST_PVS
    global MULTICAST_ALL_R
    global MULTICAST_PHS_R
    global MULTICAST_PVS_R
    global runespawn
    global runespawned
    global gamestart
    global movedist
    global gameover
    global string_null
    global empty_float
    global activator
    global damage_attacker
    global framecount
    global teamplay
    global timelimit
    global fraglimit
    global deathmatch
    global AS_STRAIGHT
    global AS_SLIDING
    global AS_MELEE
    global AS_MISSILE
    global ITEM_RUNE1_FLAG
    global ITEM_RUNE2_FLAG
    global ITEM_RUNE3_FLAG
    global ITEM_RUNE4_FLAG
    global ITEM_RUNE_MASK
    global ITEM_ENEMY_FLAG
    global TEAM_STUFF_COLOR
    global PF_GHOST
    FALSE = 0
    TRUE = 1
    FL_FLY = 1
    FL_SWIM = 2
    FL_CLIENT = 8
    FL_INWATER = 16
    FL_MONSTER = 32
    FL_GODMODE = 64
    FL_NOTARGET = 128
    FL_ITEM = 256
    FL_ONGROUND = 512
    FL_PARTIALGROUND = 1024
    FL_WATERJUMP = 2048
    FL_JUMPRELEASED = 4096
    MOVETYPE_NONE = 0
    MOVETYPE_WALK = 3
    MOVETYPE_STEP = 4
    MOVETYPE_FLY = 5
    MOVETYPE_TOSS = 6
    MOVETYPE_PUSH = 7
    MOVETYPE_NOCLIP = 8
    MOVETYPE_FLYMISSILE = 9
    MOVETYPE_BOUNCE = 10
    MOVETYPE_BOUNCEMISSILE = 11
    SOLID_NOT = 0
    SOLID_TRIGGER = 1
    SOLID_BBOX = 2
    SOLID_SLIDEBOX = 3
    SOLID_BSP = 4
    RANGE_MELEE = 0
    RANGE_NEAR = 1
    RANGE_MID = 2
    RANGE_FAR = 3
    DEAD_NO = 0
    DEAD_DYING = 1
    DEAD_DEAD = 2
    DEAD_RESPAWNABLE = 3
    DAMAGE_NO = 0
    DAMAGE_YES = 1
    DAMAGE_AIM = 2
    IT_AXE = 4096
    IT_SHOTGUN = 1
    IT_SUPER_SHOTGUN = 2
    IT_NAILGUN = 4
    IT_SUPER_NAILGUN = 8
    IT_GRENADE_LAUNCHER = 16
    IT_ROCKET_LAUNCHER = 32
    IT_LIGHTNING = 64
    IT_GRAPPLE = 128
    IT_SHELLS = 256
    IT_NAILS = 512
    IT_ROCKETS = 1024
    IT_CELLS = 2048
    IT_ARMOR1 = 8192
    IT_ARMOR2 = 16384
    IT_ARMOR3 = 32768
    IT_SUPERHEALTH = 65536
    IT_KEY1 = 131072
    IT_KEY2 = 262144
    IT_INVISIBILITY = 524288
    IT_INVULNERABILITY = 1048576
    IT_SUIT = 2097152
    IT_QUAD = 4194304
    IT_SIGIL1 = 268435456
    IT_SIGIL2 = 536870912
    IT_SIGIL3 = 1073741824
    IT_SIGIL4 = 0x80000000
    CONTENT_EMPTY = -1
    CONTENT_SOLID = -2
    CONTENT_WATER = -3
    CONTENT_SLIME = -4
    CONTENT_LAVA = -5
    CONTENT_SKY = -6
    STATE_TOP = 0
    STATE_BOTTOM = 1
    STATE_UP = 2
    STATE_DOWN = 3
    VEC_ORIGIN = Vector(0, 0, 0)
    VEC_HULL_MIN = Vector(-16, -16, -24)
    VEC_HULL_MAX = Vector(16, 16, 32)
    VEC_HULL2_MIN = Vector(-32, -32, -24)
    VEC_HULL2_MAX = Vector(32, 32, 64)
    SVC_TEMPENTITY = 23
    SVC_KILLEDMONSTER = 27
    SVC_FOUNDSECRET = 28
    SVC_INTERMISSION = 30
    SVC_FINALE = 31
    SVC_CDTRACK = 32
    SVC_SELLSCREEN = 33
    SVC_SMALLKICK = 34
    SVC_BIGKICK = 35
    SVC_MUZZLEFLASH = 39
    TE_SPIKE = 0
    TE_SUPERSPIKE = 1
    TE_GUNSHOT = 2
    TE_EXPLOSION = 3
    TE_TAREXPLOSION = 4
    TE_LIGHTNING1 = 5
    TE_LIGHTNING2 = 6
    TE_WIZSPIKE = 7
    TE_KNIGHTSPIKE = 8
    TE_LIGHTNING3 = 9
    TE_LAVASPLASH = 10
    TE_TELEPORT = 11
    TE_BLOOD = 12
    TE_LIGHTNINGBLOOD = 13
    CHAN_AUTO = 0
    CHAN_WEAPON = 1
    CHAN_VOICE = 2
    CHAN_ITEM = 3
    CHAN_BODY = 4
    CHAN_NO_PHS_ADD = 8
    ATTN_NONE = 0
    ATTN_NORM = 1
    ATTN_IDLE = 2
    ATTN_STATIC = 3
    UPDATE_GENERAL = 0
    UPDATE_STATIC = 1
    UPDATE_BINARY = 2
    UPDATE_TEMP = 3
    EF_BRIGHTLIGHT = 4
    EF_DIMLIGHT = 8
    EF_FLAG1 = 16
    EF_FLAG2 = 32
    MSG_BROADCAST = 0
    MSG_ONE = 1
    MSG_ALL = 2
    MSG_INIT = 3
    MSG_MULTICAST = 4
    PRINT_LOW = 0
    PRINT_MEDIUM = 1
    PRINT_HIGH = 2
    PRINT_CHAT = 3
    MULTICAST_ALL = 0
    MULTICAST_PHS = 1
    MULTICAST_PVS = 2
    MULTICAST_ALL_R = 3
    MULTICAST_PHS_R = 4
    MULTICAST_PVS_R = 5
    runespawn = engine.world
    runespawned = 0
    gamestart = 0
    movedist = 0
    gameover = 0
    string_null = None
    empty_float = 0
    activator = engine.world
    damage_attacker = engine.world
    framecount = 0
    teamplay = 0
    timelimit = 0
    fraglimit = 0
    deathmatch = 0
    AS_STRAIGHT = 1
    AS_SLIDING = 2
    AS_MELEE = 3
    AS_MISSILE = 4
    ITEM_RUNE1_FLAG = 1
    ITEM_RUNE2_FLAG = 2
    ITEM_RUNE3_FLAG = 4
    ITEM_RUNE4_FLAG = 8
    ITEM_RUNE_MASK = 15
    ITEM_ENEMY_FLAG = 16
    TEAM_STUFF_COLOR = 32
    PF_GHOST = 64
