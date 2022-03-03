
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASSIGN COMMA DIV DKHY DKHZ ELSE EQ FOR GE GT IDENT IF INT LE LT MUL NE NUMBER SEMI SUB WHILE XKHY XKHZ ZKHY ZKHZ\n    Function : Type IDENT XKHZ XKHY CompoundStmt\n             | Type IDENT XKHZ ArgList XKHY CompoundStmt\n    \n    ArgList : Arg\n            | ArgList COMMA Arg\n    Arg : Type IDENTDeclaration : Type IdentList SEMI\n    Type : INT\n    \n    IdentList : IdentList COMMA IDENT\n              | IDENT\n    \n    Stmt : ForStmt\n         | WhileStmt\n         | Expr SEMI\n         | IfStmt\n         | CompoundStmt\n         | Declaration\n         | SEMI\n    \n    ForStmt : FOR XKHZ OptExpr SEMI OptExpr SEMI OptExpr XKHY Stmt\n    \n    OptExpr : Expr\n            | \n    \n    WhileStmt : WHILE XKHZ Expr XKHY Stmt\n    \n    IfStmt : IF XKHZ Expr XKHY Stmt ElsePart\n    \n    ElsePart : ELSE Stmt\n             |\n    \n    CompoundStmt : DKHZ StmtList DKHY\n    \n    StmtList : StmtList Stmt\n             | \n    \n    Expr : IDENT ASSIGN Expr\n         | Rvalue\n    \n    Rvalue : Rvalue Compare Mag\n           | Mag\n    \n    Compare : EQ \n            | LT \n            | GT \n            | LE \n            | GE \n            | NE\n    \n    Mag : Mag ADD Term\n        | Mag SUB Term\n        | Term\n    \n    Term : Term MUL Factor\n         | Term DIV Factor\n         | Factor\n    \n    Factor : XKHZ Expr XKHY\n           | SUB Factor\n           | ADD Factor\n           | IDENT\n           | NUMBER\n    '
    
