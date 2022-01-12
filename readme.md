Utility Functions
=========================

Summary
-------

This library contains python native code to provide generic functionality
needed but not included in the standard library.  

Compatability
-------------

This library is tested with python 3.x

Components
---------

 + fntools-like helpers:
   + compose - functional composition
   + cut - port of SRFI-26 to python - partial application using a placeholder
   + identity - identity first class function
 + Iteration / List helpers:
   + unzip - opposite of zip
   + count_if - count if the predicate matches
   + take - take up to n items from an iterator
   + skip - skip n items from an iterator and take the rest
   + map_into - destructive map
   + remove_if - destructive remove
   + unique - only iterate over unique items
   + first, second, ... nth - first class functions to get a specific element from an iterable 
 + Shell script helpers:
   + chomp - form perl remove line-endings
   + die - perl-like print an error to stderr and exit
   + warn - perl-like print an error to stderr
   + in_directory - with-clause equivalent of pushd/popd
   + directory_removed_after - with-clause; remove a directory after the block
   + file_removed_after - with-clause; remove a file after the block
 + Symbol - symbol like dataclass can be used for sentinel values
 + pubsub - submodule that implements a simple pubsub mechanism 
