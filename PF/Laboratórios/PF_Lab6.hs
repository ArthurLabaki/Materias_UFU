--  Lab 6 -- Let e Where
--1
analisaIMC :: Float -> Float -> String
analisaIMC p a | imc <= 18.5 = "Voce esta abaixo do peso ideal."
               | imc <= 25.0 = "Seu peso parece normal."
               | imc <= 30.0 = "Voce esta acima do peso ideal."
               | otherwise =  "Voce esta obeso."
             where imc = p/(a*2)
-- OU
analisaIMC2 :: Float -> Float -> String
analisaIMC2 p a = s
             where imc = p/(a*2) ;s =if (imc <= 18.5) 
                          then "Voce esta abaixo do peso ideal." 
                          else if ( imc <= 25.0) 
                          then "Seu peso parece normal."
                          else if(imc <= 30.0) 
                          then "Voce esta acima do peso ideal."
                          else "Voce esta obeso."

-- 2
analisaIMClet :: Float -> Float -> String
analisaIMClet p a = let imc = p/(a*2) ;s =if (imc <= 18.5) 
                          then "Voce esta abaixo do peso ideal." 
                          else if ( imc <= 25.0) 
                          then "Seu peso parece normal."
                          else if(imc <= 30.0) 
                          then "Voce esta acima do peso ideal."
                          else "Voce esta obeso."
                    in s

-- 3
raizeswhere :: Float -> Float -> Float -> (Float, Float, Float)
raizeswhere a b c = ((-b + sqrt(d))/ (2*a), (-b - sqrt(d))/ (2*a), d)
                    where d = (b*b) - (4 *a*c)

-- 4
raizeslet :: Float -> Float -> Float -> (Float, Float, Float)
raizeslet a b c = let d = (b*b) - (4 *a*c) in ((-b + sqrt(d))/ (2*a), (-b - sqrt(d))/ (2*a), d)

-- 5
pares :: [Int] -> ([Int], Int)
pares  [] = ([], 0)
pares (x:xs) = if ( mod x 2 == 0) then ([x] ++ fst(pares xs),prs) else pares xs
               where prs = 1+ snd (pares xs)