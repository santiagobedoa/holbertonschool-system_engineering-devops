# 0x06. Regular expression

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Background Context
  </h2>
  <p>
   For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
  </p>
  <p>
   Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the
   <code>
    //
   </code>
   :
  </p>
  <pre><code>sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
</code></pre>
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
    <a href="https://www.slideshare.net/neha_jain/introducing-regular-expressions" target="_blank" title="Regular expressions - basics">
     Regular expressions - basics
    </a>
   </li>
   <li>
    <a href="https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518" target="_blank" title="Regular expressions - advanced">
     Regular expressions - advanced
    </a>
   </li>
   <li>
    <a href="https://rubular.com/" target="_blank" title="Rubular is your best friend">
     Rubular is your best friend
    </a>
   </li>
   <li>
    <a href="https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/" target="_blank" title="Use a regular expression against a problem: now you have 2 problems">
     Use a regular expression against a problem: now you have 2 problems
    </a>
   </li>
   <li>
    <a href="https://regexone.com/" target="_blank" title="Learn Regular Expressions with simple, interactive exercises">
     Learn Regular Expressions with simple, interactive exercises
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
    <strong>
     All your script files must be executable
    </strong>
   </li>
   <li>
    The first line of all your Bash scripts should be exactly
    <code>
     #!/usr/bin/env ruby
    </code>
   </li>
   <li>
    All your regex must be built for the Oniguruma library
   </li>
  </ul>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/78#quiz-completed)
</html>