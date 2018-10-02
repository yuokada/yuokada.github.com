-- import System.Environment
import Data.List

main = do cs <- getContents
          -- MEMO: printの部分以外はこれでOK
          -- print $ sort $ lines cs

          -- unlines が分からなかった
          putStrLn $ unlines$ sort $ lines cs
