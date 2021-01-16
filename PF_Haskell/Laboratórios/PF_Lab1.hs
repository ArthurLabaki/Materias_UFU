dobro x = x * 2

quad x = dobro x * 2

tria cat1 cat2 = sqrt (cat1 ^ 2 + cat2 ^ 2)

dist x1 x2 y1 y2 = sqrt((x2- x1)^2 + (y2 - y1)^2)

par x = mod x 2 == 0

impar x = if par x == False
   then "e impar"
   else "e par"

ftoc x = (x - 32) * (5/9)

maior x y = max x y

maior3 x y z = max (max x y) z

func2 x = if x > 0 then "1" else if x < 0 then "-1" else "0"

ehDigito::Char->Bool
ehDigito c = c >= '0' && c <= '9'

naoEhDigito c = if ehDigito c == True then False else True

ehTriangulo hip cat1 cat2 = if hip ** 2 == (cat1 ^ 2 + cat2 ^ 2) then True else False
