Sum Sequence
============

Given a positive number N, this program will generate all the possible series
of positive integers, satisfying the following conditions,

1. Numbers in a series are in descending order;
2. The sum of all the numbers in a series must be equal to N, 


[![Build Status](https://travis-ci.org/gchiam/sum-sequence.svg?branch=master)](https://travis-ci.org/gchiam/sum-sequence)
[![Build Status](https://drone.io/github.com/gchiam/sum-sequence/status.png)](https://drone.io/github.com/gchiam/sum-sequence/latest)
[![Coverage Status](https://img.shields.io/coveralls/gchiam/sum-sequence.svg)](https://coveralls.io/r/gchiam/sum-sequence?branch=master)

Example:

```
$ python sum_sequence.py 3
[3]
[2, 1]
[1, 1, 1]
```

```
$python sum_sequence.py 6
[6]
[5, 1]
[4, 2]
[4, 1, 1]
[3, 3]
[3, 2, 1]
[3, 1, 1, 1]
[2, 2, 2]
[2, 2, 1, 1]
[2, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
```
