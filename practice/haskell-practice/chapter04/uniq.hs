import           Data.List

main = do cs <- getContents
          putStrLn $ unlines $ map head $ group $ sort $ lines cs
