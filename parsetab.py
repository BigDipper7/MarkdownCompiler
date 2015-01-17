
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '!\x02E\xadP\xde\xc1\x90\xedV\xfcae\x8cD\x90'
    
_lr_action_items = {'H2':([0,15,],[3,3,]),'TEXT':([0,3,5,7,15,],[4,4,4,4,4,]),'H1':([0,15,],[5,5,]),'H3':([0,15,],[7,7,]),'CR':([2,4,6,9,10,11,12,13,14,15,16,],[-5,-12,-7,-6,-11,15,-9,-8,-10,-3,-4,]),'STRONG':([0,15,],[10,10,]),'$end':([1,2,4,6,8,9,10,11,12,13,14,15,16,],[0,-5,-12,-7,-1,-6,-11,-2,-9,-8,-10,-3,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([0,],[1,]),'setence':([0,15,],[2,16,]),'statement':([0,],[8,]),'factor':([0,3,5,7,15,],[9,12,13,14,9,]),'phrase':([0,15,],[6,6,]),'expression':([0,],[11,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> body","S'",1,None,None,None),
  ('body -> statement','body',1,'p_body','dev.py',47),
  ('statement -> expression','statement',1,'p_state','dev.py',51),
  ('expression -> expression CR','expression',2,'p_expression','dev.py',59),
  ('expression -> expression CR setence','expression',3,'p_expression','dev.py',60),
  ('expression -> setence','expression',1,'p_expression','dev.py',61),
  ('setence -> factor','setence',1,'p_setence','dev.py',68),
  ('setence -> phrase','setence',1,'p_setence','dev.py',69),
  ('phrase -> H1 factor','phrase',2,'p_phrase','dev.py',73),
  ('phrase -> H2 factor','phrase',2,'p_phrase','dev.py',74),
  ('phrase -> H3 factor','phrase',2,'p_phrase','dev.py',75),
  ('phrase -> STRONG','phrase',1,'p_phrase','dev.py',76),
  ('factor -> TEXT','factor',1,'p_factor_text','dev.py',87),
]
