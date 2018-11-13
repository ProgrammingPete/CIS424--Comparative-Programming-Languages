
male(mushu).
male(tangdee).
female(mulan).
female(beumei).
female(gugu).

father(baba,mushu).
father(baba,mulan).
father(yeye,baba).
father(yeye,gugu).
father(yeye,susu).
father(susu,tangdee).
father(zengzufu,yeye).
father(jojo,beumei).

mother(mama,mushu).
mother(mama,mulan).
mother(popo,mama).
mother(popo,jojo).

%added rules. A parent can be ether a mother or a father.
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y).

sibling(X,Y):- parent(Z,X), parent(Z,Y), not(X = Y).
brother(X,Y):- sibling(X,Y), male(X).
aunt(X,Y):- parent(Z,Y), sibling(Z,X), female(X).
granddaughter(X,Y):- female(X), parent(Z,X), parent(Y,Z).
descendant(X,Y) :- parent(Y,X).

%Problem 2
lastelm(X, [X]).
lastelm(X, [_|Z]) :- lastelm(X,Z).

%Problem 3 Parser
match(X,[X|T], T).
z([],[]).
s(X0, X) :- match(x,X0, X1), xs(X1, X).
xs(X0, X) :-  match(x,X0, X1), xs(X1, X).
xs(X0, X) :- ys(X0, X).
ys(X0, X) :- match(y, X0, X1), zs(X1, X).
zs(X0, X) :- z(X0,X).
zs(X0, X) :- match(y, X0, X1), zs(X1, X).

member(Elm, [Elm|T]) :- !. % this prevents backtracking from trying to resatisfy goals after another subgoal has failed.
member(Elm , [_|T]) :- member(Elm, T).
tests(d).
dem_candidate(X) :- member(X, [a,b,c,d,e]), tests(X).
