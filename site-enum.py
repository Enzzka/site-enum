import socket
import ssl

paths = [
    "config.php", "config.json", "config.yml", "database.sql", "backup.zip", 
    "backup.tar.gz", "db.sql", ".git/", ".env", ".env.bak", ".git/config", 
    ".gitignore", ".htaccess", "web.config", "wp-config.php.bak", "index.php.bak", 
    "settings.py", "docker-compose.yml", "package.json", "composer.json", "admin/", 
    "administrator/", "wp-admin/", "login/", "login.php", "cpanel/", "dashboard/", 
    "controlpanel/", "manage/", "manager/", "secret/", "private/", "root/", 
    "secure/", "signin/", "user/login/", "auth/", "backend/", "webadmin/", 
    "phpmyadmin/", "robots.txt", "sitemap.xml", ".well-known/security.txt", 
    "phpinfo.php", "info.php", "status/", "server-status/", "logs/", "error.log", 
    "access.log", "debug/", "test/", "dev/", "demo/", "staging/", "readme.html", 
    "license.txt", "changelog.txt", "version/", "build/", "api/", "api/v1/", 
    "api/v2/", "graphql/", "swagger/", "swagger.json", "api-docs/", "v1/", 
    "v2/", "rest/", "uploads/", "upload/", "files/", "images/", "assets/", 
    "media/", "static/", "downloads/", "documents/", "attachments/", "manager/html", 
    "actuator/", "actuator/env", "actuator/heapdump", "console/", "invoker/", 
    "jmx-console/", "jfs/", "jenkins/", "gitweb/", "old/", "new/", "temp/", 
    "tmp/", "src/", "main/", "include/", "includes/", "lib/", "cron/", "admin"
]

domain = "www.google.com"

i = 0
found = False

while i < len(paths):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((domain, 443))
        
        ctx = ssl.create_default_context()

        tls = ctx.wrap_socket(
            s,
            server_hostname = domain
        )


        request = (f"GET /{paths[i]} HTTP/1.1\r\nHost: {domain}\r\nUser-Agent: kontol-keren\r\nConnection: close\r\n\r\n").encode()
        
        tls.sendall(request)

        final = b""
        
        while True:
            data = tls.recv(4096)

            if not data:
                break

            final += data


        packet = final.decode(errors='ignore')
        header, body = packet.split("\r\n\r\n", 1)
        yes_or_no = f"Path: /{paths[i]} -> {header.split('\r\n')[0]}"

        if "200 OK" in yes_or_no:
            found = True
            print(yes_or_no)
            

        i += 1

if not found:
    print('No Paths Found')

print("Done Scanning")