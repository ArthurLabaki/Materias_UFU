fatorial :: Int->Int
fatorial 0 = 1
fatorial n = n* fatorial (n-1)


fib :: Int->Int
fib 1 = 1
fib 2 = 1
fib n = (fib (n-1)) + (fib (n-2))


n_tri :: Int->Int
n_tri 0 = 0
n_tri 1 = 1
n_tri n = n_tri (n-1) + n


--Pulando o ex 4 e o 5 --


pot2 :: Int -> Int
pot2 0 = 1
pot2 1 = 2
pot2 n = (pot2 (n-1)) * 2


prodIntervalo :: Int -> Int -> Int
prodIntervalo m n = if(n == m+1) then m*n else m * (prodIntervalo (m+1) n)

fato :: Int ->Int
fato x = prodIntervalo 1 x


resto_div :: Int -> Int ->Int
resto_div m n = if(m-n == 0) then 0 else if (m < n ) then m else (resto_div (m-n) n)

div_inteira :: Int -> Int ->Int
div_inteira m n = if(m-n == 0) then 1 else if (m < n) then 0 else (div_inteira (m-n) n) +1


mdcguard :: Int->Int->Int
mdcguard m n | (n == 0) = m
             | (n > 0) = (mdcguard n (mod m n))

mdccasa :: Int -> Int -> Int
mdccasa m 0 = m
mdccasa m n = if(n > 0) then (mdccasa n (mod m n)) else 0


binoguard :: Int -> Int -> Int
binoguard n k | (k == 0 ) = 0
              | (k == n ) = 1
              | (k < n ) && (k > 0) = (binoguard (n-1) k) + (binoguard (n-1) (k-1))

binocasa :: Int -> Int -> Int
binocasa n 0 = 0
binocasa n k = if (k == n) then 1 else if ((k < n ) && (k > 0)) then (binoguard (n-1) k) + (binoguard (n-1) (k-1)) else 0


-- Ex 4 e o 5 --


passo ::[Int] -> [Int]
passo [x, y] = [y, y+x]

fib2 :: Int-> [Int]
fib2 1 = [1]
fib2 2 = [1]
fib2 3 = [1,2]
fib2 n = head(passo(fib2 (n-1)))


lstfib50 = [fib x | x <- [1..50]]
lstfib250 = [fib2 x | x <- [1..50]] 

-- A fib (Implementado em sala) demorou cerca de 1 hora(e nao terminou).
-- A fib2 (implementado com pares (x,y)) executou quase instantaneamente.
-- A fib2 tem q executar n recurcões(no caso n = 50), tendo N como grau de complexidade.
-- Já a fib tem q executar 2 recurçoes para cada n, sendo 2^N seu grau de complexidade .
