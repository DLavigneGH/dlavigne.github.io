package com.rgl.helpers;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class FileUtils {

    public static boolean deleteFile(File file) {
        if (file.exists()) {
            return file.delete();
        }
        return false;
    }

    public static File copyFileToDirectory(File sourceFile, File targetDirectory) throws IOException {
        if (!targetDirectory.exists()) {
            targetDirectory.mkdirs(); // Ensure the directory exists
        }

        String originalFileName = sourceFile.getName();
        File newFile = new File(targetDirectory, originalFileName);

        int counter = 1;
        while (newFile.exists()) {
            String nameWithoutExtension = originalFileName.substring(0, originalFileName.lastIndexOf('.'));
            String extension = originalFileName.substring(originalFileName.lastIndexOf('.'));
            newFile = new File(targetDirectory, nameWithoutExtension + "_" + counter + extension);
            counter++;
        }

        Files.copy(sourceFile.toPath(), newFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
        return newFile;
    }
}
