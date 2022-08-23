# 0x0C. Web server

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" style=""/>
  </p>
  <h2>
   Background Context
  </h2>
  <p>
   <a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&amp;feature=youtu.be&amp;hd=1" target="_blank">
    <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" style=""/>
   </a>
  </p>
  <p>
   In this project, some of the tasks will be graded on 2 aspects:
  </p>
  <ol>
   <li>
    Is your
    <code>
     web-01
    </code>
    server configured according to requirements
   </li>
   <li>
    Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
   </li>
  </ol>
  <p>
   For example, if I need to create a file
   <code>
    /tmp/test
   </code>
   containing the string
   <code>
    hello world
   </code>
   and modify the configuration of Nginx to listen on port
   <code>
    8080
   </code>
   instead of
   <code>
    80
   </code>
   , I can use
   <code>
    emacs
   </code>
   on my server to create the file and to modify the Nginx configuration file
   <code>
    /etc/nginx/sites-enabled/default
   </code>
   .
  </p>
  <p>
   But my answer file would contain:
  </p>
  <pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>
  <p>
   As you can tell, I am not using
   <code>
    emacs
   </code>
   to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an
   <a href="https://www.atlassian.com/incident-management/devops/sre" target="_blank" title="SRE">
    SRE
   </a>
   , that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the
   <code>
    root
   </code>
   user, you do not need to use the
   <code>
    sudo
   </code>
   command.
  </p>
  <p>
   A good Software Engineer is a
   <a href="https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb" target="_blank" title="lazy Software Engineer">
    lazy Software Engineer
   </a>
   .
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" style=""/>
  </p>
  <p>
   Tips: to test your answer Bash script, feel free to reproduce the checker environment:
  </p>
  <ul>
   <li>
    start a
    <code>
     Ubuntu 16.04
    </code>
    sandbox
   </li>
   <li>
    run your script on it
   </li>
   <li>
    see how it behaves
   </li>
  </ul>
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
    <a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works" target="_blank" title="How the web works">
     How the web works
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Nginx" target="_blank" title="Nginx">
     Nginx
    </a>
   </li>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04" target="_blank" title="How to Configure Nginx">
     How to Configure Nginx
    </a>
   </li>
   <li>
    <strong>
     Child process
    </strong>
    concept page
   </li>
   <li>
    <a href="https://landingi.com/help/domains-vs-subdomains/" target="_blank" title="Root and sub domain">
     Root and sub domain
    </a>
   </li>
   <li>
    <a href="https://www.tutorialspoint.com/http/http_methods.htm" target="_blank" title="HTTP requests">
     HTTP requests
    </a>
   </li>
   <li>
    <a href="https://moz.com/learn/seo/redirection" target="_blank" title="HTTP redirection">
     HTTP redirection
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/HTTP_404" target="_blank" title="Not found HTTP response code">
     Not found HTTP response code
    </a>
   </li>
   <li>
    <a href="https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/" target="_blank" title="Logs files on Linux">
     Logs files on Linux
    </a>
   </li>
  </ul>
  <p>
   <strong>
    For reference:
   </strong>
  </p>
  <ul>
   <li>
    <a href="https://datatracker.ietf.org/doc/html/rfc7231" target="_blank" title="RFC 7231 (HTTP/1.1)">
     RFC 7231 (HTTP/1.1)
    </a>
   </li>
   <li>
    <a href="https://datatracker.ietf.org/doc/html/rfc7540" target="_blank" title="RFC 7540 (HTTP/2)">
     RFC 7540 (HTTP/2)
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
     scp
    </code>
   </li>
   <li>
    <code>
     curl
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
    What is the main role of a web server
   </li>
   <li>
    What is a child process
   </li>
   <li>
    Why web servers usually have a parent process and child processes
   </li>
   <li>
    What are the main HTTP requests
   </li>
  </ul>
  <h3>
   DNS
  </h3>
  <ul>
   <li>
    What DNS stands for
   </li>
   <li>
    What is DNS main role
   </li>
  </ul>
  <h3>
   DNS Record Types
  </h3>
  <ul>
   <li>
    <code>
     A
    </code>
   </li>
   <li>
    <code>
     CNAME
    </code>
   </li>
   <li>
    <code>
     TXT
    </code>
   </li>
   <li>
    <code>
     MX
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
    All your files will be interpreted on Ubuntu 16.04 LTS
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
    Your Bash script must pass
    <code>
     Shellcheck
    </code>
    (version
    <code>
     0.3.7
    </code>
    ) without any error
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
   <li>
    You can’t use
    <code>
     systemctl
    </code>
    for restarting a process
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/266)
</html>