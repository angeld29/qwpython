###
### Generated by QuakeC -> Python translator
### Id: qc2python.py,v 1.4 2001/02/05 16:26:04 barryp Exp 
###
from qwpython.qwsv import engine, Vector
from qwpython.qcsupport import qc

import defs
import teamplay
import ctfgame

#  time of last status update
#  is the status bar on?
PLAYERSTATTIME = 1.75

def MOTD(*qwp_extra):
    if qc.self.motd_count < 4:
        qc.self.motd_count += 1
        if qc.self.classname == 'spectator':
            qc.centerprint(qc.self, 'Welcome!\012Running ThreeWave CTF 4.21\012\012\303\301\320\324\325\322\305 \324\310\305 \306\314\301\307!\012')
            return 
            
        if defs.gamestart:
            qc.centerprint(qc.self, 'Welcome!\012Running ThreeWave CTF 4.21\012\012\303\301\320\324\325\322\305 \324\310\305 \306\314\301\307!\012\012Choose an exit...\012') # red
            return 
            
        if qc.self.steam == teamplay.TEAM_COLOR1:
            qc.centerprint(qc.self, 'Welcome!\012Running ThreeWave CTF 4.21\012\012\303\301\320\324\325\322\305 \324\310\305 \306\314\301\307!\012\012You are \322\305\304 team\012') # red
        else:
            qc.centerprint(qc.self, 'Welcome!\012Running Threewave CTF 4.21\012\012\303\301\320\324\325\322\305 \324\310\305 \306\314\301\307!\012\012You are \302\314\325\305 team') # blue
        return 
        
    qc.self.sprint(defs.PRINT_HIGH, 'Impulse 70 to turn off status bar\012')
    qc.self.sprint(defs.PRINT_HIGH, 'Impulse 71 through 81 to set status bar resolution\012')
    qc.self.sprint(defs.PRINT_HIGH, '71:200 72:240 73:300 74:350 75:384 76:400 77:480 78:600 79:768 81:1024\012')
    qc.self.motd_count = 0
    

def MOTD_ChooseTeam(*qwp_extra):
    if qc.self.motd_count < 6:
        qc.self.motd_count += 1
        qc.centerprint(qc.self, 'Welcome!\012Running ThreeWave CTF 4.2\012\012\303\301\320\324\325\322\305 \324\310\305 \306\314\301\307!\012\012Press 1 for \322\305\304 team\012Press 2 for \302\314\325\305 team\012Or Press Jump for automatic team\012')
        return 
        
    qc.self.motd_count = 0
    

def TeamCaptureCheckUpdate(*qwp_extra):
    p = engine.world
    if defs.gamestart:
        return  #  handled by vote exit
    if teamplay.lastteamscrtime > qc.time:
        return 
    teamplay.lastteamscrtime = qc.time + teamplay.TEAMSCRTIME
    #  count up teamscr
    teamplay.teamscr1 = teamplay.teamscr2 = 0
    p = qc.find(qc.world, 'classname', 'player')
    while p != qc.world:
        if p.steam == teamplay.TEAM_COLOR1:
            teamplay.teamscr1 += p.frags
        elif p.steam == teamplay.TEAM_COLOR2:
            teamplay.teamscr2 += p.frags
        p = qc.find(p, 'classname', 'player')
        
    

def TeamCaptureResetUpdate(*qwp_extra):
    teamplay.lastteamscrtime = 0
    TeamCaptureCheckUpdate()
    

