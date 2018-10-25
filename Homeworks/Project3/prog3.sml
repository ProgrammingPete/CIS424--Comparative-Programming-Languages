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
						  then largesmall(y, x, z) (*This uses recursion to cahnge the positions of the number*)
						  else if y > z
							   then largesmall(x, z, y)
							   else if x > z
							        then largesmall(z, y, x)
									else (z, x); (*If all if are false, the integers are sorted from greatest to least. *)
largesmall(a,c,b); (*All permutations tested*)
largesmall(a,b,c);
largesmall(b,a,c);
largesmall(b,c,a);
largesmall(c,a,b);
largesmall(c,b,a);

(*Problem 4: Write a function that flips alternate elements of a list*)
fun flipL(nil) = nil
	| flipL(a :: nil) = [a]  (*If a is a singleton list, then return just that element in a list*)
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
	I wrote reduce without currying. Currying uses a space for the delimiter instead of a comma and parentheses.
	This was covered in the book. There is also a built-in function that I could have used.*)
exception EmptyList

fun reduce(f, nil) = raise EmptyList
	| reduce(f, [a]) = a
	| reduce (f, x :: xr) = f(x, reduce(f, xr)) ;


(*I used my function but there is a built-in function called foldl that does the same thing. *)
reduce(fn (x, y) => if x < y then x else y, L) ; (*y is the returned value from the recursively called function. *)

(* Problem 7: Uses built in function List.filter. The built in function uses currying, which uses a space as a delimiter instead of a comma.  *)
List.filter (fn x => x >= 2.0 andalso x <= 3.0) negLreal ;