/**
 * Contains utility classes for supporting various application functionalities.
 * 
 * This package includes:
 * 
 * - HtmlOpener: Handles opening HTML files in the system's default web browser.
 *   It provides functionality to extract an HTML resource from the application's
 *   classpath to the execution directory and open it in the browser.
 * 
 * - ResourceExtractor: Extracts resource files from the application classpath to the
 *   target directory. Currently used to copy the `index.html` file to the execution
 *   directory, ensuring it is available for the application to serve or open.
 * 
 * - SimpleHttpServer: Starts a simple HTTP server that serves files from the application's
 *   execution directory. The server listens on port 8080 and serves files located in the
 *   root directory of the application, returning a 404 response if a file is not found.
 */

package com.rgl.helpers;