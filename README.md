# 3DS_Game_Server

Creates a web page listing from user-provided CIAs.
Generated web page includes a sortable table with auto-generated QR codes for downloading/installing the CIAs over LAN via FBI.
Game titles link to descriptions on www.gametdb.com, and table also pulls cover art from there.
Uses Python SimpleHTTPServer, so just one download request/thread at a time.

Requires Python 2.7

To use an updated releases list, download '3dsreleases.xml' from http://www.3dsdb.com/ (this file should me named 3dsreleases.xml but I put one in this project if you have problems downloading it)

1. Create a folder named CIAS in the root of this projects
2. Create a folder to match the name set in "ciaFolder"
3. Dump all desired CIAs into the created folder (subfolders are OK)
4. Run BuildCatalog.py
5. Run StartServer.py
