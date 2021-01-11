************
Boot process
************

CodeBug Connect has configuration options that control the boot process.

* Pressing and holding the centre of button A while applying power will 
  cause CodeBug Connect to boot as a USB drive. To avoid the chance of 
  file system corruption it will not run any of your programs.
* CodeBug Connect can be set to upgrade itself. As part of this it will 
  boot in a special mode to update its operating system. If it fails to 
  find its operating system it will boot into upgrade mode. Upgrade more is 
  completely separate mode which has no access to the filesystem and
  cannot run your programs. See :doc:`updating` for more information.
* By default CodeBug Connect boots in run mode. The exact behaviour
  depends on the config.json file.

Run mode boot configuration
===========================

Does internal setup, checks config.json

            'start_ap': True,
            'auto_connect': True,
            'fallback_to_ap': True,
            'start_mdns': True,
            'start_webconsole': True,
            'start_webserver': True,
            'remote_checkin': "http://www.codebug.org.uk",
            'remote_debug': True,
            'wait_for_connection': True,

config.json 
select options through web interface

then if found in the filesystem runs boot.py. This file can then run your projects
setup by default when you deploy a project.
