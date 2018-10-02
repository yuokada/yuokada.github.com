import org.apache.http.client.fluent.Request;
import org.apache.http.client.fluent.Response;

/**
 * Created by yukihirookada on 2017/07/01.
 */
public class HttpClientSample
{
    public static void main(String[] args)
    {
        try {
            Response response = Request.Get("http://www.yahoo.co.jp").execute();
            String body = response.returnContent().asString();
            System.out.println(body);
        }
        catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
