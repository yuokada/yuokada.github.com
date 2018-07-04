object HelloWorld {

  def sum(n: Int): Int = {
    def rec_sum(nn: Int): Int = {
      nn match {
        case nn if nn <= 0 => return 0
        case _             => return nn + rec_sum(nn - 1)
      }
    }

    return rec_sum(n)
  }

  def main(args: Array[String]): Unit = {
    println("Hello, World!")
    val ls = List[Int](1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    for (j <- ls) {
      //      println(j)
      println(j, sum(j))
    }
  }
}