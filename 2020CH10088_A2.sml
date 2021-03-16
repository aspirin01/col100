
        (*   Q1   *)

fun smallestDivisor(n,i)= 
if n =1  then 1
else if n mod i = 0 then i
else if (i+1)*(i+1) > n then 1
else smallestDivisor(n,i+1);
smallestDivisor(345,2);

fun isPrime(n) =
if n = 2 then true
else if n <=1 then false
else if smallestDivisor(n,2) = 1 then true 
else false;
isPrime(999999913);
isPrime(99991);
isPrime(~1);
isPrime(8609);

fun findPrimes(n) =
let 
  fun f(n,a,b) = 
  if a>n then (0,0,0) 
  else  if isPrime(a) andalso isPrime(b) andalso isPrime(n-a-b) then (a,b,n-a-b)
  else if (b < n) then f(n,a,b+1)
  else f(n,a+1,2)
in
  f(n,2,2)
end;
findPrimes(847);
findPrimes(878868);
findPrimes(454278954);
findPrimes(862);
findPrimes(254);
findPrimes(460);
findPrimes(2333);
findPrimes(655);
findPrimes(25);





            (*   Q2   *)


fun max(a,b) = if a>b then a else b;


fun maximumValue(n,W,v,w) =
if n < 0 then 0
else if W - w(n) >=0 then
max(maximumValue(n-1,W-w(n),v,w)+v(n) , maximumValue(n-1,W,v,w))
else  maximumValue(n-1,W,v,w);



                (* Q3 *)



fun toString(n) = 
if n=0 then "0"
else if n =1 then "1"
else if n =2 then "2"
else if n =3 then "3"
else if n =4 then "4"
else if n =5 then "5"
else if n =6 then "6"
else if n =7 then "7"
else if n =8 then "8"
else if n =9 then "9"
else toString(n div 10)^toString(n mod 10);
toString(642524);


fun convertUnitsRec(n,name,factor) =
let 
fun recn( n,j )=

if n < factor(j) then toString(n)^" "^name(j) 
else recn( n div factor(j), j+1)^" " ^toString(n mod factor(j))^" "^name(j)
in
 recn(n,0)
end;

fun convertUnitsIter(n,name,factor) = 
let
fun iter(n,j,ans )=
if n < factor(j) then toString(n)^" "^name(j)^ans^" "
else iter (n div factor(j), j+1," " ^toString(n mod factor(j))^" "^name(j)^ans);
in
  
iter(n, 0,"")
end;






              (* Q4 *)



fun power(x,n) = 
if n = 0 then 1
else x*power(x,n-1);



  fun g(n,k,i) =  
  if  k >n then i
  else g(n div k,k,i+1);
g(6423,4,0);

fun intSqrt2(n) = 
if n <0 then raise Fail("Imaginary square root")
else if n = 0 then 0
else 
let
  fun f(n,p,i)= 
  if p < 0 then i
  else if (2*i+1)*(2*i+1) > n div power(4,p) then f(n,p-1,2*i)
  else f(n, p-1,2*i+1)    
in
f(n,g(n,4,0),0)
end;
intSqrt2(500000000);
intSqrt2(1073741823);
intSqrt2(400000000);



                            (*___```END```___*)
  