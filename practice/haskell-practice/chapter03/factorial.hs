-- factorial
-- main = putStrLn "Hello World"
--        putStrLn $ factorial 10

factorial :: Int -> Int
factorial 1 = 1
factorial n = n * factorial  (n - 1)
