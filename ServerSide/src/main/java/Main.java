/**
 * Created by XelnectPC on 11/22/2014.
 */
import static spark.Spark.*;
import spark.*;

public class Main {


    public static void main(String[] args) {
        get(new Route("/hello") {
            @Override
            public Object handle(Request request, Response response) {
                return "Hello Spark MVC Frameworkfdgfdgfdgfdgfdgfdgfdgd!" +somethingmethod();
            }

        });
    }
    public static String somethingmethod(){
        String something ="fese";
        return something;
    }

}