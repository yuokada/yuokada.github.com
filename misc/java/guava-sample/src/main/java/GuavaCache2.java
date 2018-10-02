import com.google.common.cache.Cache;
import com.google.common.cache.CacheBuilder;
import com.google.common.cache.CacheLoader;
import com.google.common.cache.LoadingCache;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

/**
 * Created by yuokada on 2017/08/14.
 */
public class GuavaCache2
{

    // http://d.hatena.ne.jp/Kazuhira/20130723/1374587549
    // http://www.baeldung.com/guava-cache
    public static void main(String[] args)
    {
        Cache<String, String> cache = CacheBuilder.newBuilder()
                .maximumSize(100)
                .expireAfterAccess(1, TimeUnit.SECONDS)
                .expireAfterWrite(2, TimeUnit.SECONDS)
                .build();

        CacheLoader<String, String> loader = new CacheLoader<String, String>(){
            @Override
            public String load(String key) throws Exception {
                return key.toUpperCase();
            }
        };

        LoadingCache<String, String> loadingCache = CacheBuilder.newBuilder()
                .maximumSize(100)
                .expireAfterAccess(1, TimeUnit.SECONDS)
                .expireAfterWrite(2, TimeUnit.SECONDS)
                .build(loader);

        cache.put("key1", "v1");
        cache.put("key2", "v2");
        Map<String, String> m = new HashMap<String, String>(){{
                put("key01", "v01");
                put("key02", "v02");
        }};
        cache.putAll(m);

        System.out.println(cache.getIfPresent("key1"));;
        System.out.println(cache.getIfPresent("key01"));;

        try {
            System.out.println("wait a second.");;
            Thread.sleep(3000);
        }
        catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println(cache.getIfPresent("key1"));;
        System.out.println(cache.getIfPresent("key01"));;
        try {
            System.out.println(loadingCache.get("foo"));
        }
        catch (ExecutionException e) {
            e.printStackTrace();
        }

//        String sample = "a,  goo d b,c,d";
//        Splitter splitter = Splitter.on(",").omitEmptyStrings().trimResults();
//        List<String> ls = splitter.splitToList(sample);
//        ls.stream().forEach(x -> System.out.printf("[%s]", x));  // [a][goo d b][c][d]

        System.out.println();

//        String sample2 = "foo\tbar \t baz,boo";
//        Splitter splitter2 = Splitter.onPattern("[,\\s]").omitEmptyStrings().trimResults();
//        List<String> ls2 = splitter2.splitToList(sample2);
//        ls2.stream().forEach(x -> System.out.printf("[%s]", x));  // [foo][bar][baz][boo]
    }
}
