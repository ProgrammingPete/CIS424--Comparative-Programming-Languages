
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

%addedrules
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y).

sibling(X,Y):- parent(Z,X), parent(Z,Y), not(X = Y).
brother(X,Y):- sibling(X,Y), male(X).
aunt(X,Y):- parent(Z,Y), sibling(Z,X), female(X).
granddaughter(X,Y):- female(X), ! , parent(Z,X), parent(Y,Z).
descendant(X,Y) :- parent(Y,X).

%Problem 2
lastelm(X, [X]).
lastelm(X, [_|Z]) :- lastelm(X,Z).

