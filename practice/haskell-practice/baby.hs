doubleMe x = x + x
-- doubleUs x y = x * 2 + y * 2
doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100
                        then x
                        else x * 2

-- p16
boomBangs xs = [if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]

--  p18
removeNonUppercase st = [c | c <- st, c `elem` ['A'..'Z']]

-- p21, p22
let triples = [(a,b,c)| a <- [1..10], b<-[1..10], c <- [1..10]]
let rightTriangles = [(a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2]
let rightTriangles' = [(a,b,c) | c <- [1..10], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2, a + b + c == 24]

let rightTriangles = [(a,b,c) | c <- [1..100], a <- [1..c], b <- [1..a], a^2 + b^2 == c^2]
