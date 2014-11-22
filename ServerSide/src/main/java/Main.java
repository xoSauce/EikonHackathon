/**
 * Created by XelnectPC on 11/22/2014.
 */
import static spark.Spark.*;
import spark.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class Main {


    public static ArrayList<String> things = new ArrayList<String>();

    public static void main(String[] args) {


        get(new Route("/hello") {
            @Override
            public Object handle(Request request, Response response) {
                StringBuilder html = new StringBuilder();

                StringBuilder contentBuilder = new StringBuilder();
                try {
                  BufferedReader in = new BufferedReader(new FileReader("C:/Users/XelnectPC/Documents/GitHub/EikonHackathon/app/frontEnd/public_html/index.html"));
                    String str;
                    while ((str = in.readLine()) != null) {
                        contentBuilder.append(str);
                    }
                    in.close();
                } catch (IOException e) {
                }
                String content = contentBuilder.toString();
                return content;
            }
        });

        post(new Route("/add/:item") {
            @Override
            public Object handle(Request request, Response response) {
                Main.things.add(request.params(":item"));
                response.status(200);
                return response;
            }
        });
    }

}