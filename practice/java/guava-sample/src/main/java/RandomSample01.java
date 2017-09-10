import org.apache.commons.text.RandomStringGenerator;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by yukihirookada on 2017/07/02.
 */
public class RandomSample01
{
    public static void main(String[] args)
    {
        Random rnd = new Random();
//        rnd.ints(100, 0, 10000)
//                .sequential()
//                .sorted()
//                .forEach(System.out::println);
        List<Integer> ints = rnd.ints(100, 0, 10000).sequential()
                .boxed()
                .sorted().collect(Collectors.toList());
        for (Integer i : ints) {
            System.out.println(i);
        }

        RandomStringGenerator generator = new RandomStringGenerator.Builder()
                .withinRange('A', 'z').build();
        IntStream.rangeClosed(1, 10).forEach(
                i -> System.out.println(((Integer) i).toString() + " : " + generator.generate(10))
        );
        Map<String, Integer> xmap = new HashMap<String, Integer>()
        {
            {
                put("foo", 100);
                put("bar", 200);
                put("baz", 128);
            }
        };
        xmap.put("bool", 1);
        xmap.put("true", 1);
        xmap.put("false", 0);
        xmap.entrySet().stream().forEach(
                (b) -> System.out.println(b.getKey() + " : " + b.getValue().toString())
        );
//        rnd.ints(10).limit(100)
//        int r = rnd.nextInt(100);
//        System.out.println(r);
    }
}
