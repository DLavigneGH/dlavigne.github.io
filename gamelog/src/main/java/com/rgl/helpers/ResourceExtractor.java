package com.rgl.helpers;

import java.io.InputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * Extracts resource files from the application classpath to the target directory.
 * 
 * Currently used to copy the `index.html` and `script.js` files to the execution directory,
 * ensuring they are available for the application to serve or open.
 */
public class ResourceExtractor {

    /**
     * Copies the list of resource files to the target directory.
     * 
     * @param resourceNames Array of resource file names (e.g., "index.html", "script.js").
     */
    public static void copyResourcesToTarget(String... resourceNames) {
        for (String resourceName : resourceNames) {
            copyResourceToTarget(resourceName);
        }
    }

    /**
     * General method to copy a resource file from the classpath to the target directory.
     * 
     * @param resourceName The name of the resource file to copy (e.g., "index.html" or "script.js").
     */
    private static void copyResourceToTarget(String resourceName) {
        InputStream in = ResourceExtractor.class.getClassLoader().getResourceAsStream(resourceName);

        if (in == null) {
            System.out.println("Resource not found: " + resourceName);
            return;
        }

        try {
            // Define the output path in the target folder (root)
            String outputPath = Paths.get(System.getProperty("user.dir"), resourceName).toString();
            
            // Ensure the directory exists
            Files.createDirectories(Paths.get(System.getProperty("user.dir")));

            // Create the output stream to write to the target folder
            try (FileOutputStream out = new FileOutputStream(outputPath)) {
                byte[] buffer = new byte[1024];
                int length;
                while ((length = in.read(buffer)) > 0) {
                    out.write(buffer, 0, length);
                }
            }

            System.out.println(resourceName + " copied to: " + outputPath);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}