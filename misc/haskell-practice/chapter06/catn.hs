main = do cs <- getContents
          putStrLn cs

numbering :: String -> String
numbering cs = unlines $ map format $ zipLineNumber  $ lines cs


zipLineNumber :: [String] -> [(Int, String)]
zipLineNumber xs = zip [1..] xs

-- 
format xs =
