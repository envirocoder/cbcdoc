*****************
Remote Deployment
*****************

CodeBug Connect can automatically fetch and then run projects from the CodeBug Website. However, so that only you have remote access to your CodeBug Connect you first need to associate it with your CodeBug website account. This process is known as adoption. As you'd probably expect, if you want to deploy remotely over the Internet your CodeBug Connect needs access to the Internet via a WiFi network. For details about setting up WiFi see :doc:`setup_wifi`.

Adoption
========

CodeBug Connects can only be adopted by one account at once. By default they become locked to that account to prevent them from being taken over by someone else (though it is possible to manually unlock them). To adopt a CodeBug Connect, you need to put an adoption key onto its file system. You can adopt multiple CodeBug Connects to your account using the same adoption key.

#. Visit |codebug_adoption_link| page and, if not already, log into the account from which you wish to do the adoption.

   .. |codebug_adoption_link| raw:: html

     <a href="https://www.codebug.org.uk/newide/adoptionkey/" target="_blank">CodeBug Connect Adoption</a>


#. Click ``Download Key``. You should obtain a file ``adoption_key.dat``.

#. Copy the ``adoption_key.dat`` file into the top level directory (not in a sub-folder) of your CodeBug Connect. Follow the instructions in :doc:`quickstart` about transferring files. 

   .. warning:: Ensure that the file name matches ``adoption_key.dat`` and your web browser has not renamed it to ``adoption_key-1.dat`` or similar, as these will not work.

#. After ejecting (or for some operating systems unmounting) the CodeBug Connect USB disk unplug and remove power.

#. Re-apply power and your CodeBug Connect will reboot and try and associate itself with the CodeBug website. Wait until you see a green downward arrow.

#. Check your CodeBug Connect has been successfully adopted. If successful your CodeBug Connect will be listed on the |my_codebugs_link| page of the website and your username should be stored on your CodeBug Connect's filesystem in the file ``owner.txt``.

   .. |my_codebugs_link| raw:: html

     <a href="https://www.codebug.org.uk/newide/devices" target="_blank">My CodeBug Connects</a>
