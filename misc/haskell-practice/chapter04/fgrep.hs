import System.Environment
import Data.List
-- Fix from sample code

main = do args <- getArgs
          cs <- getContents
          putStrLn $ fgrep (head args) cs

-- 関数名 :: 第1引数 -> 第2引数 -> 戻り値
fgrep :: String -> String -> String
fgrep pattern cs = unlines $ filter match $ lines cs
  where
    -- パターンマッチ
    match :: String -> Bool
    match line = any prefixp $ tails line

    prefixp :: String -> Bool
    prefixp line = pattern `isPrefixOf` line
