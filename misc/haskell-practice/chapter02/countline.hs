main = do cs <- getContents
          print $ length $ lines cs
          -- print $ lines cs
