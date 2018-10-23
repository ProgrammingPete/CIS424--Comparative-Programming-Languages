(*Data to be used*)
val L = [1,2,3,4,5];
val negLreal = [1.0,~1.4,~5.6,2.0, 4.0, 3.1, 2.9999];
val a = 1;
val b = 5;
val c = 7;

(*Problem 1: Return the second element of a list. Assume that the list length is at least 2*)
fun secondel(x) = hd(tl(x));
secondel(L);

(*Problem 2: Given a list, return that list with its third element deleted. Assume the length of the list is at least 3.*)
fun nothird(x :: y :: xr) = x :: y :: tl(xr);
nothird(L);


(*Problem 3: Given three integers, use nested if to produce a 2-tuple containing the (largest,smallest). At least three comparisons will be made*)
fun largesmall(x, y, z) = if x > y
						  then largesmall(y, x, z)
						  else if y > z
							   then largesmall(x, z, y)
							   else if x > z
							        then largesmall(z, y, x)
									else (z, x);
largesmall(a,c,b);

(*Problem 4: Write a function that flips alternate elements of a list*)
fun flipL(nil) = nil
	| flipL(a :: nil) = [a]
	| flipL(a :: b :: xr) = b :: a :: flipL(xr);

flipL(L);

(*Problem 5: Use the function Map and an anonymous function to replace every negative element of a list of reals by 0.0*)
(* This is making my own function *)
fun Map(f, nil) = nil
	| Map(f, x ::xr) = f(x) :: Map(f, xr);

Map(fn (x:real) => if x < 0.0 then 0.0 else x, negLreal);


(*This is using the built in function
map (fn (x:real) => if x < 0.0 then 0.0 else x) negLreal; *)

(*Problem 6:: Use the function Reduce and an anonymous function to find the minimum of a list of reals.
	I wrote reduce with currying.*)
fun reduce f b nil = b
	| reduce f  b (x :: xr) = f(x, reduce f b xr) ;


(*This is using the built in library function as foldl*)
reduce (fn (x, y) => if x < y then x else y) 5 L ; 

(* Problem 7: Uses built in function List.filter *)
List.filter (fn x => x >= 2.0 andalso x <= 3.0) negLreal;