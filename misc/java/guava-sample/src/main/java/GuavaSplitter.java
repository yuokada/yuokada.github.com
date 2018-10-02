import com.google.common.base.Splitter;

import java.util.List;

/**
 * Created by yuokada on 2017/06/29.
 */
public class GuavaSplitter
{

    public static void main(String[] args)
    {
        String sample = "a,  goo d b,c,d";
        Splitter splitter = Splitter.on(",").omitEmptyStrings().trimResults();
        List<String> ls = splitter.splitToList(sample);
        ls.stream().forEach(x -> System.out.printf("[%s]", x));  // [a][goo d b][c][d]

        System.out.println();

        String sample2 = "foo\tbar \t baz,boo";
        Splitter splitter2 = Splitter.onPattern("[,\\s]").omitEmptyStrings().trimResults();
        List<String> ls2 = splitter2.splitToList(sample2);
        ls2.stream().forEach(x -> System.out.printf("[%s]", x));  // [foo][bar][baz][boo]
    }
}
