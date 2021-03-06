
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCONJUNCTIONDISJUNCTIONleftUNTILRELEASErightNEXTFINALGLOBALNOTATOMIC CONJUNCTION DISJUNCTION FINAL GLOBAL LPAREN NEXT NOT RELEASE RPAREN UNTILexpression : LPAREN expression RPARENexpression : ATOMIC\n        expression : NOT expression\n                        | NEXT expression\n                        | GLOBAL expression\n                        | FINAL expression\n        expression : expression CONJUNCTION expression\n                        | expression DISJUNCTION expression\n                        | expression UNTIL expression\n                        | expression RELEASE expression\n        '
    
_lr_action_items = {'LPAREN':([0,2,4,5,6,7,8,9,10,11,],[2,2,2,2,2,2,2,2,2,2,]),'ATOMIC':([0,2,4,5,6,7,8,9,10,11,],[3,3,3,3,3,3,3,3,3,3,]),'NOT':([0,2,4,5,6,7,8,9,10,11,],[4,4,4,4,4,4,4,4,4,4,]),'NEXT':([0,2,4,5,6,7,8,9,10,11,],[5,5,5,5,5,5,5,5,5,5,]),'GLOBAL':([0,2,4,5,6,7,8,9,10,11,],[6,6,6,6,6,6,6,6,6,6,]),'FINAL':([0,2,4,5,6,7,8,9,10,11,],[7,7,7,7,7,7,7,7,7,7,]),'$end':([1,3,13,14,15,16,17,18,19,20,21,],[0,-2,-3,-4,-5,-6,-7,-8,-9,-10,-1,]),'CONJUNCTION':([1,3,12,13,14,15,16,17,18,19,20,21,],[8,-2,8,-3,-4,-5,-6,-7,-8,-9,-10,-1,]),'DISJUNCTION':([1,3,12,13,14,15,16,17,18,19,20,21,],[9,-2,9,-3,-4,-5,-6,-7,-8,-9,-10,-1,]),'UNTIL':([1,3,12,13,14,15,16,17,18,19,20,21,],[10,-2,10,-3,-4,-5,-6,10,10,-9,-10,-1,]),'RELEASE':([1,3,12,13,14,15,16,17,18,19,20,21,],[11,-2,11,-3,-4,-5,-6,11,11,-9,-10,-1,]),'RPAREN':([3,12,13,14,15,16,17,18,19,20,21,],[-2,21,-3,-4,-5,-6,-7,-8,-9,-10,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,5,6,7,8,9,10,11,],[1,12,13,14,15,16,17,18,19,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','generate_AST.py',51),
  ('expression -> ATOMIC','expression',1,'p_expression_atomic','generate_AST.py',55),
  ('expression -> NOT expression','expression',2,'p_expression_sinop','generate_AST.py',61),
  ('expression -> NEXT expression','expression',2,'p_expression_sinop','generate_AST.py',62),
  ('expression -> GLOBAL expression','expression',2,'p_expression_sinop','generate_AST.py',63),
  ('expression -> FINAL expression','expression',2,'p_expression_sinop','generate_AST.py',64),
  ('expression -> expression CONJUNCTION expression','expression',3,'p_expression_binop','generate_AST.py',70),
  ('expression -> expression DISJUNCTION expression','expression',3,'p_expression_binop','generate_AST.py',71),
  ('expression -> expression UNTIL expression','expression',3,'p_expression_binop','generate_AST.py',72),
  ('expression -> expression RELEASE expression','expression',3,'p_expression_binop','generate_AST.py',73),
]