_lr_action_items = {'INT':([0,5,12,14,15,18,19,20,21,23,24,25,26,40,69,76,77,80,81,83,84,86,87,88,],[3,3,-26,3,3,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,3,3,-20,-23,-21,3,-22,3,-17,]),'$end':([1,11,16,18,],[0,-1,-2,-24,]),'IDENT':([2,3,6,12,15,18,19,20,21,23,24,25,26,28,33,35,37,40,41,43,44,45,46,47,48,49,50,51,52,55,56,59,60,69,70,75,76,77,80,81,82,83,84,86,87,88,],[4,-7,10,-26,30,-24,-25,-10,-11,-16,-13,-14,-15,30,54,58,58,-12,30,30,30,58,-31,-32,-33,-34,-35,-36,30,58,58,58,58,-6,78,30,30,30,-20,-23,30,-21,30,-22,30,-17,]),'XKHZ':([4,12,15,18,19,20,21,23,24,25,26,27,28,29,32,35,37,40,41,43,44,45,46,47,48,49,50,51,52,55,56,59,60,69,75,76,77,80,81,82,83,84,86,87,88,],[5,-26,28,-24,-25,-10,-11,-16,-13,-14,-15,41,28,43,52,28,28,-12,28,28,28,28,-31,-32,-33,-34,-35,-36,28,28,28,28,28,-6,28,28,28,-20,-23,28,-21,28,-22,28,-17,]),'XKHY':([5,8,9,10,17,30,31,34,36,38,39,42,57,58,61,63,64,65,66,67,68,71,72,73,74,82,85,],[7,13,-3,-5,-4,-46,-28,-30,-39,-42,-47,64,-45,-46,-44,-18,-43,76,-27,-29,77,-37,-38,-40,-41,-19,87,]),'DKHZ':([7,12,13,15,18,19,20,21,23,24,25,26,40,69,76,77,80,81,83,84,86,87,88,],[12,-26,12,12,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,12,12,-20,-23,-21,12,-22,12,-17,]),'COMMA':([8,9,10,17,53,54,78,],[14,-3,-5,-4,70,-9,-8,]),'DKHY':([12,15,18,19,20,21,23,24,25,26,40,69,80,81,83,86,88,],[-26,18,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,-20,-23,-21,-22,-17,]),'SEMI':([12,15,18,19,20,21,22,23,24,25,26,30,31,34,36,38,39,40,41,53,54,57,58,61,62,63,64,66,67,69,71,72,73,74,75,76,77,78,79,80,81,83,84,86,87,88,],[-26,23,-24,-25,-10,-11,40,-16,-13,-14,-15,-46,-28,-30,-39,-42,-47,-12,-19,69,-9,-45,-46,-44,75,-18,-43,-27,-29,-6,-37,-38,-40,-41,-19,23,23,-8,82,-20,-23,-21,23,-22,23,-17,]),'FOR':([12,15,18,19,20,21,23,24,25,26,40,69,76,77,80,81,83,84,86,87,88,],[-26,27,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,27,27,-20,-23,-21,27,-22,27,-17,]),'WHILE':([12,15,18,19,20,21,23,24,25,26,40,69,76,77,80,81,83,84,86,87,88,],[-26,29,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,29,29,-20,-23,-21,29,-22,29,-17,]),'IF':([12,15,18,19,20,21,23,24,25,26,40,69,76,77,80,81,83,84,86,87,88,],[-26,32,-24,-25,-10,-11,-16,-13,-14,-15,-12,-6,32,32,-20,-23,-21,32,-22,32,-17,]),'SUB':([12,15,18,19,20,21,23,24,25,26,28,30,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,64,67,69,71,72,73,74,75,76,77,80,81,82,83,84,86,87,88,],[-26,37,-24,-25,-10,-11,-16,-13,-14,-15,37,-46,56,37,-39,37,-42,-47,-12,37,37,37,37,-31,-32,-33,-34,-35,-36,37,37,37,-45,-46,37,37,-44,-43,56,-6,-37,-38,-40,-41,37,37,37,-20,-23,37,-21,37,-22,37,-17,]),'ADD':([12,15,18,19,20,21,23,24,25,26,28,30,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,55,56,57,58,59,60,61,64,67,69,71,72,73,74,75,76,77,80,81,82,83,84,86,87,88,],[-26,35,-24,-25,-10,-11,-16,-13,-14,-15,35,-46,55,35,-39,35,-42,-47,-12,35,35,35,35,-31,-32,-33,-34,-35,-36,35,35,35,-45,-46,35,35,-44,-43,55,-6,-37,-38,-40,-41,35,35,35,-20,-23,35,-21,35,-22,35,-17,]),'NUMBER':([12,15,18,19,20,21,23,24,25,26,28,35,37,40,41,43,44,45,46,47,48,49,50,51,52,55,56,59,60,69,75,76,77,80,81,82,83,84,86,87,88,],[-26,39,-24,-25,-10,-11,-16,-13,-14,-15,39,39,39,-12,39,39,39,39,-31,-32,-33,-34,-35,-36,39,39,39,39,39,-6,39,39,39,-20,-23,39,-21,39,-22,39,-17,]),'ELSE':([18,20,21,23,24,25,26,40,69,80,81,83,86,88,],[-24,-10,-11,-16,-13,-14,-15,-12,-6,-20,84,-21,-22,-17,]),'ASSIGN':([30,],[44,]),'MUL':([30,36,38,39,57,58,61,64,71,72,73,74,],[-46,59,-42,-47,-45,-46,-44,-43,59,59,-40,-41,]),'DIV':([30,36,38,39,57,58,61,64,71,72,73,74,],[-46,60,-42,-47,-45,-46,-44,-43,60,60,-40,-41,]),'EQ':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,46,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),'LT':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,47,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),'GT':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,48,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),'LE':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,49,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),'GE':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,50,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),'NE':([30,31,34,36,38,39,57,58,61,64,67,71,72,73,74,],[-46,51,-30,-39,-42,-47,-45,-46,-44,-43,-29,-37,-38,-40,-41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Function':([0,],[1,]),'Type':([0,5,14,15,76,77,84,87,],[2,6,6,33,33,33,33,33,]),'ArgList':([5,],[8,]),'Arg':([5,14,],[9,17,]),'CompoundStmt':([7,13,15,76,77,84,87,],[11,16,25,25,25,25,25,]),'StmtList':([12,],[15,]),'Stmt':([15,76,77,84,87,],[19,80,81,86,88,]),'ForStmt':([15,76,77,84,87,],[20,20,20,20,20,]),'WhileStmt':([15,76,77,84,87,],[21,21,21,21,21,]),'Expr':([15,28,41,43,44,52,75,76,77,82,84,87,],[22,42,63,65,66,68,63,22,22,63,22,22,]),'IfStmt':([15,76,77,84,87,],[24,24,24,24,24,]),'Declaration':([15,76,77,84,87,],[26,26,26,26,26,]),'Rvalue':([15,28,41,43,44,52,75,76,77,82,84,87,],[31,31,31,31,31,31,31,31,31,31,31,31,]),'Mag':([15,28,41,43,44,45,52,75,76,77,82,84,87,],[34,34,34,34,34,67,34,34,34,34,34,34,34,]),'Term':([15,28,41,43,44,45,52,55,56,75,76,77,82,84,87,],[36,36,36,36,36,36,36,71,72,36,36,36,36,36,36,]),'Factor':([15,28,35,37,41,43,44,45,52,55,56,59,60,75,76,77,82,84,87,],[38,38,57,61,38,38,38,38,38,38,38,73,74,38,38,38,38,38,38,]),'Compare':([31,],[45,]),'IdentList':([33,],[53,]),'OptExpr':([41,75,82,],[62,79,85,]),'ElsePart':([81,],[83,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Function","S'",1,None,None,None),
  ('Function -> Type IDENT XKHZ XKHY CompoundStmt','Function',5,'p_function','myparser.py',14),
  ('Function -> Type IDENT XKHZ ArgList XKHY CompoundStmt','Function',6,'p_function','myparser.py',15),
  ('ArgList -> Arg','ArgList',1,'p_arglist','myparser.py',26),
  ('ArgList -> ArgList COMMA Arg','ArgList',3,'p_arglist','myparser.py',27),
  ('Arg -> Type IDENT','Arg',2,'p_arg','myparser.py',38),
  ('Declaration -> Type IdentList SEMI','Declaration',3,'p_declaration','myparser.py',43),
  ('Type -> INT','Type',1,'p_type','myparser.py',50),
  ('IdentList -> IdentList COMMA IDENT','IdentList',3,'p_identlist','myparser.py',58),
  ('IdentList -> IDENT','IdentList',1,'p_identlist','myparser.py',59),
  ('Stmt -> ForStmt','Stmt',1,'p_stmt','myparser.py',72),
  ('Stmt -> WhileStmt','Stmt',1,'p_stmt','myparser.py',73),
  ('Stmt -> Expr SEMI','Stmt',2,'p_stmt','myparser.py',74),
  ('Stmt -> IfStmt','Stmt',1,'p_stmt','myparser.py',75),
  ('Stmt -> CompoundStmt','Stmt',1,'p_stmt','myparser.py',76),
  ('Stmt -> Declaration','Stmt',1,'p_stmt','myparser.py',77),
  ('Stmt -> SEMI','Stmt',1,'p_stmt','myparser.py',78),
  ('ForStmt -> FOR XKHZ OptExpr SEMI OptExpr SEMI OptExpr XKHY Stmt','ForStmt',9,'p_forstmt','myparser.py',86),
  ('OptExpr -> Expr','OptExpr',1,'p_optexpr','myparser.py',94),
  ('OptExpr -> <empty>','OptExpr',0,'p_optexpr','myparser.py',95),
  ('WhileStmt -> WHILE XKHZ Expr XKHY Stmt','WhileStmt',5,'p_whilestmt','myparser.py',106),
  ('IfStmt -> IF XKHZ Expr XKHY Stmt ElsePart','IfStmt',6,'p_ifstmt','myparser.py',114),
  ('ElsePart -> ELSE Stmt','ElsePart',2,'p_elsepart','myparser.py',122),
  ('ElsePart -> <empty>','ElsePart',0,'p_elsepart','myparser.py',123),
  ('CompoundStmt -> DKHZ StmtList DKHY','CompoundStmt',3,'p_compoundstmt','myparser.py',134),
  ('StmtList -> StmtList Stmt','StmtList',2,'p_stmtlist','myparser.py',142),
  ('StmtList -> <empty>','StmtList',0,'p_stmtlist','myparser.py',143),
  ('Expr -> IDENT ASSIGN Expr','Expr',3,'p_expr','myparser.py',155),
  ('Expr -> Rvalue','Expr',1,'p_expr','myparser.py',156),
  ('Rvalue -> Rvalue Compare Mag','Rvalue',3,'p_rvalue','myparser.py',167),
  ('Rvalue -> Mag','Rvalue',1,'p_rvalue','myparser.py',168),
  ('Compare -> EQ','Compare',1,'p_compare','myparser.py',179),
  ('Compare -> LT','Compare',1,'p_compare','myparser.py',180),
  ('Compare -> GT','Compare',1,'p_compare','myparser.py',181),
  ('Compare -> LE','Compare',1,'p_compare','myparser.py',182),
  ('Compare -> GE','Compare',1,'p_compare','myparser.py',183),
  ('Compare -> NE','Compare',1,'p_compare','myparser.py',184),
  ('Mag -> Mag ADD Term','Mag',3,'p_mag','myparser.py',192),
  ('Mag -> Mag SUB Term','Mag',3,'p_mag','myparser.py',193),
  ('Mag -> Term','Mag',1,'p_mag','myparser.py',194),
  ('Term -> Term MUL Factor','Term',3,'p_term','myparser.py',206),
  ('Term -> Term DIV Factor','Term',3,'p_term','myparser.py',207),
  ('Term -> Factor','Term',1,'p_term','myparser.py',208),
  ('Factor -> XKHZ Expr XKHY','Factor',3,'p_factor','myparser.py',219),
  ('Factor -> SUB Factor','Factor',2,'p_factor','myparser.py',220),
  ('Factor -> ADD Factor','Factor',2,'p_factor','myparser.py',221),
  ('Factor -> IDENT','Factor',1,'p_factor','myparser.py',222),
  ('Factor -> NUMBER','Factor',1,'p_factor','myparser.py',223),
]
