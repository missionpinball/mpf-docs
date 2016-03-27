To create a new branch for a new version of MPF:
------------------------------------------------

1. Fork the latest branch in GitHub
2. Change the URL curl entry in .travis.yml
3. Change the 'version' and 'release' in conf.py
4. Add the new version to the menu in all branch's navbar.html
5. Republish all branches

To publish the release branch
-----------------------------

1. Change the list entries in all branch's navbar.html pages.
2. Republish all branches
3. Edit the .htaccess file in the root of the home folder for docs.missionpinball.com to set the default redirect to the
   latest version of the docs.
