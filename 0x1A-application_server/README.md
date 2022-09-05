# 0x1A. Application server

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <p>
   <img alt="" loading="lazy" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220904%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220904T201534Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=596bd6ac40d06b8d6e881ade3a4704f39fd6162c4dacaaa10b9016fd7d09f4ad" style=""/>
  </p>
  <h2>
   Background Context
  </h2>
  <p>
   <a href="https://youtu.be/pSrKT7m4Ego" target="_blank">
    <img alt="" loading="lazy" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/2ea1058f813d42c61f48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220904%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220904T201534Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=af12b13d561d38613a4b146e91eb8111a8d0b5db3ff2f62f9ea7436a1a30d4ef" style=""/>
   </a>
  </p>
  <p>
   Your web infrastructure is already serving web pages via
   <code>
    Nginx
   </code>
   that you installed in your
   <a href="https://intranet.hbtn.io/projects/266" target="_blank" title="first web stack project">
    first web stack project
   </a>
   . While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your
   <code>
    Nginx
   </code>
   and make is serve your Airbnb clone project.
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
    <a href="https://www.nginx.com/resources/glossary/application-server-vs-web-server/" target="_blank" title="Application server vs web server">
     Application server vs web server
    </a>
   </li>
   <li>
    <a href="https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04" target="_blank" title="How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04">
     How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
    </a>
    (As mentioned in the video, do
    <strong>
     not
    </strong>
    install Gunicorn using
    <code>
     virtualenv
    </code>
    , just install everything globally)
   </li>
   <li>
    <a href="https://docs.gunicorn.org/en/latest/run.html" target="_blank" title="Running Gunicorn">
     Running Gunicorn
    </a>
   </li>
   <li>
    <a href="https://werkzeug.palletsprojects.com/en/0.14.x/routing/" target="_blank" title="Be careful with the way Flask manages slash">
     Be careful with the way Flask manages slash
    </a>
    in
    <a href="http://flask.pocoo.org/docs/1.0/api/#flask.Flask.route" target="_blank" title="route">
     route
    </a>
    -
    <code>
     strict_slashes
    </code>
   </li>
   <li>
    <a href="https://upstart.ubuntu.com/cookbook/" target="_blank" title="Upstart documentation">
     Upstart documentation
    </a>
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
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    Everything Python-related must be done using
    <code>
     python3
    </code>
   </li>
   <li>
    All config files must have comments
   </li>
  </ul>
  <h3>
   Bash Scripts
  </h3>
  <ul>
   <li>
    All your files will be interpreted on Ubuntu 16.04 LTS
   </li>
   <li>
    All your files should end with a new line
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
     0.3.7-5~ubuntu16.04.1
    </code>
    via
    <code>
     apt-get
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
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/311)
</html>