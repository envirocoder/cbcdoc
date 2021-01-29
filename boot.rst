************
Boot process
************

CodeBug Connect has three boot modes.

* By default CodeBug Connect boots in run mode. The exact behaviour
  depends on the :ref:`Run mode boot configuration`.
* Pressing and holding the centre of button A while applying power will 
  cause CodeBug Connect to boot as a USB drive. To prevent file system 
  corruption it will not run any of your programs at the same time.
* CodeBug Connect can be set to upgrade itself. As part of this it will 
  boot in a special mode to update its operating system. If it fails to 
  find its operating system it will boot into upgrade mode. Upgrade more is 
  completely separate mode which has no access to the filesystem and
  cannot run your programs. See :doc:`updating` for more information.

Run mode
========

boot configuration
------------------

In normal run mode, CodeBug Connect can do some tasks automatically,
such as automatically connecting to a WiFi network, checking for updates 
or starting its webserver. These boot options are specified in the 
``config.json`` file.

.. code-block:: json

  {
          "start_ap": true,
          "auto_connect": true,
          "fallback_to_ap": true,
          "start_mdns": true,
          "start_webconsole": true,
          "start_webserver": true,
          "remote_checkin": "https://cbc.codebug.org.uk",
          "remote_debug": true,
          "wait_for_connection": true,
          "button_b_wifi_boot" : true
  }

You can set the options graphically, through the web interface. Alternatively
you can edit the ``config.json`` just as you would any other file; either 
over USB as a removable drive, or through the web client.

running your program
--------------------

Once the actions specified in ``config.json`` are complete, your CodeBug 
Connect runs the ``boot.py`` file. This file can either contain code to run
directly, or link to run your projects.

.. warning:: ``boot.py`` can be automatically setup when you deploy a project, so it may
  get overwritten. As such you are advised to keep you programs in their own
  file, and reference them in ``boot.py``.
