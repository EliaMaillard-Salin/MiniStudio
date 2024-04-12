import pygame as py





def load_anim(athena):
    for elt in athena.all_anim :
        for i in range(len(elt)) :
            elt[i] = py.image.load(elt[i])
            
            

def walking(athena,fen,player):
    athena.size_img = [athena.walk[athena.walk_nb].get_width()/6,athena.walk[athena.walk_nb].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6 + 20
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3*1.5+10
        walk = py.transform.scale( athena.walk[athena.walk_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3*1.5+10 
        walk =py.transform.flip (py.transform.scale( athena.walk[athena.walk_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(walk,(athena.pos_img))

def attacking(athena,fen,player):
    athena.size_img = [athena.attack_anim[athena.attack_nb].get_width()/6,athena.attack_anim[athena.attack_nb].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x- athena.size_img[0]/18*9
        att = py.transform.scale( athena.attack_anim[athena.attack_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        athena.pos_img[0] = athena.x- athena.size_img[0]/18*7
        att =py.transform.flip (py.transform.scale( athena.attack_anim[athena.attack_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(att,(athena.pos_img))

def attacking_aoe(athena,fen,player):
    athena.size_img = [athena.aoe_anim[athena.aoe_nb-1].get_width()/6,athena.aoe_anim[athena.aoe_nb-1].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x - athena.size_img[0]/30*15
        aoe = py.transform.scale( athena.aoe_anim[athena.aoe_nb-1] ,(athena.size_img[0],athena.size_img[1]) )

    else :
        athena.pos_img[0] = athena.x - athena.size_img[0]/30*13
        aoe =py.transform.flip (py.transform.scale( athena.aoe_anim[athena.aoe_nb-1] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(aoe,(athena.pos_img))

def parrying(athena,fen,player):
    athena.size_img = [athena.parry_anim[athena.parry_nb-1].get_width()/6,athena.parry_anim[athena.parry_nb-1].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3 - 10
        par = py.transform.scale( athena.parry_anim[athena.parry_nb-1] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3*1.5+20
        par =py.transform.flip (py.transform.scale( athena.parry_anim[athena.parry_nb-1] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(par,(athena.pos_img))

def idle(athena,fen,player):
    athena.size_img = [athena.idle_anim[athena.idle_nb].get_width()/6,athena.idle_anim[athena.idle_nb].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6 + 20
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3*1.5+10
        idl = py.transform.scale( athena.idle_anim[athena.idle_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        athena.pos_img[0] = athena.x- athena.size_img[0]/3*1.5+10
        idl =py.transform.flip (py.transform.scale( athena.idle_anim[athena.idle_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(idl,(athena.pos_img))

def provoc(athena,fen,player):
    athena.size_img = [athena.provoc_anim[athena.provoc_nb].get_width()/6,athena.provoc_anim[athena.provoc_nb].get_height()/6]
    athena.pos_img[1] = athena.y- athena.size_img[1]/10*6 + 20
    if athena.x < player.posX :
        athena.pos_img[0] = athena.x- athena.size_img[0]/18*9
        pvc = py.transform.scale( athena.provoc_anim[athena.provoc_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        athena.pos_img[0] = athena.x- athena.size_img[0]/18*7
        pvc =py.transform.flip (py.transform.scale( athena.provoc_anim[athena.provoc_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(pvc,(athena.pos_img))

def onde(athena,fen ,player):
    athena.size_onde = [athena.onde_anim[athena.onde_nb].get_width()/15,athena.onde_anim[athena.onde_nb].get_height()/15]
    athena.pos_onde[1] = athena.shockwave_y - athena.size_onde[1]/10*8+5
    athena.pos_onde[0] = athena.x- athena.size_onde[0]/18*9
    onde1 = py.transform.scale( athena.onde_anim[athena.onde_nb] ,(athena.size_onde[0],athena.size_onde[1]) )
    onde2 = py.transform.flip (py.transform.scale( athena.onde_anim[athena.onde_nb] ,(athena.size_onde[0],athena.size_onde[1])), True, False)
    fen.blit(onde1,(athena.shockwave_r_x - athena.size_onde[0]/10-70,athena.pos_onde[1]))
    fen.blit(onde2,(athena.shockwave_l_x - athena.size_onde[0]/10,athena.pos_onde[1]))