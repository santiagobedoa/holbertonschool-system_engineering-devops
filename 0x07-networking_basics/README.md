# 0x07. Networking basics #0

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
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
    <a href="https://en.wikipedia.org/wiki/OSI_model" target="_blank" title="OSI model">
     OSI model
    </a>
   </li>
   <li>
    <a href="https://www.lifewire.com/lans-wans-and-other-area-networks-817376" target="_blank" title="Different types of network">
     Different types of network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Local_area_network" target="_blank" title="LAN network">
     LAN network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Wide_area_network" target="_blank" title="WAN network">
     WAN network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Internet" target="_blank" title="Internet">
     Internet
    </a>
   </li>
   <li>
    <a href="https://whatismyipaddress.com/mac-address" target="_blank" title="MAC address">
     MAC address
    </a>
   </li>
   <li>
    <a href="https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/" target="_blank" title="What is an IP address">
     What is an IP address
    </a>
   </li>
   <li>
    <a href="https://www.iplocation.net/public-vs-private-ip-address" target="_blank" title="Private and public address">
     Private and public address
    </a>
   </li>
   <li>
    <a href="https://www.webopedia.com/insights/ipv6-ipv4-difference/" target="_blank" title="IPv4 and IPv6">
     IPv4 and IPv6
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Localhost" target="_blank" title="Localhost">
     Localhost
    </a>
   </li>
   <li>
    <a href="https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/" target="_blank" title="TCP and UDP">
     TCP and UDP
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers" target="_blank" title="TCP/UDP ports List">
     TCP/UDP ports List
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Ping_%28networking_utility%29" target="_blank" title="What is ping /ICMP">
     What is ping /ICMP
    </a>
   </li>
   <li>
    <a href="https://wiki.bash-hackers.org/scripting/posparams" target="_blank" title="Positional parameters">
     Positional parameters
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
     netstat
    </code>
   </li>
   <li>
    <code>
     ping
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
   OSI Model
  </h3>
  <ul>
   <li>
    What it is
   </li>
   <li>
    How many layers it has
   </li>
   <li>
    How it is organized
   </li>
  </ul>
  <h3>
   What is a LAN
  </h3>
  <ul>
   <li>
    Typical usage
   </li>
   <li>
    Typical geographical size
   </li>
  </ul>
  <h3>
   What is a WAN
  </h3>
  <ul>
   <li>
    Typical usage
   </li>
   <li>
    Typical geographical size
   </li>
  </ul>
  <h3>
   What is the Internet
  </h3>
  <ul>
   <li>
    What is an IP address
   </li>
   <li>
    What are the 2 types of IP address
   </li>
   <li>
    What is
    <code>
     localhost
    </code>
   </li>
   <li>
    What is a subnet
   </li>
   <li>
    Why IPv6 was created
   </li>
  </ul>
  <h3>
   TCP/UDP
  </h3>
  <ul>
   <li>
    What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
   </li>
   <li>
    What is the main difference between TCP and UDP
   </li>
   <li>
    What is a port
   </li>
   <li>
    Memorize SSH, HTTP and HTTPS port numbers
   </li>
   <li>
    What tool/protocol is often used to check if a device is connected to a network
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
    All your Bash script files will be interpreted on Ubuntu 20.04 LTS
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
     shellcheck
    </code>
    without any error
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
  <h2>
   More Info
  </h2>
  <p>
   The second line of all your Bash scripts should be a comment explaining what is the script doing
  </p>
  <p>
   For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:
  </p>
  <p>
   What is the most important position in a software company?
  </p>
  <ol>
   <li>
    Project manager
   </li>
   <li>
    Backend developer
   </li>
   <li>
    System administrator
   </li>
  </ol>
  <pre><code>sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
</code></pre>
  <p>
   Source for question 1
   <a href="https://twitter.com/devopsreact/status/831922429215662080" target="_blank" title="here">
    here
   </a>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/259)
</html>