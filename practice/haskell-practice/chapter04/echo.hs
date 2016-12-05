import System.Environment
-- Fix from sample code

--  System.Environment.getProgName

main = do args <- getArgs
          putStrLn $ unwords args
