main = do cs <- getContents
          print $ firstNLines 10 cs
          -- print $ length $ lines cs
          -- print $ lines cs
firstNLines n cs = unlines $ take n $ lines cs
