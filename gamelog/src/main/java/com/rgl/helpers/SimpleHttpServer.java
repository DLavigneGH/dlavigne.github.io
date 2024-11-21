package com.rgl.helpers;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.net.InetSocketAddress;

/**
 * Starts a simple HTTP server to serve files from the application's execution directory.
 * 
 * The server listens on port 8080 and serves files located in the root directory of the application. 
 * If a file is not found, it returns a 404 response.
 */

public class SimpleHttpServer {

    /**
     * Starts the HTTP server that listens on port 8080 and serves files from the execution directory.
     * 
     * This method creates an HTTP server that serves files from the root directory where the application is running.
     * If a requested file does not exist, it returns a 404 error. If the file is found, it returns the file content with a 200 OK status.
     *
     * @throws Exception if an error occurs while starting the server.
     */
    public static void startServer() throws Exception {
        // Serve from the target directory (assuming the JAR is executed from target)
        String rootDir = System.getProperty("user.dir"); // This should be the target directory
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);

        // Serve files from the target directory
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String uri = exchange.getRequestURI().getPath();
                String filePath = rootDir + uri;

                // If file doesn't exist, return 404
                if (!Files.exists(Paths.get(filePath))) {
                    exchange.sendResponseHeaders(404, -1);
                    return;
                }

                try (InputStream fileStream = Files.newInputStream(Paths.get(filePath))) {
                    byte[] response = fileStream.readAllBytes();
                    exchange.sendResponseHeaders(200, response.length);
                    OutputStream os = exchange.getResponseBody();
                    os.write(response);
                    os.close();
                } catch (IOException e) {
                    e.printStackTrace();
                    exchange.sendResponseHeaders(500, -1);
                }
            }
        });

        server.start();
        System.out.println("Server started on http://localhost:8080");
    }
}
