main = do cs <- getContents
          print $ lastNLines 10 cs
          -- print $ length $ lines cs
          -- print $ lines cs
lastNLines n cs = unlines $ takeLast n $ lines cs
takeLast n ss = reverse $ take n $ reverse ss
