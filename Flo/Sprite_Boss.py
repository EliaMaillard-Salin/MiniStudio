import pygame as py





def load_anim(athena):
    for elt in athena.all_anim :
        for i in range(len(elt)) :
            elt[i] = py.image.load(elt[i])
            
            

def walking(athena,fen,player):
    athena.size_img = [athena.walk[athena.walk_nb].get_width()/3,athena.walk[athena.walk_nb].get_height()/3]
    if athena.x < player.posX :
        walk = py.transform.scale( athena.walk[athena.walk_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        walk =py.transform.flip (py.transform.scale( athena.walk[athena.walk_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    py.Surface.set_colorkey(walk,(34,255,0))
    fen.blit(walk,(athena.pos_img))

def attacking(athena,fen,player):
    athena.size_img = [athena.attack_anim[athena.attack_nb].get_width()/3,athena.attack_anim[athena.attack_nb].get_height()/3]
    if athena.x < player.posX :
        att = py.transform.scale( athena.attack_anim[athena.attack_nb] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        att =py.transform.flip (py.transform.scale( athena.attack_anim[athena.attack_nb] ,(athena.size_img[0],athena.size_img[1])), True, False)
    py.Surface.set_colorkey(att,(34,255,0))
    fen.blit(att,(athena.pos_img))

def attacking_aoe(athena,fen,player):
    athena.size_img = [athena.aoe_anim[athena.aoe_nb-1].get_width()/3,athena.aoe_anim[athena.aoe_nb-1].get_height()/3]
    if athena.x < player.posX :
        aoe = py.transform.scale( athena.aoe_anim[athena.aoe_nb-1] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        aoe =py.transform.flip (py.transform.scale( athena.aoe_anim[athena.aoe_nb-1] ,(athena.size_img[0],athena.size_img[1])), True, False)
    py.Surface.set_colorkey(aoe,(34,255,0))
    fen.blit(aoe,(athena.pos_img))

def parrying(athena,fen,player):
    athena.size_img = [athena.parry_anim[athena.parry_nb-1].get_width()/3,athena.parry_anim[athena.parry_nb-1].get_height()/3]
    if athena.x < player.posX :
        par = py.transform.scale( athena.parry_anim[athena.parry_nb-1] ,(athena.size_img[0],athena.size_img[1]) )
    else :
        par =py.transform.flip (py.transform.scale( athena.parry_anim[athena.parry_nb-1] ,(athena.size_img[0],athena.size_img[1])), True, False)
    fen.blit(par,(athena.pos_img))