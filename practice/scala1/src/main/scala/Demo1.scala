//package io.github.yuokada.scala

import java.util.ArrayList

object Demo1 {

  def main(args: Array[String]): Unit = {
    println("HEllo World!")
    val xlist = new ArrayList[String]()
    for (i <- 1 to 10) {
      xlist.add("foo")
    }
    println(xlist)
  }
}