def TeamEndScore(*qwp_extra):
    s = None
    if defs.gamestart:
        return 
    teamplay.lastteamscrtime = 0
    TeamCaptureCheckUpdate()
    if teamplay.teamscr1 > teamplay.teamscr2:
        engine.bprint(defs.PRINT_HIGH, '\322\305\304 team won the level with ')
        s = str(teamplay.teamscr1)
        engine.bprint(defs.PRINT_HIGH, s)
        engine.bprint(defs.PRINT_HIGH, ' points!\012')
        engine.bprint(defs.PRINT_HIGH, '\302\314\325\305 team lost with ')
        s = str(teamplay.teamscr2)
        engine.bprint(defs.PRINT_HIGH, s)
        engine.bprint(defs.PRINT_HIGH, ' points.\012')
        
    elif teamplay.teamscr1 < teamplay.teamscr2:
        engine.bprint(defs.PRINT_HIGH, '\302\314\325\305 team won the level with ')
        s = str(teamplay.teamscr2)
        engine.bprint(defs.PRINT_HIGH, s)
        engine.bprint(defs.PRINT_HIGH, ' points!\012')
        engine.bprint(defs.PRINT_HIGH, '\322\305\304 team lost with ')
        s = str(teamplay.teamscr1)
        engine.bprint(defs.PRINT_HIGH, s)
        engine.bprint(defs.PRINT_HIGH, ' points.\012')
        
    else:
        engine.bprint(defs.PRINT_HIGH, '\302\314\325\305 and \322\305\304 team tied level with ')
        s = str(teamplay.teamscr1)
        engine.bprint(defs.PRINT_HIGH, s)
        engine.bprint(defs.PRINT_HIGH, ' points!\012')
        
    

def TeamSetStatRes(who, *qwp_extra):
    if who.statstate > 7: #  768 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 7: #  600 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 6: #  480 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 5: #  400
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 4: #  384 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 3: #  350 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 2: #  300 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 1: #  240 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    #  200 
    return '\012\012\012\012\012\012\012\012\012\012\012\012'
    

def TeamSetStatRes2(who, *qwp_extra):
    if who.statstate > 7: #  768 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 7: #  600 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 6: #  480 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 5: #  400
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 4: #  384 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 3: #  350 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 2: #  300 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    elif who.statstate == 1: #  240 
        return '\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012\012'
    #  200 
    return '\012\012\012\012\012\012\012\012\012\012\012'
    

def TeamCapturePlayerUpdate(*qwp_extra):
    e = engine.world
    n = None
    t = None
    s1 = None
    s2 = None
    s3 = None
    res = None
    if qc.self.laststattime > qc.time:
        return 
    TeamCaptureCheckUpdate()
    qc.self.laststattime = qc.time + PLAYERSTATTIME
    if qc.self.motd_count:
        MOTD()
        return 
        
    if qc.self.statstate < 0:
        return 
    res = TeamSetStatRes(qc.self)
    if defs.gamestart:
        if ctfgame.vote_leader == qc.world:
            qc.centerprint2(qc.self, res, '                    Choose an exit...')
        else:
            res = TeamSetStatRes2()
            n = str(ctfgame.voteexit_time - qc.time)
            qc.centerprint5(qc.self, res, ctfgame.vote_leader.message, ' leads\012', n, ' seconds until exit')
            
        return 
        
    # .1234567890123456789012345678901234567
    #  Res.R.B.             Capture The Flag
    #  Res.R.B.                     BLUE 999
    if qc.self.player_flag & defs.ITEM_RUNE1_FLAG:
        s1 = 'Resist  \205'
    elif qc.self.player_flag & defs.ITEM_RUNE2_FLAG:
        s1 = 'Strength\205'
    elif qc.self.player_flag & defs.ITEM_RUNE3_FLAG:
        s1 = 'Haste   \205'
    elif qc.self.player_flag & defs.ITEM_RUNE4_FLAG:
        s1 = 'Regen   \205'
    else:
        s1 = '        \205'
    e = qc.find(qc.world, 'classname', 'item_flag_team1')
    if e.cnt == teamplay.FLAG_AT_BASE:
        s2 = ' \205'
    elif e.cnt == teamplay.FLAG_CARRIED:
        s2 = 'R\205'
    else:
        s2 = '\322\205'
    e = qc.find(qc.world, 'classname', 'item_flag_team2')
    if e.cnt == teamplay.FLAG_AT_BASE:
        s3 = ' \205'
    elif e.cnt == teamplay.FLAG_CARRIED:
        s3 = 'B\205'
    else:
        s3 = '\302\205'
    if teamplay.teamscr1 == 0 and teamplay.teamscr2 == 0:
        qc.centerprint5(qc.self, res, s1, s2, s3, '         Capture The Flag') #  CTFBOT
        return 
        
    if qc.time < (teamplay.last_flag_capture + 6):
        if teamplay.last_capture_team == teamplay.TEAM_COLOR1:
            if teamplay.teamscr1 > teamplay.teamscr2:
                t = 'Red Capture!   RED '
                n = str(teamplay.teamscr1 - teamplay.teamscr2)
                
            elif teamplay.teamscr1 < teamplay.teamscr2:
                t = 'Red Capture!  BLUE '
                n = str(teamplay.teamscr2 - teamplay.teamscr1)
                
            else:
                t = 'Red Capture!  TIED '
                n = None
                
            
        else:
            if teamplay.teamscr1 > teamplay.teamscr2:
                t = 'Blue Capture!  RED '
                n = str(teamplay.teamscr1 - teamplay.teamscr2)
                
            elif teamplay.teamscr1 < teamplay.teamscr2:
                t = 'Blue Capture! BLUE '
                n = str(teamplay.teamscr2 - teamplay.teamscr1)
                
            else:
                t = 'Blue Capture! TIED '
                n = None
                
            
        
    else:
        if teamplay.teamscr1 > teamplay.teamscr2:
            t = '               RED '
            n = str(teamplay.teamscr1 - teamplay.teamscr2)
            
        elif teamplay.teamscr1 < teamplay.teamscr2:
            t = '              BLUE '
            n = str(teamplay.teamscr2 - teamplay.teamscr1)
            
        else:
            t = '              TIED '
            n = None
            
        
    qc.centerprint7(qc.self, res, s1, s2, s3, '    ', t, n) # 
    

