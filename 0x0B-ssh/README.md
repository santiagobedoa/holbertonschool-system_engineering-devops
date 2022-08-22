# 0x0B. SSH

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Background Context
  </h2>
  <p>
   <img alt="" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" style=""/>
  </p>
  <p>
   Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away.  Like level 2 of the application process, you will connect using
   <code>
    ssh
   </code>
   . But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of
   <a href="https://intranet.hbtn.io/tasks/1223" target="_blank" title="a previous project">
    a previous project
   </a>
   shared in your
   <a href="https://intranet.hbtn.io/users/my_profile" target="_blank" title="intranet profile">
    intranet profile
   </a>
   .
  </p>
  <p>
   You can access your server information in the
   <a href="https://intranet.hbtn.io/dashboards/my_server" target="_blank" title="my servers">
    my servers
   </a>
   section of the intranet, each line with contains the IP and username you should use to connect via
   <code>
    ssh
   </code>
   .
  </p>
  <p>
   <strong>
    Note:
   </strong>
   Your server is configured with an Ubuntu 20.04 LTS environment.
  </p>
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="https://en.wikipedia.org/wiki/Server_%28computing%29#Hardware_requirement" target="_blank" title="What is a (physical) server - text">
     What is a (physical) server - text
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=B1ANfsDyjeA" target="_blank" title="What is a (physical) server - video">
     What is a (physical) server - video
    </a>
   </li>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys" target="_blank" title="SSH essentials">
     SSH essentials
    </a>
   </li>
   <li>
    <a href="https://www.ssh.com/academy/ssh/config" target="_blank" title="SSH Config File">
     SSH Config File
    </a>
   </li>
   <li>
    <a href="https://www.ssh.com/academy/ssh/public-key-authentication" target="_blank" title="Public Key Authentication for SSH">
     Public Key Authentication for SSH
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=ORcvSkgdA58" target="_blank" title="How Secure Shell Works">
     How Secure Shell Works
    </a>
   </li>
   <li>
    <a href="https://www.youtube.com/watch?v=hQWRp-FdTpc" target="_blank" title="SSH Crash Course">
     SSH Crash Course
    </a>
    (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)
   </li>
  </ul>
  <p>
   <strong>
    For reference:
   </strong>
  </p>
  <ul>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process" target="_blank" title="Understanding the SSH Encryption and Connection Process">
     Understanding the SSH Encryption and Connection Process
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Secure_Shell" target="_blank" title="Secure Shell Wiki">
     Secure Shell Wiki
    </a>
   </li>
   <li>
    <a href="https://www.ietf.org/rfc/rfc4251.txt" target="_blank" title="IETF RFC 4251 (Description of the SSH Protocol)">
     IETF RFC 4251 (Description of the SSH Protocol)
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force" target="_blank" title="Internet Engineering Task Force">
     Internet Engineering Task Force
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Request_for_Comments" target="_blank" title="Request for Comments">
     Request for Comments
    </a>
   </li>
  </ul>
  <p>
   <strong>
    man or help
   </strong>
   :
  </p>
  <ul>
   <li>
    <code>
     ssh
    </code>
   </li>
   <li>
    <code>
     ssh-keygen
    </code>
   </li>
   <li>
    <code>
     env
    </code>
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   General
  </h3>
  <ul>
   <li>
    What is a server
   </li>
   <li>
    Where servers usually live
   </li>
   <li>
    What is SSH
   </li>
   <li>
    How to create an SSH RSA key pair
   </li>
   <li>
    How to connect to a remote host using an SSH RSA key pair
   </li>
   <li>
    The advantage of using
    <code>
     #!/usr/bin/env bash
    </code>
    instead of
    <code>
     /bin/bash
    </code>
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your files will be interpreted on Ubuntu 20.04 LTS
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    All your Bash script files must be executable
   </li>
   <li>
    The first line of all your Bash scripts should be exactly
    <code>
     #!/usr/bin/env bash
    </code>
   </li>
   <li>
    The second line of all your Bash scripts should be a comment explaining what is the script doing
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/244)
</html>