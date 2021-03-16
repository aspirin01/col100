(* This is the program for Q1. *)

fun climbStair(n) = 
if n = 0 then 0
else if n<0 then raise Fail("Invalid stair count")
else if n = 1 then 1
else if n  = 2 then 2
else  climbStair(n-1) + climbStair(n-2);
climbStair(22);
climbStair(~15);

(* Code is completed. Please scroll to next code. *)







(* This is the program for Q2. *)

fun modifiedDigitSum(n) =
if n = 0 then 0
else (n mod 10) + 2*modifiedDigitSum((n) div 10);
modifiedDigitSum(132);
modifiedDigitSum(442457397);

(* Code is completed. Please scroll to next code. *)









(* This is the program for Q3. *)

fun sqrt(n) = 
if n = 0 then 0 
else 
let 
  fun g(a) =
  if n <  0 then raise Fail("Invalid input")
  else if n = a*a then a
  else if a*a > n then 0
  else g(a+1); 
in 
 g(0)
end;
sqrt(49);
sqrt(~1);


fun squaredCount(n) =
 if n = 0 then 0
else 
   let  
    fun q(n,a) = 
    if n < a*a then 0
    else  
      let 
        val b = sqrt(n-(a*a))
      in 
    if b>0 then 1
    else  q(n,a+1)
 end;
in
q(n,0) + squaredCount(n-1)
end;
squaredCount(300);
squaredCount(24);
squaredCount(7);

(* Code is completed. Please scroll to next code. *)







(* This is the program for Q4. *)

fun nilakanthaSum(t)  = 
let 
  val N = floor(t)
in
  if N = 0 then 3.0
else if N mod 2 = 1 then  nilakanthaSum(t-1.0) + 4.0/((2.0*t)*(2.0*t +1.0)*(2.0*t +2.0)) 
else  nilakanthaSum(t-1.0) -  4.0/((2.0*t)*(2.0*t +1.0)*(2.0*t +2.0)) 
end;
nilakanthaSum(9999.0);
nilakanthaSum(1.0);

                        
                        (* END *)