def TeamPlayerUpdate(who, s, *qwp_extra):
    n = None
    res = None
    TeamCaptureCheckUpdate()
    who.laststattime = qc.time + PLAYERSTATTIME
    if who.statstate < 0:
        qc.centerprint(who, s)
        return 
        
    res = TeamSetStatRes2(who)
    if teamplay.teamscr1 == 0 and teamplay.teamscr2 == 0:
        qc.centerprint3(who, res, s, '\012                       Capture The Flag')
        
    elif teamplay.teamscr1 > teamplay.teamscr2:
        n = str(teamplay.teamscr1 - teamplay.teamscr2)
        qc.centerprint4(who, res, s, '\012                               RED ', n)
        
    elif teamplay.teamscr1 < teamplay.teamscr2:
        n = str(teamplay.teamscr2 - teamplay.teamscr1)
        qc.centerprint4(who, res, s, '\012                               BLUE ', n)
        
    else:
        qc.centerprint3(who, res, s, '\012                               TIED')
    

def TeamPlayerUpdate2(who, s1, s2, *qwp_extra):
    n = None
    res = None
    TeamCaptureCheckUpdate()
    who.laststattime = qc.time + PLAYERSTATTIME
    if who.statstate < 0:
        qc.centerprint2(who, s1, s2)
        return 
        
    res = TeamSetStatRes2(who)
    if teamplay.teamscr1 == 0 and teamplay.teamscr2 == 0:
        qc.centerprint4(who, res, s1, s2, '\012                       Capture The Flag')
        return 
        
    elif teamplay.teamscr1 > teamplay.teamscr2:
        n = str(teamplay.teamscr1 - teamplay.teamscr2)
        qc.centerprint5(who, res, s1, s2, '\012                               RED ', n)
        
    elif teamplay.teamscr1 < teamplay.teamscr2:
        n = str(teamplay.teamscr2 - teamplay.teamscr1)
        qc.centerprint5(who, res, s1, s2, '\012                               BLUE ', n)
        
    else:
        qc.centerprint4(who, res, s1, s2, '\012                               TIED')
        return 
        
    


def qwp_reset_status(*qwp_extra):
    global PLAYERSTATTIME
    PLAYERSTATTIME = 1.75
