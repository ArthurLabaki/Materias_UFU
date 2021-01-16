conversao x = (x, x*3.96, x*4.45)

bissexto :: Int -> Bool
bissexto x |( mod x 4 == 0 ) && ( mod x 100 /= 0) = True
           |( mod x 400 == 0) = True
           |otherwise = False

type Data = (Int, Int, Int)
bissexto2 :: Data -> Bool 
bissexto2 (a, b ,x) | ( mod x 4 == 0 ) && ( mod x 100 /= 0) = True
                    | ( mod x 400 == 0) = True
                    | otherwise = False

valida :: Data -> Bool 
valida (a, b, c) | (b==1 || b==3 || b==5 || b==7 || b==8 || b==10 || b==12) && (a>=1 && a<=31) = True
                 | (b==4 || b==6 || b==9 || b==11) && (a>=1 && a<=30) = True
                 | (b==2 && bissexto c) &&  (a>=1 && a<=29) = True
                 | (b==2) &&  (a>=1 && a<=28) = True
                 | otherwise = False

precede :: Data -> Data ->Bool
precede (a, b, c) (d, e, f) | (valida (a,b,c) && valida (d,e,f)) && (c < f)= True
                            | (valida (a,b,c) && valida (d,e,f)) && (c == f) && (b < e) = True
                            | (valida (a,b,c) && valida (d,e,f)) && (c == f) && (b == e) && (a < d) = True
                            | otherwise = False

type Livro = (String, String, String, String, Int)
type Aluno = (String, String, String, Int)
type Emprestimo = (String, String, Data, Data, String)

el :: Emprestimo 
el = ("H123C9","BSI200945",(12,9,2009),(20,9,2009),"aberto")

verif :: Emprestimo-> Data ->Bool
verif (a, b, (da,db,dc),(dd, df, dg),c) (x, y, z) = if precede (x,y,z) (dd,df,dg) == True then True else False 
-- ou
-- verif (a, b, (da,db,dc),(dd, df, dg),c) (x, y, z) | precede (x,y,z) (dd,df,dg) = True
--                                                   | otherwise = False