# 0x13. Firewall

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" style=""/>
  </p>
  <h2>
   Background Context
  </h2>
  <h3>
   Your servers without a firewall…
  </h3>
  <p>
   <img alt="" loading="lazy" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" style=""/>
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
    <a href="https://en.wikipedia.org/wiki/Firewall_%28computing%29" target="_blank" title="What is a firewall">
     What is a firewall
    </a>
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <p>
   As explained in the
   <strong>
    web stack debugging guide
   </strong>
   concept page,
   <code>
    telnet
   </code>
   is a very good tool to check if sockets are open with
   <code>
    telnet IP PORT
   </code>
   . For example, if you want to check if port 22 is open on
   <code>
    web-02
   </code>
   :
  </p>
  <pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
</code></pre>
  <p>
   We can see for this example that the connection is successful:
   <code>
    Connected to web-02.holberton.online.
   </code>
  </p>
  <p>
   Now let’s try connecting to port 2222:
  </p>
  <pre><code>sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C
sylvain@ubuntu$
</code></pre>
  <p>
   We can see that the connection never succeeds, so after some time I just use
   <code>
    ctrl+c
   </code>
   to kill the process.
  </p>
  <p>
   This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.
  </p>
  <p>
   Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on
   <code>
    web-01
   </code>
   , please perform the test from outside of the school network, like from your
   <code>
    web-02
   </code>
   server. If you SSH into your
   <code>
    web-02
   </code>
   server, the traffic will be originating from
   <code>
    web-02
   </code>
   and not from the school’s network, bypassing the firewall.
  </p>
  <h2>
   Warning!
  </h2>
  <p>
   <strong>
    Containers on demand cannot be used for this project (Docker container limitation)
   </strong>
  </p>
  <p>
   <strong>
    Be very careful with firewall rules! For instance, if you ever deny port
    <code>
     22/TCP
    </code>
    and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.
   </strong>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/284)
</html>