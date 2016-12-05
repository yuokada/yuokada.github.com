-- $ runghc chapter04/uniq.hs < chapter04/practice_uniq.txt 
-- AK	Alaska
-- AL	Alabama
-- AR	Arkansas
-- AZ	Arizona
-- CA	Califolnia
--
import           Data.List

main = do cs <- getContents
          putStrLn $ unlines $ map head $ group $ sort $ lines cs
