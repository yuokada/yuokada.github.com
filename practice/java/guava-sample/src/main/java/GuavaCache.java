import java.util.Arrays;
import java.util.List;
import java.util.StringJoiner;

/**
 * Created by yukihirookada on 2017/06/29.
 */
public class GuavaCache
{

    public static void main(String[] args)
    {
        StringJoiner joiner = new StringJoiner(" , ", "{", "]");
        joiner.add("d").add("e").add("f").toString();
        System.out.println(joiner.toString());

        List<String> ls1 = Arrays.asList("foo", "bar", "baz");
        String[] ls = new String[] {"foo", "bar", "baz"};
        List<String> ls2 = Arrays.asList(ls);

        System.out.println(ls.hashCode());
        System.out.println(ls2.toString());
    }
}
