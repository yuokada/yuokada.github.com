-- import System.Environment
import Data.List

main = do cs <- getContents
          -- ここからUniq化する
          -- sortからのgroupでUniq
          print $ group $ sort $ lines cs
        --  [["AK\tAlaska","AK\tAlaska"],["AL\tAlabama","AL\tAlabama"],["AR\tArkansas","AR\tArkansas"],["AZ\tArizona","AZ\tArizona"],["CA\tCalifolnia","CA\tCalifolnia"]]
-- TODO: Group化した結果をMapでListに変換すればOK?
