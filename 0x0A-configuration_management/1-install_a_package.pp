# install flask from pipe

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
